# 10 · Güvenlik: Sıkışma/Ezilme Riski, Acil Durdurma, Güç Kesme

> **Çıktı türü:** Liste

> 📋 **Syllabus:** K7 · Güvenlik (zorunlu) · **Dönem:** P3 (30 Kasım – 6 Aralık), ilk elektrik testinden (07–13 Aralık) önce · **Tahmini süre:** 3 saat · **Öncelikli:** Kişi 2 ve Kişi 5  
> **Ön koşul:** [O2 · Elektrik ve güç](../ortak/o2-elektrik-guc.md) · **Ay sonu hedefi:** Güvenlik kontrol listesini hazırlar · **Syllabus çıktısı:** Güvenlik kontrol listesi (İSG görüşüne tabi) · [Proje planı](../plan.html)

> ### 🎯 Kısaca
> Robot **güçlüdür, hızlıdır ve seni fark etmez**. Güvenlik, robotun insana zarar vermemesini garanti altına alan kuralların bütünüdür. Üç altın kural:
> 1. **Ayrı tut:** Robot çalışırken insan çalışma alanına girmesin. Girerse robot dursun.
> 2. **Durdurabil:** Herkes tek bir hareketle robotu durdurabilmeli. Bu durdurma **yazılıma güvenmemeli**.
> 3. **Enerji kesilince güvende kal:** Robotun gücü kesildiğinde kol düşmemeli ve güç geri geldiğinde kendi kendine harekete geçmemeli.

> 🧠 **Benzetme:** Acil durdurma butonu, arabadaki **el freni** gibidir. Bilgisayar donsa bile çalışmalıdır. Bu yüzden e-stop "programa stop komutu gönderen" bir düğme değildir. Motorların **gücünü fiziksel olarak keser**.

> ⚠️ Bu liste eğitim amaçlıdır ve kendi başına bir uygunluk değerlendirmesi yerine geçmez. Gerçek bir robot hücresi devreye alınmadan önce ilgili standartlara göre **risk değerlendirmesi** yapılmalıdır. Bu değerlendirmenin yetkin bir kişi tarafından yapılması gerekir.

## 10.1 Temel tehlikeler

| Tehlike | Nasıl oluşur? | Örnek |
|---|---|---|
| **Sıkışma / ezilme** | Robot ile sabit bir nesne arasında vücut kısmı kalır | Kol masaya doğru inerken el arada kalır |
| **Çarpma** | Hareketli kol insana serbestçe çarpar | Hızlı bir eklem hareketinde kafaya darbe |
| **Kesme / delme** | Keskin tutucu, parça veya takım | Bıçaklı uç efektör |
| **Fırlatma** | Tutucu parçayı bırakır, parça savrulur | Hava basıncı kesilince vakumun bırakması |
| **Beklenmedik hareket** | Yazılım hatası, enkoder hatası, yeniden başlatma | Enerji geri gelince kolun aniden hareket etmesi |
| **Yerçekimiyle düşme** | Güç kesilince kol kendi ağırlığıyla çöker | Fren olmayan bir eklemin düşmesi |
| **Elektrik** | Yüksek gerilimli sürücü ve kablolar | Kapasitörlerde kalan yük |

## 10.2 Durdurma kategorileri (IEC 60204-1)

Bu kategoriler IEC 60204-1 [24] ve ISO 13850 [23]'te tanımlıdır:

| Kategori | Ne olur? | Ne zaman? |
|---|---|---|
| **Stop 0** | Motor gücü **hemen** kesilir, sistem kontrolsüz durur (frenler devreye girer) | Acil durumda, en basit çözüm |
| **Stop 1** | Önce **kontrollü** frenleme yapılır, durduktan sonra güç kesilir | Endüstriyel robot e-stop'unda en yaygın kullanım |
| **Stop 2** | Kontrollü durulur, güç **kesilmez** (konum tutulur) | Koruyucu durma; acil durdurma olarak kullanılamaz |

Acil durdurma yalnızca **Stop 0 veya Stop 1** olabilir [23], [24].

## 10.3 Güvenlik kontrol listesi

### A. Tasarım
- [ ] Risk değerlendirmesi yapıldı: tehlikeler belirlendi, riskler tahmin edildi, önlemler tanımlandı [26].
- [ ] Güvenlik fonksiyonlarının gereken performans seviyesi (PLr) belirlendi ve ulaşılan seviye (PL) doğrulandı [25].
- [ ] Önlemler sırayla uygulandı:
  1. **Doğası gereği güvenli tasarım** (düşük kütle, yuvarlatılmış kenarlar, yeterli boşluklar)
  2. **Koruyucular**
  3. **Uyarı ve eğitim**
- [ ] Sıkışma noktalarında güvenlik boşluğu bırakıldı. Bu mümkün değilse kuvvet ve basınç sınırları uygulandı. İşbirlikçi robotlarda vücut bölgesine göre izin verilen değerler ISO/TS 15066 ve ISO 10218-2:2025'te verilir [21], [22], [27].
- [ ] Gravite altında düşebilecek eklemlerde **fren** var. Fren, güç kesildiğinde kapanan tipte (fail-safe).
- [ ] Yazılımda eklem sınırları, hız ve tork sınırları tanımlandı. Mümkünse bu sınırlar donanımda da var (mekanik stop, limit anahtarı).

