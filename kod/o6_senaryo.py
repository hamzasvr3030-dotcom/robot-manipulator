"""
O6 — Aynı senaryoyu iki parametre setiyle çalıştır, kaydet, karşılaştır.

Senaryo: Eklem 0° → 60° (yumuşak yörünge, 2 s), 5 s kayıt.
  Set A: Kp=60, Ki=150, Kd=4      Set B: Kp=120, Ki=300, Kd=8
Her iki set ayrıca "gerçekçi" modelle de koşulur (gürültü + 10 ms gecikme + kuru sürtünme):
simülasyon ile gerçek arasındaki farkın nasıl görüneceğine bir örnek.
Çıktılar: veri/*.csv (O3'teki betik bunları okur), gorseller/o6_senaryo.png, ekrana özet tablo.
"""
from pathlib import Path
import csv, datetime, platform
import numpy as np
import matplotlib.pyplot as plt
from eklem_sim import PID, Model, simule, olcutler

KOK = Path(__file__).resolve().parent.parent
(KOK / "veri").mkdir(exist_ok=True)

SETLER = {"A": PID(60, 150, 4), "B": PID(120, 300, 8)}
MODELLER = {"ideal": Model(), "gercekci": Model(gurultu=0.05, gecikme=0.010, tau_c=0.3)}

sonuc = {}
for sa, pid in SETLER.items():
    for ma, model in MODELLER.items():
        s = simule(pid, model, hedef=60, tip="quintic", T=5)
        sonuc[(sa, ma)] = (s, olcutler(s, 60))
        yol = KOK / "veri" / f"senaryo_{sa}_{ma}.csv"
        with open(yol, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["# senaryo: 0->60 derece quintic 2 s", f"set {sa}: Kp={pid.Kp} Ki={pid.Ki} Kd={pid.Kd}",
                        f"model: {ma}", f"python {platform.python_version()}", f"numpy {np.__version__}"])
            w.writerow(["t_s", "referans_deg", "gercek_deg", "olcum_deg", "tork_Nm"])
            for k in range(0, len(s["t"]), 10):        # 100 Hz kayıt
                w.writerow([f"{s['t'][k]:.3f}", f"{s['ref'][k]:.4f}", f"{s['q'][k]:.4f}", f"{s['olcum'][k]:.4f}", f"{s['u'][k]:.4f}"])

print(f"{'set':4s} {'model':9s} {'RMSE [°]':>9s} {'maks hata [°]':>14s} {'kalıcı hata [°]':>16s} {'maks tork':>10s}")
for (sa, ma), (s, o) in sonuc.items():
    print(f"{sa:4s} {ma:9s} {o['rmse']:9.3f} {np.abs(s['ref'] - s['q']).max():14.3f} {o['kalici']:+16.3f} {o['maks_tork']:10.2f}")

fig, ax = plt.subplots(1, 2, figsize=(13, 4.6), gridspec_kw={"width_ratios": [1.7, 1]})
stil = {("A", "ideal"): ("#4C72B0", "-"), ("B", "ideal"): ("#DD8452", "-"),
        ("A", "gercekci"): ("#4C72B0", ":"), ("B", "gercekci"): ("#DD8452", ":")}
for (sa, ma), (s, o) in sonuc.items():
    c, ls = stil[(sa, ma)]
    ad = f"Set {sa} · {ma} (RMSE {o['rmse']:.2f}°)"
    ax[0].plot(s["t"], s["ref"] - s["q"], color=c, ls=ls, lw=1.6, label=ad)
ax[0].axhline(0, color="k", lw=.6); ax[0].set_ylabel("hata = referans − gerçek [°]"); ax[0].set_xlabel("t [s]")
ax[0].set_title("Aynı senaryo, iki parametre seti (düz: ideal, noktalı: gerçekçi)"); ax[0].legend(fontsize=8)
ad_l = [f"{sa}\n{ma}" for (sa, ma) in sonuc]; x = np.arange(len(ad_l))
rm = [o["rmse"] for _, o in sonuc.values()]; tm = [o["maks_tork"] for _, o in sonuc.values()]
cs = [stil[k][0] for k in sonuc]
b1 = ax[1].bar(x - 0.2, rm, 0.4, color=cs, alpha=.9, label="RMSE [°]")
ax2 = ax[1].twinx(); b2 = ax2.bar(x + 0.2, tm, 0.4, color=cs, alpha=.35, hatch="//", label="maks tork [N·m]")
ax[1].bar_label(b1, fmt="%.2f", fontsize=8); ax2.bar_label(b2, fmt="%.1f", fontsize=8)
ax[1].set_xticks(x, ad_l, fontsize=8); ax[1].set_ylabel("RMSE [°] (dolu)"); ax2.set_ylabel("maks tork [N·m] (taralı)")
ax[1].set_title("Ölçütler: hata ↓ ama tork ↑")
for a in ax: a.grid(alpha=.3)
plt.tight_layout(); plt.savefig(KOK / "gorseller" / "o6_senaryo.png", dpi=120)
print("\nKayıt:", datetime.date.today(), "· CSV dosyaları veri/ klasöründe")
