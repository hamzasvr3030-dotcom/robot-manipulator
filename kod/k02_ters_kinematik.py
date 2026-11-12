"""Konu 2 — Ters kinematik: analitik ve sayısal çözüm karşılaştırması."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from robot_kol import (ters_kinematik_analitik, ters_kinematik_sayisal,
                       uc_poz, eklem_konumlari)

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
np.set_printoptions(precision=4, suppress=True)

hedef = np.array([0.35, 0.25, np.radians(-20)])  # x [m], y [m], phi [rad]
print(f"Hedef: x={hedef[0]} m, y={hedef[1]} m, phi={np.degrees(hedef[2]):.0f}°\n")

# --- Analitik: iki çözüm (dirsek aşağı / yukarı) ---
cozumler = {}
for dirsek, ad in [(+1, "dirsek aşağı"), (-1, "dirsek yukarı")]:
    q = ters_kinematik_analitik(*hedef, dirsek=dirsek)
    hata = np.linalg.norm(uc_poz(q)[:2] - hedef[:2])
    cozumler[ad] = q
    print(f"Analitik ({ad:13s}): q = {np.degrees(q)} °   konum hatası = {hata:.1e} m")

# --- Sayısal: sönümlü en küçük kareler ---
q0 = np.radians([10, 10, 10])
q_say, n_iter, gecmis = ters_kinematik_sayisal(hedef, q0)
print(f"\nSayısal (DLS, q0={np.degrees(q0)}°): q = {np.degrees(q_say)} °  "
      f"({n_iter} iterasyon, son hata {gecmis[-1]:.1e})")

# --- Erişilemeyen hedef ---
try:
    ters_kinematik_analitik(0.8, 0.0, 0.0)
except ValueError as e:
    print(f"\n(0.8, 0.0) hedefi: {e}")

# --- Çizim ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
renk = {"dirsek aşağı": "#4C72B0", "dirsek yukarı": "#DD8452"}
for ad, q in cozumler.items():
    p = eklem_konumlari(q)
    ax1.plot(p[:, 0], p[:, 1], "-o", lw=4, ms=8, color=renk[ad], mfc="white", mec="k", label=ad)
ax1.plot(*hedef[:2], "*", ms=18, color="#C44E52", label="hedef")
ax1.set_aspect("equal"); ax1.grid(alpha=0.3); ax1.legend()
ax1.set_title("Analitik IK — aynı hedefe iki çözüm"); ax1.set_xlabel("x [m]"); ax1.set_ylabel("y [m]")

ax2.semilogy(gecmis, "o-", color="#55A868")
ax2.set_title("Sayısal IK (DLS) — hata yakınsaması")
ax2.set_xlabel("iterasyon"); ax2.set_ylabel("|e|  (log ölçek)"); ax2.grid(alpha=0.3, which="both")
plt.tight_layout()
plt.savefig(CIKTI / "02_ters_kinematik.png", dpi=130)
