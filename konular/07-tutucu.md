# 7 · Tutucu (Gripper) Tasarımı ve Temel Sensörler

> **Çıktı türü:** Not

> 📋 **Syllabus:** K6'nın tutucu kontrolü başlığı · **Dönem:** P4–P5 (7 Aralık – 10 Ocak) · **Tahmini süre:** K6 içinde · **Öncelikli:** Kişi 1 (tutucu tasarımı), Kişi 3 (tutucu kontrolü)  
> **Ön koşul:** Konu 5 · **Ay sonu hedefi:** Tutucu seçeneklerini not eder · **Syllabus çıktısı:** Tutucu seçenekleri notu · [Proje planı](../plan.html)

> ### 🎯 Kısaca
> Tutucu robotun **elidir**. Doğru tutucu seçimi nesneye bağlıdır:
> - Nesnenin şekline: kutu mu, yuvarlak mı?
> - Malzemesine: metal mi, karton mu?
> - Hassasiyetine: yumurta mı, cıvata mı?
>
> Bu sayfada tutucu tiplerini karşılaştırıyor, "**ne kadar sıkmalı?**" sorusunu hesaplıyor ve tutucunun kullandığı sensörlere bakıyoruz.

> 🧠 **Benzetme:**
> - **Paralel tutucu:** Bir şeyi iki parmakla sıkıştırmak.
> - **Vakum:** Camı vantuzla kaldırmak.
> - **Mıknatıs:** Buzdolabı magneti.
> - **Yumuşak tutucu:** Avucunla bir meyveyi sarmak.
>
> Elindeki ıslak bir şişeyi düşürmemek için daha sıkı tutarsın, çünkü sürtünme azalmıştır. Kavrama kuvveti formülü bu sezgiyi hesaba döker.

Tutucu, robotun dünyayla temas ettiği parçadır. Kol ne kadar iyi olursa olsun, tutucu yanlış seçilmişse sistem çalışmaz [12].

## 7.1 Tutucu seçenekleri

| Tip | Çalışma ilkesi | Artı | Eksi | Uygun nesne |
|---|---|---|---|---|
| **Paralel çeneli (2 parmak)** | Elektrik veya pnömatik ile çeneler paralel kayar | Basit, hassas, yaygın | Şekle uyum sağlamaz | Prizmatik parçalar, kutular |
| **Açısal çeneli** | Çeneler bir pim etrafında döner | Ucuz, kompakt | Kavrama noktası çapa göre değişir | Silindirik parçalar |
| **3 parmaklı merkezleyici** | Üç çene merkeze doğru kapanır | Kendiliğinden merkezler | Pahalı | Mil, boru, yuvarlak parça |
| **Vakum** | Vantuz ve vakum jeneratörü (venturi veya pompa) | Hızlı, düz yüzeyde çok etkili | Gözenekli veya kirli yüzeyde tutmaz | Sac, karton, cam, kutu |
| **Manyetik** | Elektromıknatıs veya kalıcı mıknatıs | Çok güçlü, basit | Yalnızca ferromanyetik malzemeyi tutar | Çelik sac, parça |
| **Yumuşak (soft) / Fin Ray** | Esnek parmaklar nesnenin şekline uyar | Kırılgan ve düzensiz nesneleri tutar | Taşıma kapasitesi düşük, konum belirsiz | Gıda, meyve, düzensiz nesneler |
| **Kavanoz (granular jamming)** | Tanecikli kese vakumla sertleşir | Neredeyse her şekli tutar | Yavaş, hacimli | Araştırma |

## 7.2 Kavrama kuvveti hesabı (sürtünmeyle kavrama)

$n$ temas yüzeyi, $\mu$ sürtünme katsayısı, $a$ hareket ivmesi ve $S$ emniyet katsayısı olmak üzere [12, Bölüm 2]:

```math
F_{kavrama} \;\ge\; \frac{m\,(g + a)}{\mu\,n}\; S
```

**Örnek:** Bu depodaki kol için alınan yük $m = 0.5$ kg (Konu 5). Değerler:
- İki çeneli tutucu, kauçuk çene ve çelik parça: $\mu \approx 0.5$, $n = 2$
- Hareket ivmesi $a = 3$ m/s², emniyet katsayısı $S = 2$

