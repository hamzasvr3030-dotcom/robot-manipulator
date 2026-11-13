"""Konu 4 — Eklem uzayı ve kartezyen yörünge planlama karşılaştırması."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from robot_kol import ters_kinematik_analitik, eklem_konumlari, wrap

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"

T = 2.0                                  # hareket süresi [s]
t = np.linspace(0, T, 201)


def quintic(s0, s1, t, T):
    """5. derece polinom: başta/sonda hız ve ivme sıfır."""
    tau = t / T
    s = 10 * tau**3 - 15 * tau**4 + 6 * tau**5
    sd = (30 * tau**2 - 60 * tau**3 + 30 * tau**4) / T
    sdd = (60 * tau - 180 * tau**2 + 120 * tau**3) / T**2
    return s0 + (s1 - s0) * s, (s1 - s0) * sd, (s1 - s0) * sdd


def cubic(s0, s1, t, T):
    """3. derece polinom: başta/sonda hız sıfır (ivme sıçrar)."""
    tau = t / T
    s = 3 * tau**2 - 2 * tau**3
    sd = (6 * tau - 6 * tau**2) / T
    sdd = (6 - 12 * tau) / T**2
    return s0 + (s1 - s0) * s, (s1 - s0) * sd, (s1 - s0) * sdd


A = np.array([0.45, 0.05, np.radians(0)])     # başlangıç pozu
B = np.array([0.15, 0.40, np.radians(60)])    # bitiş pozu
qA = ters_kinematik_analitik(*A)
qB = ters_kinematik_analitik(*B)

# 1) Eklem uzayı: her eklem quintic ile doğrudan qA -> qB
qJ, qdJ, qddJ = zip(*[quintic(qA[i], qB[i], t, T) for i in range(3)])
qJ, qdJ, qddJ = map(np.array, (qJ, qdJ, qddJ))
_, _, qdd_cubic = zip(*[cubic(qA[i], qB[i], t, T) for i in range(3)])
uc_J = np.array([eklem_konumlari(qJ[:, k])[3] for k in range(len(t))])

# 2) Kartezyen uzay: uç düz çizgide, her adımda IK
s, _, _ = quintic(0.0, 1.0, t, T)
pozlar = A[None, :] + s[:, None] * (B - A)[None, :]
qC = np.array([ters_kinematik_analitik(*p) for p in pozlar]).T
uc_C = pozlar[:, :2]

print(f"qA = {np.degrees(qA).round(1)}°,  qB = {np.degrees(qB).round(1)}°")
yol_J = np.sum(np.linalg.norm(np.diff(uc_J, axis=0), axis=1))
yol_C = np.sum(np.linalg.norm(np.diff(uc_C, axis=0), axis=1))
print(f"Uç efektör yol uzunluğu: eklem uzayı = {yol_J:.3f} m, kartezyen = {yol_C:.3f} m")
print(f"Maks. eklem hızı (eklem uzayı, quintic) = {np.degrees(np.abs(qdJ).max()):.1f} °/s")
print(f"Maks. eklem ivmesi: quintic = {np.degrees(np.abs(qddJ).max()):.1f} °/s², "
      f"cubic = {np.degrees(np.abs(np.array(qdd_cubic)).max()):.1f} °/s²")

fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(2, 2, (1, 3))
for k in range(0, len(t), 25):
    p = eklem_konumlari(qJ[:, k]); ax.plot(p[:, 0], p[:, 1], "-", color="#4C72B0", alpha=0.25)
    p = eklem_konumlari(qC[:, k]); ax.plot(p[:, 0], p[:, 1], "-", color="#DD8452", alpha=0.25)
ax.plot(uc_J[:, 0], uc_J[:, 1], lw=2.5, color="#4C72B0", label="eklem uzayı (uç eğri çizer)")
ax.plot(uc_C[:, 0], uc_C[:, 1], lw=2.5, color="#DD8452", label="kartezyen (uç düz çizgi)")
ax.plot(*A[:2], "go", ms=10, label="A"); ax.plot(*B[:2], "rs", ms=10, label="B")
ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(fontsize=9)
ax.set_title("Uç efektör yolu"); ax.set_xlabel("x [m]"); ax.set_ylabel("y [m]")

ax = fig.add_subplot(2, 2, 2)
for i, c in enumerate(["#4C72B0", "#DD8452", "#55A868"]):
    ax.plot(t, np.degrees(qJ[i]), color=c, label=f"q{i+1} eklem uzayı")
    ax.plot(t, np.degrees(qC[i]), "--", color=c, label=f"q{i+1} kartezyen")
ax.set_title("Eklem açıları"); ax.set_ylabel("[°]"); ax.grid(alpha=0.3); ax.legend(fontsize=7, ncol=2)

ax = fig.add_subplot(2, 2, 4)
ax.plot(t, np.degrees(qddJ[0]), label="q1 ivmesi — quintic", color="#4C72B0")
ax.plot(t, np.degrees(qdd_cubic[0]), "--", label="q1 ivmesi — cubic", color="#C44E52")
ax.set_title("Quintic vs cubic: ivme sürekliliği"); ax.set_xlabel("t [s]"); ax.set_ylabel("[°/s²]")
ax.grid(alpha=0.3); ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(CIKTI / "04_yorunge.png", dpi=130)
