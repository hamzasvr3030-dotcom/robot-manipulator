# 🔌 Kişi 2 · Elektronik ve Güç

> 📋 **Rol:** Elektronik ve güç (Kişi 2) · **Sorumluluk:** Motor sürücüler, güç dağıtımı, sensör bağlantıları, acil durdurma · **Ana çıktı:** Güç şeması · **Sorumlusu olduğum modül:** O2 · **Ortak sorumlu olduğum modüller:** K4 (Kişi 1 ile), K7 (Kişi 5 ile) · [Proje planı](plan.html)

> ### 🎯 Kısaca
> Ortak dersler (O1–O7) herkes için aynı. Bu sayfa yalnızca **elektronik ve güç** alanına odaklanır:
> 1. Öncelik sırası ve ekiple bilgi alışverişi
> 2. Elektrik ihtiyacı ve **malzeme listesi** (son gün 20 Kasım)
> 3. Sürücü seçimi, **acil durdurma devresi**, sensör bağlantıları ve kablolama
> 4. T2 ve T7 **test prosedürleri**
> 5. Hafta hafta **iş listesi**
>
> Sayfadaki kutucuklar tıklanabilir. İşaretler bu tarayıcıda saklanır.

> ⚠️ **En acil iş: 20 Kasım.** Malzeme listesi, siparişler ve onaylar 20 Kasım'da kapanmalıdır. 21–29 Kasım ara sınav dönemidir ve malzeme 1 Aralık'ta teslim edilir. Elektrik kalemleri bu tarihe yetişmezse bütün takvim kayar. Liste için **Bölüm 3**'e bakın.

## 1. Öncelik sırası

| Öncelik | Modül / konu | Neden önemli? | Dönem |
|---|---|---|---|
| 🔴 Sorumlusuyum | [O2 · Elektrik ve güç temelleri](ortak/o2-elektrik-guc.md) | Syllabus'ta öncelikli kişi Kişi 2. Güç şeması bu modülün çıktısı | P2 (16–20 Kas) |
| 🔴 Ortak sorumlu | [10 · Güvenlik](konular/10-guvenlik.md) (K7, zorunlu) | Acil durdurma devresi Kişi 2'nin işi, Kişi 5 ile birlikte. Elektrik testinden (07–13 Ara) önce bitmeli | P3 (30 Kas – 6 Ara) |
| 🟠 Ortak sorumlu | [5 · Motorlar, tork ve redüktör](konular/05-motorlar.md) (K4) | Kişi 1 torku hesaplar, Kişi 2 motorun ve sürücünün akım/gerilim ihtiyacını çıkarır | P2 |
| 🟡 Destek | [6 · Kontrol](konular/06-kontrol.md) (K5): 6.1 kaskad döngü, 6.2 sensörler | Enkoder ve sürücü bağlantıları Kişi 2'de, kontrol yazılımı Kişi 3'te | P3–P4 |
| 🟡 Destek | [7 · Tutucu](konular/07-tutucu.md): 7.4 sensörler | Tutucu servosunun beslemesi ve sensör kabloları | P4–P5 |
| ⚪ Herkes gibi | O1, O3, O4, O5, O6, O7 | Ortak dersler | Plana göre |

**Kiminle hangi bilgi paylaşılır?**

| Kişi | Ondan alınan | Ona verilen |
|---|---|---|
| Kişi 1 (mekanik) | Eklem torkları, motor kütleleri, kablo güzergâhı için gövde çizimi | Motor/sürücü boyutları ve kütleleri, konnektör yerleri |
| Kişi 3 (gömülü yazılım) | Kullanılacak kart ve pinler, haberleşme tipi | Pin listesi, sinyal seviyeleri (5 V / 3.3 V), e-stop durum sinyali |
| Kişi 5 (test, güvenlik) | Güvenlik kontrol listesi, test planı biçimi | E-stop devresi, güç kesme ve fren davranışı, test kayıtları |

## 2. Örnek koldan çıkan elektrik ihtiyacı

