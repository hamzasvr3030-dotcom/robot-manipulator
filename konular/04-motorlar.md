# 4 · Motorlar: Servo, Step, BLDC, Tork, Redüktör, Sürücü Seçimi

> **Çıktı türü:** Hesap sayfası · **Kod:** [`kod/k04_tork.py`](../kod/k04_tork.py) · **Tablo:** [`kod/tork_hesap_sayfasi.csv`](../kod/tork_hesap_sayfasi.csv) (Excel'de açılır)

## 4.1 Motor tipleri

| Tip | Çalışma ilkesi | Artı | Eksi | Robotta kullanım |
|---|---|---|---|---|
| **Fırçalı DC** | Komütasyon mekanik fırçayla yapılır | Ucuz, sürmesi kolay | Fırça aşınır, kıvılcım çıkarır | Eğitim robotları, küçük kollar |
| **Hobi servo** | DC motor + dişli + potansiyometre + kart tek kutuda | Tak-çalıştır, PWM ile konum komutu | Düşük hassasiyet, geri bildirim dışarıya verilmez | Masaüstü kollar |
| **Akıllı servo** (Dynamixel vb.) | Aynı yapı + manyetik enkoder + seri haberleşme | Konum, hız ve akım okunabilir | Pahalı, tork sınırlı | Araştırma kolları |
| **Step motor** | Sabit adımlarla döner, açık çevrimde konumlanır | Ucuz, enkodersiz konumlanır, düşük hızda torku yüksek | Hız arttıkça tork düşer, **adım kaçırabilir**, ısınır | 3B yazıcı, ucuz kollar |
| **BLDC / PMSM (AC servo)** | Elektronik komütasyon, sinüs (FOC) sürüş | Tork/hacim oranı yüksek, verimli, sessiz | Enkoder ve gelişmiş sürücü gerektirir | **Endüstriyel kollar**, kobotlar |

Kaynaklar: [9, Bölüm 3, 9, 10].

## 4.2 Redüktör seçimi

Motorlar düşük torkta yüksek devirle çalışır. Eklemler ise yüksek tork ve düşük devir ister. Redüktör bu ikisini eşleştirir. $N$ çevrim oranı ve $\eta$ verim olmak üzere:

```math
\tau_{eklem} = N\,\eta\,\tau_{motor}, \qquad \omega_{motor} = N\,\omega_{eklem}, \qquad
J_{yansıyan} = \frac{J_{yük}}{N^2}
```

Son formül önemlidir: Yükün ataleti motora **$N^2$ oranında küçülerek** yansır. Bu yüzden yüksek oranlı redüktör kullanıldığında kontrol kolaylaşır, ama arka sürülebilirlik (backdrivability) azalır.

| Redüktör | Tipik N | Boşluk (backlash) | Verim | Not |
|---|---|---|---|---|
| Düz/planet dişli | 3–100 | Orta | 0.85–0.95 | Ucuz, yaygın |
| **Harmonik (strain wave)** | 30–160 | **≈ 0** | 0.65–0.85 | Endüstriyel ve kobot bilekleri |
| Sikloidal (RV) | 30–200 | Çok düşük | 0.80–0.90 | Ağır yüklü taban eklemleri |
| Sonsuz vida | 10–100 | Orta | 0.4–0.7 | Kendiliğinden kilitlenir, verimi düşüktür |
| Kayış-kasnak | 1–5 | Düşük | 0.95+ | Motoru eklemden uzağa yerleştirmeye yarar |

## 4.3 Eklem torku hesabı

**En kötü durum**, kolun tamamen **yatay** uzandığı konumdur. Bu konumda yerçekimi kolları maksimumdur. Buna hızlanma sırasında oluşan dinamik tork da eklenir [2, Bölüm 7], [1, Bölüm 6]:

```math
\tau_{g,i} = g\sum_{k \,>\, i} m_k\,(x_k - x_i), \qquad
J_i = \sum_{k \,>\, i}\left(I_{c,k} + m_k (x_k - x_i)^2\right), \qquad
\tau_i = SF\,(\tau_{g,i} + J_i\,\alpha_i)
```

Toplamlar $i$. eklemin **dışında kalan** bütün kütleleri kapsar: uzuvlar, sonraki eklemlerin motorları ve yük. Uzuvlar ince çubuk kabul edilir: $I_c = mL^2/12$.

**Girdiler** (`k04_tork.py` dosyasının başından değiştirilebilir):

| | Uzuv 1 | Uzuv 2 | Uzuv 3 |
|---|---|---|---|
| Boy [m] | 0.30 | 0.25 | 0.10 |
| Uzuv kütlesi [kg] | 1.20 | 0.90 | 0.30 |
| Eklemdeki motor+redüktör [kg] | — (tabanda) | 0.40 | 0.25 |
| Hedef maks. ivme [°/s²] | 120 | 150 | 200 |
| Hedef maks. hız [°/s] | 90 | 120 | 180 |

Yük + tutucu kütlesi 0.50 kg, emniyet katsayısı $SF = 1.5$, redüktör verimi $\eta = 0.80$ alındı.

**Sonuçlar:**

| Eklem | Statik tork [N·m] | $J$ [kg·m²] | Dinamik tork [N·m] | **Toplam ×1.5 [N·m]** | N | **Motor torku [N·m]** | Motor devri [rpm] | Güç [W] |
|---|---|---|---|---|---|---|---|---|
| 1 | 13.00 | 0.634 | 1.33 | **21.49** | 50 | **0.537** | 750 | 33.8 |
| 2 | 4.32 | 0.123 | 0.32 | **6.96** | 50 | **0.174** | 1000 | 14.6 |
| 3 | 0.64 | 0.006 | 0.02 | **0.99** | 30 | **0.041** | 900 | 3.1 |

**Yorum ve seçim:**
- Statik (yerçekimi) tork, dinamik torktan **yaklaşık 10 kat büyük**. Yavaş çalışan kollarda boyutlandırmayı belirleyen yerçekimidir. Bu yüzden ağır motorları tabana yakın yerleştirmek veya **yay ya da karşı ağırlıkla dengeleme** yapmak büyük kazanç sağlar.
- **Eklem 1** için 21.5 N·m gerekiyor. N = 50 planet ya da harmonik redüktörle motorda 0.54 N·m ve 750 rpm yeterli. Bu değerler NEMA 23 sınıfı bir step motorun veya 100–200 W'lık bir AC servonun anma aralığında. Step motor seçilirse **750 rpm'deki** tork eğrisine bakılmalıdır. Step motorun torku hızla düştüğü için tutma torku (holding torque) tek başına yanıltıcıdır.
- **Eklem 2** için 7 N·m gerekiyor. N = 50 ile NEMA 17 step motor ya da küçük bir BLDC yetiyor.
- **Eklem 3** için 1 N·m gerekiyor. Bu değeri büyük bir hobi servo veya akıllı servo doğrudan karşılayabilir.

## 4.4 Sürücü seçimi

| Motor | Sürücü | Dikkat edilecek nokta |
|---|---|---|
| Fırçalı DC | H-köprüsü (PWM) | Akım sınırı ve akım ölçümü |
| Step | Mikro-adım sürücü (STEP/DIR) | Akım ayarı ve mikro-adım sayısı. Kapalı çevrim (enkoderli) step motor adım kaçırmayı önler |
| BLDC/PMSM | FOC sürücü (ODrive, VESC, endüstriyel servo sürücü) | Enkoder tipi, akım ve hız çevrimi ayarı |
| Servo | Kendi içinde | Besleme gerilimi ve haberleşme protokolü |

Gerilim, sürekli ve tepe akım değerleri motor etiketine göre seçilir. Frenleme sırasında motor sürücüye enerji geri basar. Bu nedenle **rejeneratif enerji** için fren direnci gerekip gerekmediği kontrol edilmelidir [9, Bölüm 4].

## Kaynaklar
[1] Craig · [2] Spong vd. · [9] Hughes & Drury. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)
