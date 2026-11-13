# O2 · Elektrik ve Güç Temelleri

> 📋 **Syllabus:** O2 · **Dönem:** P2 (16–20 Kasım) · **Tahmini süre:** 4 saat · **Kimler:** tüm ekip, öncelik Kişi 2 (elektronik ve güç) · **Çıktı:** Kendi projeniz için güç dağıtım şeması taslağı

> ⚠️ **Zorunlu modül:** O2 ve güvenlik modülü (Konu 10 / K7), **ilk elektrik testinden (07–13 Aralık) önce** tamamlanmalıdır. Bu sayfa İSG eğitiminin yerini tutmaz.

> ### 🎯 Kısaca
> Robotun her parçası elektrikle çalışır: motorlar, sürücüler, mikrodenetleyici, kamera. Bu sayfa üç soruyu yanıtlar:
> 1. **Ne kadar güç lazım?**
> 2. **Hangi kaynaktan?** Batarya mı, güç kaynağı mı?
> 3. **Güvenle nasıl dağıtılır?** Sigorta, kablo kesiti, regülatör ve acil durdurma.

> 🧠 **Benzetme — su tesisatı:**
> - **Gerilim (V)**, su basıncıdır.
> - **Akım (A)**, borudan geçen su miktarıdır.
> - **Direnç (Ω)**, borunun darlığıdır.
> - **Sigorta**, aşırı basınçta patlayan emniyet valfidir.
> - **İnce kablo**, dar borudur: Çok su geçirmeye çalışırsan ısınır.

## O2.1 Temel yasalar

```math
V = I \cdot R \qquad\qquad P = V \cdot I = I^2 R
```

| Bağlantı | Gerilim | Akım | Kullanım |
|---|---|---|---|
| **Seri** | Toplanır | Aynı | Batarya hücreleri (3S = 3 hücre seri) |
| **Paralel** | Aynı | Toplanır | Aynı hatta birden çok sürücü |

**Kayıp gücü:** Kablo ve bağlantılarda harcanan güç $I^2R$'dir. Akım iki katına çıkarsa kayıp **dört katına** çıkar. Bu yüzden yüksek güçte daha yüksek gerilim tercih edilir.

## O2.2 Bataryalar: LiPo

| Terim | Anlamı | Örnek |
|---|---|---|
| Hücre gerilimi | Nominal 3.7 V, dolu 4.2 V, **boş sayılan ~3.3–3.5 V** | — |
| "**S**" sayısı | Seri hücre sayısı | 3S: 11.1 V nominal, 4S: 14.8 V nominal |
| **Kapasite** (mAh) | Kaç saat ne kadar akım verebildiği | 2200 mAh = 2.2 A'i 1 saat boyunca |
| **C-oranı** | Sürekli verebileceği akımın kapasiteye oranı | 30C × 2.2 Ah = 66 A |

> ⚠️ LiPo hasarlıysa, şişmişse ya da aşırı boşalmışsa **yangın riski** taşır. Şarj ve depolama için İSG birimine danışın. Masaüstü bir robot kolda çoğu zaman bataryaya hiç gerek yoktur: **Şebekeden beslenen bir DC güç kaynağı** daha güvenli ve daha basittir.

## O2.3 Dağıtım elemanları

| Eleman | Görevi | Seçimde dikkat |
|---|---|---|
| **Sigorta** | Kısa devrede hattı keser, yangını önler | Hat akımının yaklaşık 1.25–1.5 katı. Motor hattında gecikmeli tip |
| **Kablo kesiti** | Akımı ısınmadan taşır | Kesit küçükse kablo ısınır ve gerilim düşer |
| **Gerilim düşümü** | $\Delta V = I \cdot R_{kablo}$, $R = \rho L / A$ | Uzun ve ince kabloda motor zayıflar |
| **Regülatör** (BEC, DC-DC) | Motor geriliminden mantık devresi için 5 V veya 3.3 V üretir | Anahtarlamalı (buck) tip verimlidir. Lineer tip ısınır |
| **Motor sürücü** | Mantık sinyaliyle (PWM/STEP) motora güç verir | Sürekli ve tepe akımı, gerilim aralığı |
| **Acil durdurma** | Motor gücünü **donanımla** keser | Röle veya kontaktörle güç hattını açmalıdır (Konu 10) |

**Gerilim düşümü örneği:** 2 m gidiş-dönüş, 0.5 mm² bakır kablo ve 5 A akım:

$R = 0.0172 \cdot 2 / 0.5 = 0.069\ \Omega$ ve $\Delta V = 5 \cdot 0.069 = 0.34$ V.

Bu kayıp 24 V'ta %1.4 eder ve kabul edilebilir. Aynı kayıp 5 V'luk bir mantık hattında %7'dir, ki bu da bir mikrodenetleyiciyi resetlemeye yeter.

