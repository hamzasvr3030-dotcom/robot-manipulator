"""
Konu 4 — Eklem torku hesabı ve motor/redüktör boyutlandırma.

En kötü durum: kol tamamen yatay uzanmış (yerçekimi momenti maksimum)
+ hedef açısal ivmede hızlanırken.
Sonuç tablo olarak hem ekrana hem CSV'ye (Excel'de açılır) yazılır.
"""
from pathlib import Path
import csv
import numpy as np
from robot_kol import L

KOK = Path(__file__).resolve().parent.parent
g = 9.81

# ---------------- Girdiler (kendi kolunuza göre değiştirin) ----------------
m_uzuv = [1.20, 0.90, 0.30]   # uzuv kütleleri [kg] (kütle merkezi uzuv ortasında)
m_motor = [0.0, 0.40, 0.25]   # eklem i'deki motor+redüktör kütlesi [kg] (eklem 1 tabanda)
m_yuk = 0.50                  # taşınacak yük + tutucu [kg]
alfa_maks = np.radians([120, 150, 200])  # hedef maks. açısal ivme [rad/s²]
omega_maks = np.radians([90, 120, 180])  # hedef maks. açısal hız [rad/s]
emniyet = 1.5                 # emniyet katsayısı
verim = 0.80                  # redüktör verimi (planet ~0.9, sonsuz vida ~0.5)
redukter = [50, 50, 30]       # seçilen çevrim oranları N
# ---------------------------------------------------------------------------

# Kol yatay: her kütlenin tabana göre x konumu
x_eklem = np.cumsum([0.0, *L])            # eklem 1, 2, 3 ve uç
kutleler = []                             # (kütle, x_konum, kendi_atalet_merkez)
for i in range(3):
    kutleler.append((m_uzuv[i], x_eklem[i] + L[i] / 2, m_uzuv[i] * L[i] ** 2 / 12))
    if m_motor[i] > 0:
        kutleler.append((m_motor[i], x_eklem[i], 0.0))
kutleler.append((m_yuk, x_eklem[3], 0.0))

satirlar = []
for i in range(3):
    xi = x_eklem[i]
    disari = [(m, x, Ic) for (m, x, Ic) in kutleler if x > xi + 1e-9]
    tau_g = g * sum(m * (x - xi) for m, x, _ in disari)            # statik [N·m]
    J = sum(Ic + m * (x - xi) ** 2 for m, x, Ic in disari)         # eklem eksenine göre atalet
    tau_a = J * alfa_maks[i]                                       # dinamik [N·m]
    tau_top = (tau_g + tau_a) * emniyet
    N = redukter[i]
    tau_motor = tau_top / (N * verim)
    rpm_motor = omega_maks[i] * N * 60 / (2 * np.pi)
    guc = tau_top * omega_maks[i]
    satirlar.append({
        "Eklem": i + 1,
        "Statik tork [N·m]": tau_g,
        "Atalet J [kg·m²]": J,
        "Dinamik tork [N·m]": tau_a,
        f"Toplam ×{emniyet} [N·m]": tau_top,
        "Redüktör N": N,
        "Motor torku [N·m]": tau_motor,
        "Motor devri [rpm]": rpm_motor,
        "Mekanik güç [W]": guc,
    })

basliklar = list(satirlar[0].keys())
print(" | ".join(basliklar))
for s in satirlar:
    print(" | ".join(f"{v:.3f}" if isinstance(v, float) else str(v) for v in s.values()))

with open(KOK / "kod" / "tork_hesap_sayfasi.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["GİRDİLER"])
    w.writerow(["Uzuv boyları [m]", *L])
    w.writerow(["Uzuv kütleleri [kg]", *m_uzuv])
    w.writerow(["Motor kütleleri [kg]", *m_motor])
    w.writerow(["Yük [kg]", m_yuk])
    w.writerow(["Maks. ivme [rad/s²]", *np.round(alfa_maks, 3)])
    w.writerow(["Maks. hız [rad/s]", *np.round(omega_maks, 3)])
    w.writerow(["Emniyet katsayısı", emniyet]); w.writerow(["Redüktör verimi", verim])
    w.writerow([])
    w.writerow(["SONUÇLAR"])
    w.writerow(basliklar)
    for s in satirlar:
        w.writerow([f"{v:.3f}".replace(".", ",") if isinstance(v, float) else v for v in s.values()])
print("\nKaydedildi:", KOK / "kod" / "tork_hesap_sayfasi.csv")