[Konu 5](konular/05-motorlar.md) ve [O2](ortak/o2-elektrik-guc.md) hesaplarının özeti. Gerçek kolun yükü ve motorları Proje Kartı'nda belirlenince bu tablo yeniden hesaplanmalıdır.

| Eklem | Tasarım torku | Motor torku (N = 50/30, η = 0.8) | Motor devri | Mekanik güç | Elektriksel güç (≈%70 verim) |
|---|---|---|---|---|---|
| 1 | 21.5 N·m | 0.54 N·m | 750 rpm | 33.8 W | ≈ 48 W |
| 2 | 7.0 N·m | 0.17 N·m | 1000 rpm | 14.6 W | ≈ 21 W |
| 3 | 1.0 N·m | 0.04 N·m | 900 rpm | 3.1 W | ≈ 4 W |
| Tutucu + mantık kartı | — | — | — | — | ≈ 15–20 W |
| **Toplam** | | | | | **≈ 90 W → 24 V'ta ≈ 3.8 A** |

**Sonuç:** 24 V, en az 150 W'lık bir DC güç kaynağı (yaklaşık 2 kat pay), 8 A gecikmeli ana sigorta ve sürücü başına 3–5 A sigorta.

## 3. Elektrik malzeme listesi taslağı (20 Kasım'a kadar)

> ℹ️ Değerler örnek kola göredir. Motor tipi (step, BLDC veya servo) Kişi 1 ile kesinleşince sürücü satırları güncellenir. Fiyat ve tedarikçi Çalışma Tablosu'nun "Satın Alma" sayfasına işlenir. Onay sınırları için proje dosyasına bakın. Dosyadaki öneri, bütçenin %15–20'sinin yedek parça payı olarak ayrılmasıdır.

| # | Kalem | Adet | Seçim kriteri | Örnek kol için değer |
|---|---|---|---|---|
| 1 | DC güç kaynağı (kapalı kasa, sertifikalı) | 1 | Toplam güç × 1.5–2, kısa devre korumalı | 24 V, ≥ 150 W |
| 2 | Ana sigorta + sigorta yuvası | 1 + yedek | Toplam akım × 1.25–1.5, gecikmeli | 8 A |
| 3 | Sürücü sigortaları + yuvaları | 3–4 + yedek | Sürücünün sürekli akımına göre | 3–5 A |
| 4 | Acil durdurma butonu (mantar, mandallı) | 1–2 | **2 adet NC kontak** (çift kanal), sarı zemin | — |
| 5 | Güvenlik rölesi **veya** kontaktör | 1 | Bobin 24 V DC, kontak akımı ≥ motor hattı akımı, Stop 1 için gecikmeli çıkış | ≥ 10 A kontak |
| 6 | Reset / başlat butonu | 1 | NO kontak | — |
| 7 | Motor sürücüleri | 3 (+1 yedek) | 24 V'u kapsayan gerilim aralığı, sürekli akım ≥ motor anma akımı, ayarlı akım limiti, **enable girişi** | Motor tipine göre |
| 8 | DC-DC dönüştürücü (buck) | 1 | 24 → 5 V, ≥ 3 A (tek kartlı bilgisayar varsa 5 A) | 5 V / 3 A |
| 9 | Sınır (limit) anahtarları | 3–6 | NC bağlanabilir, mekanik ömrü uzun | Eklem başına 1–2 |
| 10 | Güç kablosu | m | Akıma göre kesit, hareketli eklemlerde esnek | 1 mm² (kırmızı/siyah) |
| 11 | Sinyal kablosu + blendajlı enkoder kablosu | m | Çok damarlı, blendajlı | 0.25 mm² |
| 12 | Konnektörler | set | Akım kapasitesi, ters takılamaz ve kilitli tip | Güç: XT30/XT60 veya vidalı klemens. Sinyal: kilitli tip |
| 13 | DIN ray, klemensler, kablo kanalı | set | Pano düzeni | — |
| 14 | Kablo pabucu, makaron, kablo bağı, etiket | set | — | — |
| 15 | Fren direnci (gerekirse) | 0–1 | Sürücü belgesine göre (rejeneratif enerji) | Sürücüye bağlı |
| 16 | Ölçüm: multimetre, akım sınırlı laboratuvar güç kaynağı | lab | İlk enerji verme için şart | Laboratuvarda varsa ödünç |
| 17 | Yedekler | — | Sürücü, sigorta, konnektör | %15–20 pay |