### B. Acil durdurma (e-stop)
- [ ] Kırmızı mantar butonu sarı zemin üzerinde. Basılınca **mandallanıyor** (kendi kendine geri dönmüyor) [23].
- [ ] Her operatör konumundan ve öğretme cihazından (teach pendant) erişilebiliyor.
- [ ] E-stop **donanımla** çalışıyor: güvenlik rölesi veya güvenlik PLC'si üzerinden. Yalnızca yazılım ile yapılan bir "durdur" komutu **e-stop sayılmaz** [24].
- [ ] Devre **kontakları normalde kapalı (NC)** ve çift kanallı. Kablo koparsa sistem durur.
- [ ] Butonun mandalı açılınca robot **kendiliğinden yeniden başlamıyor**. Ayrı bir reset ve başlatma komutu gerekiyor [23].
- [ ] E-stop Stop 0 veya Stop 1 olarak çalışıyor ve gerçek yük altında periyodik olarak test ediliyor.

### C. Güç kesme ve enerji izolasyonu
- [ ] Ana şalter **kilitlenebilir** tipte (kilitleme/etiketleme, LOTO) [24].
- [ ] Güç kesilince kol **düşmüyor**: frenler tutuyor veya kol dengelenmiş.
- [ ] Pnömatik tutucuda hava basıncı kesilince parça düşmüyor: kendinden kilitli valf veya yay ile kapanma var.
- [ ] Sürücü kapasitörlerinin boşalma süresi etikette yazılı. Bu süre beklenmeden müdahale edilmiyor.
- [ ] Güç **geri geldiğinde** robot otomatik olarak harekete başlamıyor.

### D. Çalışma alanı koruması
- [ ] Hücre sabit çitle (perimeter guard) çevrili ve kapıda **kilitli güvenlik anahtarı** var. Kapı açılınca robot duruyor [21].
- [ ] Çit kullanılmıyorsa ışık perdesi, lazer tarayıcı veya güvenlik halısı var. Hız ve mesafe izleme yapılıyor.
- [ ] Güvenlik mesafeleri insan yaklaşma hızına göre hesaplandı.
- [ ] Zemin işaretli (sarı-siyah bant). Uyarı levhaları asılı.

### E. Çalıştırma ve bakım
- [ ] Öğretme modunda hız düşürülmüş (endüstriyel robotlarda ≤ 250 mm/s).
- [ ] Öğretme cihazında **3 konumlu onay (enabling) anahtarı** var.
- [ ] Yeni program önce düşük hızda ve **boş havada** (yük olmadan) deneniyor.
- [ ] Bakım LOTO prosedürüne göre yapılıyor.
- [ ] Operatörler eğitimli. Eğitim kayıt altında.
- [ ] Olay ve ramak kala (near-miss) durumları kayıt altına alınıyor.

### F. Bu depodaki eğitim kolu için minimum set
- [ ] Masaüstü e-stop butonu motor sürücülerinin **güç hattını** kesiyor (yalnızca mikrodenetleyicinin girişine bağlı değil).
- [ ] Kod içinde eklem sınırları (`Q_MIN`/`Q_MAX`) ve tork sınırı (`tau_maks`) uygulanıyor.
- [ ] İlk denemeler düşük hızda ve kol menzilinin (0.65 m) dışında durarak yapılıyor.
- [ ] Kolun düşmesine karşı ilk testlerde eklem 1 desteklenmiş. Ya da redüktör kendiliğinden kilitlenen tipte.

## ⚡ Akılda kalsın
- Önlemler bu sırayla düşünülür: **Önce tasarımla tehlikeyi yok et**, sonra koruyucu koy, en son uyarı ve eğitimle destekle.
- **E-stop** donanımla çalışır, mandallıdır, çift kanallıdır ve **Stop 0 veya Stop 1** kategorisindedir.
- Güç kesildiğinde **fren** kolu tutmalı. Güç geri geldiğinde robot **kendiliğinden başlamamalı**.
- Bakımdan önce **kilitle ve etiketle (LOTO)**.

## ✍️ Kendini test et
<details>
<summary><b>Soru:</b> Arduino'ya bağlı bir buton motorları yazılımla durduruyor. Bu bir e-stop sayılır mı?</summary>
<br>
Hayır. Program donarsa buton işe yaramaz. E-stop, motor sürücülerinin gücünü bir güvenlik rölesi üzerinden kesmelidir.
</details>
<details>
<summary><b>Soru:</b> Stop 2 neden acil durdurma olarak kullanılamaz?</summary>
<br>
Stop 2'de motorlara güç gitmeye devam eder. Yazılım veya sürücü arızalanırsa kol yeniden hareket edebilir.
</details>

## Kaynaklar
[21] ISO 10218-1/-2:2025 · [22] ISO/TS 15066 · [23] ISO 13850 · [24] IEC 60204-1 · [25] ISO 13849-1 · [26] ISO 12100 · [27] Haddadin vd. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← 9 · Algılama](09-algilama.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [Kaynakça →](../KAYNAKLAR.md)
