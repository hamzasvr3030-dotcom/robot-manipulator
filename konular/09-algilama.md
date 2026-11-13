# 9 · Algılama: Kamera, Nesne Konumu, Kamera–Robot Kalibrasyonu

> **Çıktı türü:** Çıktı · **Kod:** [`kod/k09_goruntu.py`](../kod/k09_goruntu.py)

> 📋 **Syllabus:** K6'nın el-göz kalibrasyonu başlığı (proje hedefine bağlı) · **Dönem:** P4–P5 (7 Aralık – 10 Ocak) · **Tahmini süre:** K6 içinde · **Öncelikli:** Kişi 5 (simülasyon, test, algılama)  
> **Ön koşul:** [O1 · Matematik ve fizik](../ortak/o1-matematik-fizik.md), [O5 · ROS 2](../ortak/o5-ros2.md) · **Ay sonu hedefi:** Temel görüntü işleme örneği yapar · **Syllabus çıktısı:** Temel görüntü işleme örneği · [Proje planı](../plan.html)

> ### 🎯 Kısaca
> Kamera bize "nesne görüntünün **455. pikselinde**" der. Robotun bilmesi gereken ise "nesne benden **0.53 m ileride**" bilgisidir. Bu sayfa pikseli metreye çevirmenin iki adımını anlatıyor:
> 1. **Kamera kalibrasyonu:** Kamera, piksel cinsinden gördüğünü metreye nasıl çevirir?
> 2. **El-göz kalibrasyonu:** Kamera robota göre nerede duruyor?

> 🧠 **Benzetme:** Bir haritada iki şehir arası 5 cm olabilir. Gerçek mesafeyi bulmak için haritanın **ölçeğini** bilmen gerekir. Kamera kalibrasyonu bu ölçeği bulur. Ayrıca haritanın **kuzeyi nereye baktığını** da bilmen gerekir: Bu da el-göz kalibrasyonudur. Bizim gözlerimiz ve ellerimiz bu koordinasyonu doğuştan yapar, robota ise öğretmek gerekir.

**Amaç:** Kamerada görülen bir nesnenin konumunu **robot tabanına göre** metre cinsinden bulmak ve kolu oraya göndermek. Bunun için iki dönüşüm gerekir:

```text
piksel (u,v) ──[iç parametreler K]──► kamera çerçevesi (X,Y,Z) ──[el-göz kalibrasyonu T_rc]──► robot tabanı
```

## 9.1 Kamera modeli: iğne deliği (pinhole)

Kameranın bir 3B noktayı görüntüye nasıl düşürdüğü şu modelle ifade edilir [20, Bölüm 6]:

```math
\lambda\begin{bmatrix}u\\v\\1\end{bmatrix} = K\begin{bmatrix}X\\Y\\Z\end{bmatrix},
\qquad
K = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix}
```

- **İç parametreler** ($K$ matrisi ve lens bozulma katsayıları), satranç tahtası desenli fotoğraflarla **Zhang yöntemiyle** bulunur [17]. OpenCV'de karşılığı `cv2.calibrateCamera` fonksiyonudur [19].
- **Tek kamerada derinlik kaybolur.** $Z$ (derinlik) bilinmiyorsa piksel yalnızca bir **ışın** tanımlar. $Z$ üç yoldan elde edilebilir:
  - Nesne bilinen bir masa düzleminde duruyordur.
  - Derinlik kamerası kullanılır (RealSense, ZED vb.).
  - Stereo kamera kullanılır.

## 9.2 Kamera–robot (el-göz) kalibrasyonu

| Yapı | Kamera nerede? | Bulunan dönüşüm |
|---|---|---|
| **Eye-to-hand** | Sabit, robotu dışarıdan görür | Kamera → robot tabanı ($T_{rc}$) |
| **Eye-in-hand** | Robotun ucunda | Kamera → uç efektör ($T_{ec}$) |

Robot farklı pozlara götürülür ve her pozda kalibrasyon deseni görüntülenir. Bu ölçümlerden $AX = XB$ denklemi kurulur ve bilinmeyen $X$ dönüşümü çözülür. Klasik çözüm **Tsai–Lenz** yöntemidir [18]. OpenCV'deki karşılığı `cv2.calibrateHandEye` fonksiyonudur [19].

## 9.3 Örnek: renkli nesneyi bul, robot koordinatına çevir