## 4. Motor sürücüsü seçim kontrol listesi

- [ ] Besleme gerilim aralığı 24 V'u rahatça kapsıyor (üst sınıra yakın değil).
- [ ] Sürekli akım ≥ motorun anma akımı, tepe akım ≥ hızlanma anındaki akım.
- [ ] Akım sınırı ayarlanabiliyor (ilk testler düşük akımla yapılır).
- [ ] **Enable (etkinleştirme) girişi var.** E-stop ve yazılım bu girişle sürücüyü kapatabilir.
- [ ] Arayüz Kişi 3'ün kartına uygun: STEP/DIR, PWM+DIR, UART veya CAN. Sinyal seviyesi (5 V / 3.3 V) uyumlu.
- [ ] Korumalar var: aşırı akım, aşırı ısı, düşük gerilim.
- [ ] Soğutma düşünüldü: Sürekli akımda ısınma için soğutucu veya fan gerekiyor mu?
- [ ] Frenleme sırasında geri gelen enerji için fren direnci gerekip gerekmediği kontrol edildi.
- [ ] Belgesi (datasheet) ve bağlantı şeması mevcut, yedeği Türkiye'den bulunabiliyor.

## 5. Acil durdurma (e-stop) devresi

```text
 +24 V ──[ANA SİGORTA]──┬──────────────────────────────────────────────┐
                         │                                              │
                         │   E-STOP (NC, kanal 1) ──┐                    │
                         │   E-STOP (NC, kanal 2) ──┤                    │
                         │   RESET (NO) ────────────┤                    │
                         │                    [GÜVENLİK RÖLESİ]          │
                         │                          │ çıkış              │
                         │                    [KONTAKTÖR bobini]         │
                         │                                              │
                         └──[KONTAKTÖR kontağı]──┬── Sürücü 1, 2, 3 (+V) │
                                                 └── Fren besleme       │
                                                                        │
   Güvenlik rölesi durum çıkışı ──► mikrodenetleyici girişi ("STOP var")│
   DC-DC 24→5 V (mantık) ◄──────────────────────────────────────────────┘
```

**Tasarım kuralları:**

- **NC ve çift kanal:** Kablo koparsa ya da kontak yapışırsa sistem güvenli tarafa geçer, yani durur.
- **E-stop motor gücünü keser, mantık devresini kesmez.** Böylece mikrodenetleyici durmanın sebebini kaydeder.
- **Kendiliğinden yeniden başlama yok:** Butonun mandalı açılsa bile reset butonuna basılmadan kontaktör kapanmaz.
- **Fren beslemesi kontaktörden sonra alınır.** Fail-safe (yaylı) fren, gücü kesilince kapanır ve eklemi tutar.
- **Stop 0 mı, Stop 1 mi?** Stop 0'da güç hemen kesilir. Stop 1'de önce sürücülere "dur" komutu verilir (enable kapatılır veya hız sıfırlanır), güç gecikmeli röle çıkışıyla sonra kesilir. Seçim Kişi 5 ve İSG görüşüyle birlikte yapılır ([Konu 10.2](konular/10-guvenlik.md)).
- **Yazılımla durdurma e-stop değildir.** Yazılım yalnızca ek bir katmandır.

> ⚠️ 230 V AC tarafında çalışmayın. Sertifikalı, kapalı kasa bir güç kaynağı kullanın ve şebeke tarafını açmayın. Bu devre bir taslaktır. Elektrik testinden önce K7 güvenlik kontrol listesi ve grup lideri onayı tamamlanmalı, İSG görüşü alınmalıdır.

## 6. Sensör bağlantıları

