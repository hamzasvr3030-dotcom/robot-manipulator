# 1 · Robot Manipülatör Temelleri

> **Çıktı türü:** Şema · **Kod:** [`kod/k01_sema.py`](../kod/k01_sema.py)

> 📋 **Syllabus:** K1 · Manipülatör temelleri · **Dönem:** P1 (12–15 Kasım) · **Tahmini süre:** 3 saat · **Öncelikli:** Kişi 1 (mekanik tasarım)  
> **Ön koşul:** [O1 · Matematik ve fizik](../ortak/o1-matematik-fizik.md) · **Ay sonu hedefi:** Seçilen kolu şemada anlatır · **Syllabus çıktısı:** Kolun şeması ve çalışma uzayı notu · [Proje planı](../plan.html)

> ### 🎯 Kısaca
> Robot kol, **senin kolun gibi** çalışır: omuz, dirsek ve bilek yerine **eklemler**, kemikler yerine **uzuvlar** vardır. Bu sayfada üç şey öğreneceksin:
> 1. Eklem çeşitleri: dönen ve kayan eklemler.
> 2. Serbestlik derecesi (DOF): kolun kaç bağımsız hareket yapabildiği.
> 3. Çalışma uzayı: kolun uzanabildiği bölge.

> 🧠 **Benzetme:** Dirseğini masaya dayayıp önündeki bir noktaya parmağınla dokun. Omzunu, dirseğini ve bileğini kullanıyorsun, yani 3 eklem. Bileğini sabit tutarsan aynı noktaya yine dokunabilirsin, ama artık elinin açısını seçemezsin. İşte **serbestlik derecesi** budur: Her eklem sana bir "seçim hakkı" daha verir.

## 1.1 Manipülatör nedir?

Robot manipülatör, birbirine **eklemlerle** bağlanmış katı **uzuvlardan** (link) oluşan açık kinematik zincirdir. Zincirin bir ucu sabit **tabana**, diğer ucu işi yapan **uç efektöre** (tutucu, kaynak torcu, vakum vb.) bağlıdır [1, Bölüm 1], [2, Bölüm 1].

## 1.2 Eklem tipleri

| Eklem | Sembol | Hareket | Serbestlik | Örnek |
|---|---|---|---|---|
| Döner (revolute) | R | Bir eksen etrafında dönme | 1 | Endüstriyel kolların neredeyse tüm eklemleri |
| Prizmatik (prismatic) | P | Bir eksen boyunca öteleme | 1 | Kartezyen (gantry) robotlar, SCARA'nın z ekseni |
| Silindirik | C | Dönme + öteleme (aynı eksen) | 2 | — |
| Küresel (spherical) | S | Üç eksende dönme | 3 | Bilek (3 R eklemle gerçeklenir) |

Pratikte robotlarda neredeyse yalnızca **R** ve **P** eklemleri kullanılır. Çok serbestlikli eklemler bu iki tipin art arda dizilmesiyle elde edilir [3, Bölüm 2].

## 1.3 Serbestlik derecesi (DOF)

Bir mekanizmanın serbestlik derecesi **Grübler–Kutzbach** formülüyle hesaplanır [3, Bölüm 2.2]:

```math
\text{DOF} = m\,(N - 1 - J) + \sum_{i=1}^{J} f_i
```

Burada $m$ düzlemde 3, uzayda 6'dır. $N$ tabanla birlikte uzuv sayısı, $J$ eklem sayısı, $f_i$ ise $i$. eklemin serbestliğidir.

Açık zincirli seri bir kolda bu formül sadeleşir: **DOF = eklem serbestliklerinin toplamı.**

- Uzayda bir cismi **istenen konum ve yönelime** getirmek için 6 DOF gerekir (3 konum + 3 yönelim).
- Düzlemde bunun için 3 DOF yeterlidir: $(x, y, \varphi)$.
- DOF sayısı görevin gerektirdiğinden fazlaysa kola **artık serbestlikli (redundant)** denir. Örnek: 7 eksenli kollar. Fazla serbestlik engellerden kaçınmak için kullanılır.

## 1.4 Yaygın kol yapıları