Örnekte ek kütüphane gerekmesin diye **sentetik bir görüntü** ve yalnızca numpy kullanıldı. Senaryo şöyle: Kamera masanın 0.80 m üzerinde, aşağı bakıyor (eye-to-hand). İç parametreler $f_x = f_y = 600$ px ve $c = (320, 240)$.

| Adım | Bu koddaki işlem | OpenCV karşılığı |
|---|---|---|
| 1. Görüntü al | Sentetik görüntü + gürültü | `cv2.VideoCapture` |
| 2. Renk eşikleme | `(R>140) & (G<100) & (B<100)` | `cv2.cvtColor(..., HSV)` + `cv2.inRange` |
| 3. Gürültü temizleme | Komşu sayısına göre filtreleme | `cv2.morphologyEx(OPEN)` |
| 4. Ağırlık merkezi | Maske piksellerinin ortalaması | `cv2.moments` |
| 5. Piksel → kamera | $[X,Y,Z]^T = Z\,K^{-1}[u,v,1]^T$ | `cv2.undistortPoints` + aynı formül |
| 6. Kamera → robot | $p_r = T_{rc}\,p_c$ | `calibrateHandEye` sonucu |

**Çıktı:**

```text
Bulunan nesne alanı: 2409 piksel
Merkez (piksel): u = 455.0, v = 170.0   (gerçek: 455.0, 170.0)
Kamera çerçevesinde: [ 0.18   -0.0933  0.8   ] m
Robot tabanına göre: x = 0.5300 m, y = 0.0933 m, z = 0.0000 m
```

![Görüntü işleme](../gorseller/09_goruntu_isleme.png)

**Elle doğrulama:**
- Kamera çerçevesinde: $X = (455 - 320)\cdot 0.8 / 600 = 0.180$ m ve $Y = (170 - 240)\cdot 0.8/600 = -0.0933$ m ✔
- Robot tabanına çevirme: Kamera tabanın 0.35 m önünde ve y ekseni ters yönde. Bu yüzden robot koordinatı $x = 0.35 + 0.18 = 0.53$ m, $y = +0.0933$ m ✔
- Sonuç olarak nesne 0.53 m uzakta. Bu nokta kolun 0.65 m'lik erişim alanı içinde, yani Konu 3'teki IK ile kol nesneye gönderilebilir.

**Bir sonraki adımlar:**
- **ArUco/AprilTag işaretçileri:** Nesnenin konumuna ek olarak yönelimini de verir.
- **Derin öğrenme tabanlı nesne tespiti** (örneğin YOLO): Nesnelerin renk yerine sınıfa göre bulunmasını sağlar.
- **ROS 2'de bu zincirin karşılıkları:** `image_pipeline` ve `tf2` [13].

## ⚡ Akılda kalsın
- Görüntüden nesneyi bulmak için eşikleme, ardından ağırlık merkezi hesabı yapılır. Bu adım işin **kolay** kısmıdır.
- Asıl önemli olan iki kalibrasyondur:
  - **İç parametreler ($K$):** Piksel → kamera çerçevesi.
  - **El-göz ($T_{rc}$):** Kamera çerçevesi → robot tabanı.
- Tek bir kamera **derinliği bilemez**. Derinlik masa düzleminden, bir derinlik kamerasından veya stereo kameradan gelir.
- OpenCV'de bu işlerin karşılıkları: `inRange` → `moments` → `calibrateCamera` → `calibrateHandEye`.

## ✍️ Kendini test et
<details>
<summary><b>Soru:</b> Nesne görüntünün tam ortasında (u = 320, v = 240) olsaydı, kamera çerçevesindeki X ve Y ne olurdu?</summary>
<br>
X = 0, Y = 0. Nesne tam kameranın altında, yani robot koordinatında (0.35, 0) m'de.
</details>
<details>
<summary><b>Soru:</b> Kamera 0.80 m yerine 1.60 m yükseğe taşınırsa aynı nesne görüntüde nasıl görünür?</summary>
<br>
Yarı boyutta görünür ve görüntü merkezine daha yakın durur. Formülde Z iki katına çıktığı için aynı piksel kayması iki kat metreye karşılık gelir.
</details>

## Kaynaklar
[5] Corke · [13] ROS 2 Dokümantasyonu · [17] Zhang · [18] Tsai & Lenz · [19] OpenCV · [20] Hartley & Zisserman. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← 8 · Yazılım](08-yazilim.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [10 · Güvenlik →](10-guvenlik.md)