```math
F \ge \frac{0.5\,(9.81 + 3)}{0.5 \cdot 2}\cdot 2 \approx 12.8\ \text{N}
```

Vakumlu tutucularda kavrama kuvveti $F = \Delta p \cdot A \cdot \eta$ ile hesaplanır. Yatay kaldırmada vakum sürtünmeyle tutar, bu yüzden $\mu$ hesaba girer.

## 7.3 Bu kol için öneri

| Senaryo | Öneri |
|---|---|
| Eğitim/prototip, 0.5 kg küçük parça | **Servo motorlu paralel tutucu.** Konu 5'teki 3. eklem bütçesine (0.25 kg motor) sığar, ucuzdur ve kontrolü kolaydır |
| Düz kutu veya karton | **Vakum tutucu** (küçük pompa + 30–40 mm vantuz) |
| Meyve veya düzensiz nesne | **Fin Ray tipi yumuşak parmak** (3B yazıcıda TPU'dan basılabilir) |

> ⚠️ Tutucunun kütlesi, Konu 5'teki 0.5 kg'lık "yük + tutucu" bütçesinin içinde kalmalıdır. Kütle artarsa bütün eklem torkları yeniden hesaplanmalıdır.

## 7.4 Temel sensörler

| Sensör | Ne işe yarar? | Örnek |
|---|---|---|
| **Limit / mikro anahtar** | Çene açık veya kapalı mı? | Pnömatik tutucu konum algılama |
| **Endüktif / kapasitif yakınlık** | Parça yerinde mi? | Metal parça algılama |
| **Optik (IR) sensör** | Çeneler arasında nesne var mı? | Kızılötesi bariyer |
| **Kuvvet sensörü (FSR, yük hücresi)** | Ne kadar sıkıyorum? Kırılgan parçayı ezmemek için | Parmak ucuna FSR yerleştirme |
| **Motor akımı** | Kuvvet için dolaylı ölçüm ($\tau = K_t i$), ek sensör gerekmez | Akıllı servo ile kavrama kontrolü |
| **Vakum sensörü (basınç anahtarı)** | Vakum oluştu mu, parça tutuldu mu? | Vakum tutucu |
| **6 eksenli kuvvet/tork sensörü** | Bilekte $F_{x,y,z},\,M_{x,y,z}$ ölçer | Montaj, yüzey takibi, çarpışma algılama |
| **Dokunsal (tactile) dizi** | Temas dağılımını ve kaymayı algılar | Araştırma robotları |

## ⚡ Akılda kalsın
- **Paralel tutucu** varsayılan seçimdir. Düz yüzeyli nesneler için **vakum**, kırılgan veya düzensiz nesneler için **yumuşak** tutucu kullanılır.
- Sürtünmeyle kavrama kuvveti $F \ge m(g+a)S / (\mu n)$ ile hesaplanır. Sürtünme ($\mu$) azalırsa daha sıkı tutmak gerekir.
- Tutucunun kendi kütlesi kolun yük kapasitesinden **düşülür**.
- En basit "tuttum mu?" sensörü **motor akımıdır**: Tutucu nesneye dayandığında akım artar.

## ✍️ Kendini test et
<details>
<summary><b>Soru:</b> Sürtünme katsayısı 0.5'ten 0.25'e düşerse (yağlı parça) gereken kavrama kuvveti ne olur?</summary>
<br>
İki katına çıkar: 12.8 N yerine yaklaşık 25.6 N gerekir.
</details>
<details>
<summary><b>Soru:</b> Delikli bir metal ızgarayı hangi tutucuyla tutarsın?</summary>
<br>
Manyetik tutucuyla (malzeme çelikse) ya da paralel tutucuyla. Vakum işe yaramaz, çünkü delikler havayı kaçırır.
</details>

## Kaynaklar
[12] Monkman vd. · [4] Siciliano vd. (Bölüm 5, sensörler). Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← 6 · Kontrol](06-kontrol.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [8 · Yazılım →](08-yazilim.md)