| Yapı | İlk 3 eklem | Çalışma uzayı | Tipik kullanım |
|---|---|---|---|
| Kartezyen (gantry) | PPP | Dikdörtgenler prizması | 3B yazıcı, CNC, paletleme |
| Silindirik | RPP | Silindir | Montaj, makine besleme |
| Küresel (polar) | RRP | Küre kabuğu | Eski tip kaynak robotları |
| SCARA | RRP | Silindir | Hızlı al-yerleştir, elektronik montaj |
| Eklemli (antropomorfik) | RRR | Küre benzeri | Endüstriyel 6 eksenli kollar |

## 1.5 Çalışma uzayı (workspace)

- **Ulaşılabilir çalışma uzayı:** Uç efektörün *en az bir* yönelimle ulaşabildiği noktaların kümesi.
- **Becerikli (dexterous) çalışma uzayı:** Uç efektörün *her* yönelimle ulaşabildiği noktaların kümesi. Ulaşılabilir uzayın bir alt kümesidir [1, Bölüm 4.3].

Uzuv boylarına ek olarak **eklem sınırları** da çalışma uzayını daraltır.

## 1.6 Bu depoda kullanılan kol

Tüm konularda aynı model kullanılıyor: **düşey düzlemde çalışan 3 eklemli düzlemsel RRR kol**. Yerçekimi $-y$ yönünde etki eder.

| Parametre | Değer |
|---|---|
| Uzuv boyları $L_1, L_2, L_3$ | 0.30 m, 0.25 m, 0.10 m |
| Eklem sınırları | $q_1 \in [-180°, 180°]$, $q_2, q_3 \in [-150°, 150°]$ |
| Uç efektör pozu | $(x, y, \varphi)$, $\varphi = q_1+q_2+q_3$ |
| Maksimum erişim | $L_1+L_2+L_3 = 0.65$ m |

![Kol şeması ve çalışma uzayı](../gorseller/01_kol_semasi.png)

**Sağdaki grafiğin yorumu:** Çalışma uzayı 0.65 m yarıçaplı bir disktir. Merkezde küçük bir boşluk kalıyor, çünkü $q_2$ ve $q_3$ ±150° ile sınırlı olduğu için kol kendi üzerine tamamen katlanamıyor. Eklem sınırları olmasaydı iç sınırın yarıçapı $\max(0,\; L_1 - L_2 - L_3) = 0$ olurdu ve boşluk oluşmazdı.

**Neden bu kol?** 3 DOF, düzlemde konum ve yönelimi tam belirlemeye yetiyor. Bu sayede ters kinematiğin analitik çözümü elle türetilebiliyor. Aynı kavramlar (DH, Jacobian, tekillik) 6 eksenli kollara doğrudan genellenebilir.

## ⚡ Akılda kalsın
- Robotlarda neredeyse yalnızca iki eklem tipi kullanılır: **dönen (R)** ve **kayan (P)**.
- Seri bir kolda **DOF = eklem sayısı**. Düzlemde her pozu alabilmek için 3, uzayda 6 DOF gerekir.
- **Çalışma uzayının** sınırlarını uzuv boyları ve eklem sınırları birlikte belirler.
- **Tekillik sezgisi:** Kol tamamen açıldığında (ya da tamamen katlandığında) bir yöne hareket edemez hâle gelir. Ayrıntısı Konu 2.5'te.

## ✍️ Kendini test et
<details>
<summary><b>Soru:</b> Kartezyen bir 3B yazıcının eklem yapısı nedir, kaç DOF'u vardır?</summary>
<br>
PPP: Üç kayan eklemi vardır, yani 3 DOF. Çalışma uzayı bir kutu şeklindedir.
</details>
<details>
<summary><b>Soru:</b> Bu depodaki kolun uzuvları 0.30 + 0.25 + 0.10 m. En uzak hangi mesafeye uzanabilir?</summary>
<br>
0.65 m. Kol tamamen düz açıldığında uzuv boyları toplanır.
</details>

## Kaynaklar
[1] Craig · [2] Spong vd. · [3] Lynch & Park. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [2 · Düz kinematik →](02-duz-kinematik.md)
