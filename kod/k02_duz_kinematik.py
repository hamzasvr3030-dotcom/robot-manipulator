"""Konu 2 — DH parametreleriyle düz kinematik hesabı."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from robot_kol import L, dh, dh_tablosu, duz_kinematik, eklem_konumlari

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
np.set_printoptions(precision=4, suppress=True)

q_derece = np.array([30.0, 45.0, -30.0])
q = np.radians(q_derece)

print("Eklem açıları [°]:", q_derece)
print("\nDH tablosu (a [m], alpha [rad], d [m], theta [rad]):")
for i, satir in enumerate(dh_tablosu(q), 1):
    print(f"  {i}: a={satir[0]:.2f}  alpha={satir[1]:.0f}  d={satir[2]:.0f}  theta={satir[3]:.4f}")

for i, satir in enumerate(dh_tablosu(q), 1):
    print(f"\n{i-1}_T_{i} =\n{dh(*satir)}")

T03 = duz_kinematik(q)[-1]
print(f"\n0_T_3 =\n{T03}")
x, y = T03[0, 3], T03[1, 3]
phi = np.degrees(np.arctan2(T03[1, 0], T03[0, 0]))
print(f"\nUç efektör konumu: x = {x:.4f} m, y = {y:.4f} m, phi = {phi:.1f}°")

# Elle kontrol: kapalı form formül
q1, q2, q3 = q
xk = L[0]*np.cos(q1) + L[1]*np.cos(q1+q2) + L[2]*np.cos(q1+q2+q3)
yk = L[0]*np.sin(q1) + L[1]*np.sin(q1+q2) + L[2]*np.sin(q1+q2+q3)
print(f"Kapalı form kontrol: x = {xk:.4f} m, y = {yk:.4f} m  (fark: {abs(x-xk)+abs(y-yk):.1e})")

# Çizim: kol ve her eklemin çerçevesi
p = eklem_konumlari(q)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(p[:, 0], p[:, 1], "-o", lw=4, ms=9, color="#4C72B0", mfc="white", mec="k")
for i, T in enumerate(duz_kinematik(q)):
    o = T[:2, 3]
    ax.arrow(*o, *(0.06 * T[:2, 0]), head_width=0.012, color="#C44E52")
    ax.arrow(*o, *(0.06 * T[:2, 1]), head_width=0.012, color="#55A868")
    ax.text(o[0] + 0.01, o[1] - 0.04, f"{{{i}}}", fontsize=10)
ax.set_title(f"q = ({q_derece[0]:.0f}°, {q_derece[1]:.0f}°, {q_derece[2]:.0f}°)  →  "
             f"uç = ({x:.3f}, {y:.3f}) m")
ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")
ax.text(0.02, 0.95, "kırmızı: x_i ekseni\nyeşil: y_i ekseni", transform=ax.transAxes, va="top", fontsize=8)
plt.tight_layout()
plt.savefig(CIKTI / "02_duz_kinematik.png", dpi=130)
