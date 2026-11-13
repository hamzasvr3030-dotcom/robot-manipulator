"""O4 — P, PI ve PID karşılaştırması (basamak yanıtı) ve yanıt ölçütlerinin okunması."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from eklem_sim import PID, Model, simule, olcutler

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
HEDEF = 10.0                     # küçük basamak: motor tork sınırına (12 N·m) dayanmasın
model = Model()
setler = {"P   (Kp=60)": PID(60, 0, 0), "PI  (Kp=60, Ki=50)": PID(60, 50, 0), "PID (Kp=60, Ki=150, Kd=4)": PID(60, 150, 4)}
renk = ["#C44E52", "#DD8452", "#4C72B0"]

fig, ax = plt.subplots(1, 2, figsize=(13, 4.8), gridspec_kw={"width_ratios": [1.6, 1]})
print(f"{'':28s} {'yükselme':>9s} {'aşım':>7s} {'yerleşme':>9s} {'kalıcı hata':>12s} {'maks tork':>10s}")
for (ad, k), c in zip(setler.items(), renk):
    s = simule(k, model, hedef=HEDEF, tip="basamak", T=8)
    o = olcutler(s, HEDEF)
    yer = "yerleşmedi" if np.isnan(o["yerlesme"]) else f"{o['yerlesme']:.2f} s"
    print(f"{ad:28s} {o['yukselme']:8.3f}s {o['asim']:6.1f}% {yer:>9s} {o['kalici']:+11.3f}° {o['maks_tork']:9.2f}")
    ax[0].plot(s["t"], s["q"], color=c, lw=2, label=ad)
ax[0].axhline(HEDEF, color="k", ls="--", lw=1, label=f"hedef ({HEDEF:.0f}°)")
ax[0].axhspan(HEDEF * 0.98, HEDEF * 1.02, color="0.5", alpha=.15, label="±%2 bandı")
ax[0].set_xlabel("t [s]"); ax[0].set_ylabel("eklem açısı [°]"); ax[0].set_title("Basamak yanıtı: P, PI, PID")
ax[0].legend(fontsize=8, loc="lower right"); ax[0].grid(alpha=.3); ax[0].set_xlim(0, 8)

# Sağ: ölçütlerin bir grafikte nasıl okunduğu (PID eğrisi üzerinde)
s = simule(setler["PID (Kp=60, Ki=150, Kd=4)"], model, hedef=HEDEF, tip="basamak", T=8)
o = olcutler(s, HEDEF)
ax[1].plot(s["t"], s["q"], color="#4C72B0", lw=2)
ax[1].axhline(HEDEF, color="k", ls="--", lw=1)
i_max = int(np.argmax(s["q"]))
ax[1].annotate(f"aşım = %{o['asim']:.1f}", (s["t"][i_max], s["q"][i_max]), xytext=(0.75, HEDEF * 0.8),
               arrowprops=dict(arrowstyle="->"), fontsize=9)
t10 = s["t"][np.argmax(s["q"] >= 0.1 * HEDEF)]; t90 = s["t"][np.argmax(s["q"] >= 0.9 * HEDEF)]
ax[1].axvspan(t10, t90, color="#55A868", alpha=.2)
ax[1].text(t90 + 0.06, HEDEF * 0.25, f"yükselme\n%10→%90\n{t90 - t10:.3f} s", fontsize=8, color="#2f7a46")
if not np.isnan(o["yerlesme"]):
    ax[1].axvline(o["yerlesme"], color="#8172B3", ls=":")
    ax[1].text(o["yerlesme"] + 0.03, HEDEF * 0.7, f"yerleşme\n(±%2)\n{o['yerlesme']:.2f} s", fontsize=8, color="#8172B3")
ax[1].set_xlim(0, 1.6); ax[1].set_xlabel("t [s]"); ax[1].set_title("Ölçütler grafikten nasıl okunur?"); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.savefig(CIKTI / "o4_p_pi_pid.png", dpi=120)
