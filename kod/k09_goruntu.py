"""
Konu 9 — Temel görüntü işleme: renkli nesneyi bul, robot koordinatına çevir.

Bağımlılık olmasın diye sentetik görüntü ve yalnızca numpy kullanılır.
Gerçek kamerada aynı adımlar OpenCV ile yapılır (cv2.inRange, cv2.moments,
cv2.calibrateCamera, cv2.calibrateHandEye) — bkz. konular/09-algilama.md

Senaryo: Kamera masanın 0.80 m üzerinde, aşağı bakıyor (eye-to-hand).
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"
rng = np.random.default_rng(1)

# --- Kamera iç parametreleri (kalibrasyondan gelir) ---
fx = fy = 600.0
cx, cy = 320.0, 240.0
K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
Z = 0.80  # kamera–masa mesafesi [m]

# --- Kamera -> robot taban dönüşümü (el-göz kalibrasyonundan gelir) ---
# Kamera tabanın 0.35 m önünde; kamera x ekseni robot x'i ile aynı,
# kamera y ekseni robot -y yönünde (aşağı bakan kamera), z aşağı.
R_rc = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]], dtype=float)
t_rc = np.array([0.35, 0.0, 0.80])
T_rc = np.eye(4); T_rc[:3, :3] = R_rc; T_rc[:3, 3] = t_rc

# --- 1) Sentetik görüntü üret: gri masa + kırmızı disk + mavi kare + gürültü ---
H, W = 480, 640
img = np.full((H, W, 3), 170, dtype=float)
v, u = np.mgrid[0:H, 0:W]
gercek_u, gercek_v = 455.0, 170.0
img[(u - gercek_u) ** 2 + (v - gercek_v) ** 2 < 28 ** 2] = [200, 30, 35]
img[(abs(u - 150) < 30) & (abs(v - 330) < 30)] = [40, 60, 190]
img = np.clip(img + rng.normal(0, 12, img.shape), 0, 255).astype(np.uint8)

# --- 2) Renk eşikleme (kırmızı maske) ---
r, g, b = (img[..., i].astype(int) for i in range(3))
maske = (r > 140) & (g < 100) & (b < 100)

# --- 3) Gürültü temizleme: komşu sayısı az olan pikselleri at (basit açma) ---
komsu = sum(np.roll(np.roll(maske, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1))
maske = maske & (komsu >= 6)

# --- 4) Ağırlık merkezi (görüntü momentleri) ---
alan = maske.sum()
u_c, v_c = u[maske].mean(), v[maske].mean()

# --- 5) Piksel -> kamera koordinatı (iğne deliği modeli, Z biliniyor) ---
p_kamera = Z * np.linalg.inv(K) @ np.array([u_c, v_c, 1.0])
# --- 6) Kamera -> robot taban ---
p_robot = (T_rc @ np.append(p_kamera, 1.0))[:3]

print(f"Bulunan nesne alanı: {alan} piksel")
print(f"Merkez (piksel): u = {u_c:.1f}, v = {v_c:.1f}   (gerçek: {gercek_u}, {gercek_v})")
print(f"Kamera çerçevesinde: {p_kamera.round(4)} m")
print(f"Robot tabanına göre: x = {p_robot[0]:.4f} m, y = {p_robot[1]:.4f} m, z = {p_robot[2]:.4f} m")

fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
ax[0].imshow(img); ax[0].set_title("1) Kamera görüntüsü (sentetik)")
ax[1].imshow(maske, cmap="gray"); ax[1].set_title("2–3) Kırmızı maske + temizleme")
ax[2].imshow(img); ax[2].plot(u_c, v_c, "y+", ms=25, mew=3)
ax[2].set_title(f"4–6) Merkez → robot: ({p_robot[0]:.3f}, {p_robot[1]:.3f}) m")
for a in ax: a.set_xlabel("u [px]"); a.set_ylabel("v [px]")
plt.tight_layout()
plt.savefig(CIKTI / "09_goruntu_isleme.png", dpi=110)
