"""O1 — Matematik ve fizik minimumu: kendini sınama sorularının çözümü + gürültü örneği."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
np.set_printoptions(precision=4, suppress=True)

# --- Soru 1: 30° dönme matrisi ve (1, 0) noktasının döndürülmesi ---
a = np.radians(30)
R = np.array([[np.cos(a), -np.sin(a)],
              [np.sin(a),  np.cos(a)]])
p = np.array([1.0, 0.0])
print("Soru 1 — R(30°) =\n", R)
print("R · (1, 0) =", R @ p, " (uzunluk:", round(float(np.linalg.norm(R @ p)), 4), ")")

# --- Soru 2: yatay kolun ucundaki yükün statik torku ---
m, g, L = 0.5, 9.81, 0.3
print(f"\nSoru 2 — τ = m·g·L = {m}·{g}·{L} = {m * g * L:.4f} N·m")

# --- Soru 3: sensör okumasının ortalaması ve standart sapması ---
rng = np.random.default_rng(3)
gercek = 25.0                                   # gerçek mesafe [cm]
olcum = gercek + rng.normal(0.4, 0.8, 200)      # 0.4 cm sabit hata (bias) + 0.8 cm gürültü
print(f"\nSoru 3 — 200 ölçüm: ortalama = {olcum.mean():.2f} cm, std = {olcum.std(ddof=1):.2f} cm, "
      f"ortalamanın std'si = {olcum.std(ddof=1) / np.sqrt(len(olcum)):.3f} cm")

# --- Ek: atan2 ile atan farkı ---
for x, y in [(1, 1), (-1, 1), (-1, -1)]:
    print(f"(x={x:+d}, y={y:+d}):  atan(y/x) = {np.degrees(np.arctan(y / x)):7.1f}°   atan2(y, x) = {np.degrees(np.arctan2(y, x)):7.1f}°")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(olcum, ".", ms=4, color="#4C72B0", alpha=.7, label="ölçümler")
ax[0].axhline(gercek, color="#55A868", lw=2, label=f"gerçek değer ({gercek} cm)")
ax[0].axhline(olcum.mean(), color="#C44E52", lw=2, ls="--", label=f"ortalama ({olcum.mean():.2f} cm)")
ax[0].set_xlabel("ölçüm no"); ax[0].set_ylabel("mesafe [cm]"); ax[0].set_title("Gürültülü sensör okumaları"); ax[0].legend(fontsize=8)
ax[1].hist(olcum, bins=20, color="#4C72B0", alpha=.75)
ax[1].axvline(gercek, color="#55A868", lw=2); ax[1].axvline(olcum.mean(), color="#C44E52", lw=2, ls="--")
ax[1].axvspan(olcum.mean() - olcum.std(), olcum.mean() + olcum.std(), color="#C44E52", alpha=.12, label="±1 std")
ax[1].set_xlabel("mesafe [cm]"); ax[1].set_ylabel("adet"); ax[1].set_title("Dağılım: ortalama = merkez, std = genişlik"); ax[1].legend(fontsize=8)
for a_ in ax: a_.grid(alpha=.3)
plt.tight_layout(); plt.savefig(CIKTI / "o1_gurultu.png", dpi=120)
