"""Konu 0 — Kol şeması ve çalışma uzayı çizimi."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from robot_kol import L, Q_MIN, Q_MAX, eklem_konumlari

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
CIKTI.mkdir(exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# --- Sol: kolun şeması ---
q = np.radians([35, 40, -45])
p = eklem_konumlari(q)
ax1.plot(p[:, 0], p[:, 1], "-", lw=6, color="#4C72B0", solid_capstyle="round")
ax1.plot(p[:3, 0], p[:3, 1], "o", ms=14, mfc="white", mec="black", mew=2)
ax1.plot(p[3, 0], p[3, 1], "s", ms=10, color="#C44E52")
ax1.fill([-0.06, 0.06, 0.06, -0.06], [-0.04, -0.04, 0, 0], color="0.4", hatch="///")
for i, ad in enumerate(["Eklem 1 (q1)", "Eklem 2 (q2)", "Eklem 3 (q3)"]):
    ax1.annotate(ad, p[i], xytext=(p[i, 0] - 0.13, p[i, 1] + 0.05), fontsize=9,
                 arrowprops=dict(arrowstyle="->", lw=0.8))
ax1.annotate("Uç efektör (x, y, φ)", p[3], xytext=(p[3, 0] - 0.05, p[3, 1] + 0.1),
             fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))
for i in range(3):
    m = (p[i] + p[i + 1]) / 2
    ax1.text(m[0] + 0.015, m[1] - 0.035, f"L{i+1} = {L[i]:.2f} m", fontsize=9, color="#4C72B0")
ax1.annotate("", (0.15, 0), (0, 0), arrowprops=dict(arrowstyle="->"))
ax1.annotate("", (0, 0.15), (0, 0), arrowprops=dict(arrowstyle="->"))
ax1.text(0.155, -0.015, "x0"); ax1.text(-0.03, 0.155, "y0")
ax1.annotate("g", (-0.15, 0.05), (-0.15, 0.17), arrowprops=dict(arrowstyle="->", color="gray"), color="gray")
ax1.set_title("3-DOF düzlemsel RRR kol (düşey düzlem)")
ax1.set_aspect("equal"); ax1.set_xlim(-0.25, 0.7); ax1.set_ylim(-0.1, 0.65)
ax1.grid(alpha=0.3); ax1.set_xlabel("x [m]"); ax1.set_ylabel("y [m]")

# --- Sağ: çalışma uzayı (Monte Carlo örnekleme) ---
rng = np.random.default_rng(0)
Q = rng.uniform(Q_MIN, Q_MAX, size=(30000, 3))
uc = np.array([eklem_konumlari(qi)[3] for qi in Q])
ax2.scatter(uc[:, 0], uc[:, 1], s=0.3, alpha=0.3, color="#55A868")
R = sum(L)
t = np.linspace(0, 2 * np.pi, 400)
ax2.plot(R * np.cos(t), R * np.sin(t), "k--", lw=1, label=f"Maks. erişim R = {R:.2f} m")
ax2.set_title("Ulaşılabilir çalışma uzayı (30 000 rastgele eklem açısı)")
ax2.set_aspect("equal"); ax2.grid(alpha=0.3); ax2.legend(loc="lower left", fontsize=8)
ax2.set_xlabel("x [m]"); ax2.set_ylabel("y [m]")

plt.tight_layout()
plt.savefig(CIKTI / "00_kol_semasi.png", dpi=130)
print("Kaydedildi:", CIKTI / "00_kol_semasi.png")