| Sensör | Bağlantı kuralı | Dikkat |
|---|---|---|
| **Enkoder** (A/B, varsa Z) | Blendajlı kablo kullanılır, blendaj **yalnızca kart tarafında** toprağa bağlanır. Güç kablolarından ayrı demetlenir | 5 V'luk enkoder 3.3 V'luk karta bağlanacaksa **seviye dönüştürücü** gerekir. Uzun kabloda diferansiyel (RS-422) enkoder daha güvenilirdir |
| **Sınır anahtarı** | **NC** bağlanır, kart girişinde pull-up direnci olur | Kablo koparsa "sınıra ulaşıldı" okunur ve motor durur, yani güvenli taraf. Yazılımda debounce yapılır |
| **Potansiyometre** (hobi servo) | 3 hat: besleme, GND, sinyal. Analog girişe kısa kabloyla bağlanır | Motor gürültüsü okumayı bozabilir, RC filtre eklenir |
| **Akım ölçümü** | Sürücünün akım çıkışı veya şönt direnç + yükselteç | Tutucuda "tuttum mu?" bilgisi ve aşırı yük tespiti için |
| **E-stop durum sinyali** | Güvenlik rölesinin durum kontağı → kart girişi | Yazılım durumu bilir, ama durdurmayı **donanım** yapar |

## 7. Kablolama kuralları

- **Renk kodu:** Ekipçe bir kez seçilir ve yazılır. Yaygın kullanım: +24 V kırmızı, 0 V/GND siyah, +5 V turuncu, sinyaller diğer renkler. IEC 60204-1'e göre koruma toprağı her zaman **yeşil-sarıdır**.
- **Etiket:** Her kablonun iki ucunda aynı etiket bulunur (örneğin `M1-A+`, `ES-K1`). Etiket listesi bir tabloda tutulur.
- **Kesit:** Güç hattı ≥ 1 mm², sinyal hattı 0.14–0.25 mm². Uzun hatlarda gerilim düşümü hesaplanır ([O2.3](ortak/o2-elektrik-guc.md)).
- **Topraklama:** Bütün GND'ler tek noktada birleşir (yıldız topraklama). Güç ve sinyal kabloları ayrı kanallardan geçer.
- **Hareketli eklemler:** Esnek (çok telli) kablo, yeterli bükülme yarıçapı ve gerilme önleyici (strain relief) kullanılır. Kablo eklem dönerken sıkışmamalı ve gerilmemeli. Güzergâh Kişi 1 ile birlikte planlanır.
- **Konnektörler:** Ters takılamayan, kilitli tipler. Güç ve sinyal için farklı konnektör aileleri kullanılır, böylece birbirine karıştırılamaz.

## 8. Test prosedürleri

### T2 · İlk enerji verme (tek eklem test düzeneği)

1. **Enerjisiz kontrol:** Görsel kontrol yapılır, kablo etiketlerine bakılır, multimetreyle **+24 V ile GND arasında kısa devre olmadığı** ölçülür.
2. **Akım sınırlı ilk enerji:** Laboratuvar güç kaynağı 24 V'a, akım sınırı düşük bir değere (örneğin 0.5 A) ayarlanır. Sürücü bağlıdır, motor bağlı değildir. Akım ve ısınma gözlenir.
3. **Önce e-stop:** Motor bağlanmadan önce, e-stop'a basıldığında sürücü beslemesinin kesildiği ölçülür.
4. **Motor yüksüz:** Sürücünün akım limiti düşük tutulur, motor eklemden ayrıktır. Yön, hız ve enkoder sayımı kontrol edilir (Kişi 3 ile).
5. **Kayıt:** Ölçümler senaryo kaydına ([O6 şablonu](ortak/o6-simulasyon-veri.md)) ve Haftalık Form'a yazılır.

**Çıkış kriteri (öneri):** 5 adım komutunun 5'inde yön doğru, enkoder sayımı beklenenden en fazla ±%1 sapıyor, e-stop 5 denemenin 5'inde sürücü beslemesini kesiyor.

