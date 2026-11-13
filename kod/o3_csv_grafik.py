"""
O3 — Bir CSV dosyasını okuyup grafik çizen betik (kendini sınama alıştırması).

Kullanım:
    python o3_csv_grafik.py                         # varsayılan: veri/senaryo_A_ideal.csv
    python o3_csv_grafik.py ../veri/senaryo_B_gercekci.csv
CSV biçimi: ilk satır '#' ile başlayan açıklama, ikinci satır sütun adları.
"""
import csv
import sys
from pathlib import Path
import matplotlib.pyplot as plt

KOK = Path(__file__).resolve().parent.parent
yol = Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "senaryo_A_ideal.csv"

with open(yol, encoding="utf-8") as f:
    okuyucu = csv.reader(f)
    aciklama = next(okuyucu)                 # 1. satır: açıklama
    basliklar = next(okuyucu)                # 2. satır: sütun adları
    sutunlar = {b: [] for b in basliklar}
    for satir in okuyucu:
        for b, v in zip(basliklar, satir):
            sutunlar[b].append(float(v))

t = sutunlar["t_s"]
print("Dosya:", yol.name, "|", " · ".join(aciklama))
print(f"{len(t)} satır, {t[-1]:.2f} s kayıt, sütunlar: {', '.join(basliklar)}")
hata = [r - q for r, q in zip(sutunlar["referans_deg"], sutunlar["gercek_deg"])]
print(f"maks |hata| = {max(map(abs, hata)):.3f}°")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, sutunlar["referans_deg"], "k--", label="referans")
ax.plot(t, sutunlar["gercek_deg"], label="gerçek açı")
ax.set_xlabel("t [s]"); ax.set_ylabel("açı [°]"); ax.set_title(yol.name); ax.grid(alpha=.3); ax.legend()
plt.tight_layout()
cikti = KOK / "gorseller" / "o3_csv_grafik.png"
plt.savefig(cikti, dpi=110)
print("Grafik:", cikti)