## O2.4 Bu kol için güç bütçesi

Konu 5'teki mekanik güçlerden yola çıkılır. Bunlar eklemlerin aynı anda en hızlı hareket ettiği en kötü durumun değerleridir:

| Tüketici | Mekanik güç | Elektriksel güç (motor+sürücü verimi ≈ %70) |
|---|---|---|
| Eklem 1 | 33.8 W | ≈ 48 W |
| Eklem 2 | 14.6 W | ≈ 21 W |
| Eklem 3 | 3.1 W | ≈ 4 W |
| Tutucu servosu | — | ≈ 5 W |
| Mantık kartı (mikrodenetleyici veya tek kartlı bilgisayar) | — | ≈ 10–15 W |
| **Toplam** | | **≈ 90 W** |

**Öneri:**
- **24 V, en az 150 W'lık bir DC güç kaynağı.** Bu, yaklaşık 2 kat pay bırakır. 24 V'ta 90 W, yaklaşık 3.8 A eder.
- **Ana sigorta:** 8 A gecikmeli.
- **Sürücü başına sigorta:** 3–5 A.
- **Ana hat kablosu:** 1 mm² veya daha kalın.

> ℹ️ Bu sayılar örnek kol içindir. Gerçek kolun yükü, erişimi ve motorları **Proje Kartı'nda** belirlendikten sonra yeniden hesaplanmalıdır.

## O2.5 Güç dağıtım şeması taslağı (çıktı)

```text
 230 V AC ──► [24 V DC güç kaynağı, 150 W]
                    │
                [ANA SİGORTA 8 A]
                    │
                    ├──────────────────────────────┐
                    │                              │
        [E-STOP kontaktörü/rölesi] ◄── mantar     [DC-DC 24→5 V, 3 A]
           (NC, çift kanal)            buton            │
                    │                                   ├──► Mikrodenetleyici / SBC
         ┌──────────┼──────────┬──────────┐             ├──► Enkoderler, sensörler
       [3–5 A]    [3–5 A]    [3 A]      [2 A]           └──► (mantık hattı E-STOP'tan
         │          │          │          │                    etkilenmez: hata kaydı alınır)
     Sürücü 1   Sürücü 2   Sürücü 3   Tutucu servo
         │          │          │
      Motor 1    Motor 2    Motor 3 (+ fren)

 Tüm GND'ler tek noktada birleşir (yıldız topraklama). Güç ve sinyal kabloları ayrı demetlenir.
```

**Tasarım kararları ve gerekçeleri:**
- **E-STOP yalnızca motor gücünü keser**, mantık devresi çalışmaya devam eder. Böylece robotun neden durduğu kayda geçer ve kol yeniden başlatılmadan kendi kendine hareket etmez.
- **Güç ve mantık hatları ayrıdır.** Motorların çektiği akım darbeleri mikrodenetleyiciyi resetleyemez.
- **Her sürücünün kendi sigortası vardır.** Bir sürücü yanarsa diğerleri çalışmaya devam eder.

## ✍️ Kendini sına (syllabus soruları)

<details>
<summary><b>1.</b> 3S 2200 mAh 30C bir batarya en çok kaç amper sürekli akım verebilir?</summary>
<br>
I = kapasite × C = 2.2 Ah × 30 = <b>66 A</b>. Bu değer bataryanın sınırıdır. Kablo, konnektör ve sigortanın da bu akıma göre seçilmesi gerekir.
</details>
<details>
<summary><b>2.</b> 4S bataryanın nominal gerilimi nedir?</summary>
<br>
4 × 3.7 V = <b>14.8 V</b>. Tam doluyken 4 × 4.2 = 16.8 V olur.
</details>
<details>
<summary><b>3.</b> Aynı güç için gerilim artarsa akım nasıl değişir?</summary>
<br>
P = V·I sabitse akım <b>ters orantılı olarak azalır</b>. Gerilim iki katına çıkınca akım yarıya iner. Kablodaki kayıp I²R ile hesaplandığı için kayıp <b>dörtte birine</b> düşer. Ayrıca daha ince kablo kullanılabilir.
</details>

## ⚡ Akılda kalsın
- $V = IR$ ve $P = VI$. Kayıp akımın **karesiyle** büyür.
- LiPo: Hücre başına 3.7 V nominal, 4.2 V dolu. "S" seri hücre sayısıdır. Sürekli akım = kapasite × C.
- **Sigorta → acil durdurma → sürücüler** sırası kurulur. Güç ve mantık hatları ayrılır, GND'ler ortaktır.
- E-stop, motor gücünü **donanımla** kesmelidir.

## Kaynaklar
[9] Hughes & Drury · [24] IEC 60204-1 · [31] Horowitz & Hill. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← O1 · Matematik ve fizik](o1-matematik-fizik.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [O3 · Yazılım altyapısı →](o3-yazilim-altyapisi.md)