### T7 · Güvenlik testleri (yüksüz hareket, sınır anahtarları, acil durdurma)

| Test | Yöntem | Çıkış kriteri (öneri) |
|---|---|---|
| E-stop durdurma | Kol hareket ederken e-stop'a basılır, durma süresi videodan ölçülür | 5 denemenin 5'inde ≤ 0.5 s içinde duruyor |
| Yeniden başlama | E-stop mandalı açılır, reset'e basılmaz | Kol hareket etmiyor |
| Güç kesme | Kol yatayken ana güç kesilir | Eklemler 1°'den fazla düşmüyor (fren veya dengeleme sayesinde) |
| Sınır anahtarı | Her eklem yavaşça sınıra sürülür | Anahtara gelince motor duruyor, 3 tekrarın 3'ünde |
| Kablo kopması | Sınır anahtarının kablosu çıkarılır | Sistem "sınırda" okuyup duruyor |

## 9. Çıktılarım

- [ ] Elektrik malzeme listesi (Bölüm 3) — **son gün 20 Kasım**
- [ ] Güç dağıtım şeması (O2 çıktısı; taslak [O2 sayfasında](ortak/o2-elektrik-guc.md)) — P2
- [ ] Acil durdurma devre şeması (Bölüm 5) — K7 ile, elektrik testinden önce
- [ ] Güvenlik kontrol listesinin elektrik maddeleri (Kişi 5 ile) — P3
- [ ] Pin ve kablo listesi (etiket tablosu) — Kişi 3 ile, T2'den önce
- [ ] T2 ve T7 test kayıtları
- [ ] Final raporunun elektrik bölümü — T14

## 10. Hafta hafta iş listesi

Liste proje planından ve syllabus'taki Kişi 2 tanımından türetildi. Ekiple teyit edilmelidir. ⭐ kritik işleri, 📄 bir çıktı üreten işleri gösterir.

| Hafta | Son tarih | İş | Birlikte |
|---|---|---|---|
| H1 | 15 Kas | O1 ve O3 ortak derslerini bitir | Tüm ekip |
| H1 | 15 Kas | K1 · Manipülatör temelleri ([Konu 1](konular/01-temeller.md)) | Kişi 1 öncelikli |
| H1 | 15 Kas | ⭐📄 Elektrik malzeme listesi taslağı (Bölüm 3) | Kişi 1 (motor tipi), Kişi 3 (kart ve arayüz) |
| H2 | 18 Kas | ⭐ K4 · Tork hesabından motor ve sürücünün akım/gerilim gereksinimini çıkar | Kişi 1 |
| H2 | 19 Kas | Sürücü seçim kontrol listesini motor adaylarına uygula (Bölüm 4) | Kişi 1, Kişi 3 |
| H2 | **20 Kas** | ⭐ Elektrik siparişlerini ve onaylarını kapat | Grup lideri, danışman |
| H2 | 20 Kas | ⭐ O2 · Elektrik ve güç dersini bitir (sorumlusu sensin) | Tüm ekip |
| H2 | 20 Kas | ⭐📄 Güç dağıtım şemasını gerçek parçalarla güncelle | — |
| H2 | 20 Kas | O4 · Kontrol ve PID dersi | Tüm ekip |
| — | 21–29 Kas | *Ara sınav: çalışma yok* | — |
| H3 | 30 Kas | Teslimata hazırlık: elektrik çalışma alanı, envanter kodları, test kayıt şablonu | Kişi 5 |
| T1 | 6 Ara | ⭐📄 K7 · Acil durdurma devre şeması ve güvenlik listesinin elektrik maddeleri | Kişi 5, İSG |
| T1 | 6 Ara | Elektrik parçalarını teslim al, say, kontrol et, eksik listesi çıkar | Kişi 5 |
| T1 | 6 Ara | O5 · ROS 2 temelleri | Tüm ekip |
| T1 | 6 Ara | 📄 Pin ve kablo listesi (etiket tablosu) | Kişi 3 |
| T2 | 13 Ara | ⭐ Tek eklem test düzeneği: ilk enerji verme prosedürü (Bölüm 8) | Kişi 3 |
| T3–T5 | 3 Oca | Kablolama, konnektörler, kablo etiketleme ve güç panosu montajı | Kişi 1 (kablo güzergâhı) |
| T3–T5 | 20 Ara | O6 · Simülasyon ve veri analizi | Tüm ekip |
| T6 | 10 Oca | 📄 Elektrik şemalarını belgele (hafif hafta, elektrikli test yok) + O7 | — |
| — | 11–24 Oca | *Final sınavı: çalışma yok* | — |
| T7 | 31 Oca | ⭐📄 Güvenlik testleri: e-stop, yeniden başlama, güç kesme, sınır anahtarları, kablo kopması | Kişi 5 |
| T8–T9 | 14 Şub | PID ayarı sırasında akım ölçümü ve sürücü akım limiti ayarı | Kişi 3 |
| T10–T11 | 28 Şub | Tutucu servosunun beslemesi ve tutucu sensör bağlantıları | Kişi 1, Kişi 3 |
| T12–T13 | 14 Mar | Görev testlerinde kablo dayanıklılığı ve elektrik arızası takibi | Kişi 5 |
| T14 | 21 Mar | 📄 Final raporunun elektrik bölümü ve devir teslim | — |

## ✍️ Kendini sına

<details>
<summary><b>1.</b> Sürücü sürekli 2.5 A çekiyor. Sigortayı kaç amper seçersin?</summary>
<br>
Hat akımının yaklaşık 1.25–1.5 katı: 2.5 × 1.25–1.5 ≈ 3.1–3.75 A. Bu durumda <b>3.15 A veya 4 A gecikmeli</b> bir sigorta seçilir. Gecikmeli tip, motorun kalkış akımında sigortanın atmaması içindir. Kablo kesiti de sigorta değerini güvenle taşıyabilmelidir.
</details>
<details>
<summary><b>2.</b> E-stop ve sınır anahtarları neden NC (normalde kapalı) bağlanır?</summary>
<br>
NC devrede normal durumda akım akar. Kablo koparsa, konnektör çıkarsa ya da kontak açılırsa akım kesilir ve sistem bunu "dur" olarak algılar. NO bağlansaydı kopuk bir kablo fark edilmezdi ve basılan buton hiçbir şey yapmazdı.
</details>
<details>
<summary><b>3.</b> Kol hızla yavaşlarken sürücünün besleme gerilimi yükseliyor. Neden ve ne yapılır?</summary>
<br>
Yavaşlayan motor jeneratör gibi çalışır ve enerjiyi beslemeye geri basar (rejeneratif enerji). Güç kaynağı bu enerjiyi geri alamazsa gerilim yükselir ve sürücü aşırı gerilim korumasına girer ya da zarar görür. Çözüm, sürücünün önerdiği <b>fren direnci</b>ni (brake chopper) kullanmak ya da kaynağın çıkışına kapasitör eklemektir. Ayrıntı sürücünün belgesindedir.
</details>
<details>
<summary><b>4.</b> 5 V çıkışlı bir enkoderi 3.3 V'luk karta doğrudan bağlayabilir misin?</summary>
<br>
Hayır. Çoğu 3.3 V'luk mikrodenetleyici girişi 5 V'a dayanıklı değildir ve zarar görebilir. Bunun yerine seviye dönüştürücü, gerilim bölücü ya da 3.3 V ile beslenebilen bir enkoder kullanılır. Kartın belgesinde "5 V tolerant" yazan pinler bunun istisnasıdır.
</details>

## Kaynaklar
[9] Hughes & Drury · [23] ISO 13850 · [24] IEC 60204-1 · [25] ISO 13849-1 · [31] Horowitz & Hill. Tam künyeler: [KAYNAKLAR.md](KAYNAKLAR.md)

---
[← Proje planı](plan.html) · [🏠 Ana sayfa](README.md) · [📖 Sözlük](SOZLUK.md) · [O2 · Elektrik ve güç →](ortak/o2-elektrik-guc.md)
