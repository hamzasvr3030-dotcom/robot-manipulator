# 9 · Güvenlik: Sıkışma/Ezilme Riski, Acil Durdurma, Güç Kesme

> **Çıktı türü:** Liste

> ⚠️ Bu liste eğitim amaçlıdır ve kendi başına bir uygunluk değerlendirmesi yerine geçmez. Gerçek bir robot hücresi devreye alınmadan önce ilgili standartlara göre **risk değerlendirmesi** yapılmalıdır. Bu değerlendirmenin yetkin bir kişi tarafından yapılması gerekir.

## 9.1 Temel tehlikeler

| Tehlike | Nasıl oluşur? | Örnek |
|---|---|---|
| **Sıkışma / ezilme** | Robot ile sabit bir nesne arasında vücut kısmı kalır | Kol masaya doğru inerken el arada kalır |
| **Çarpma** | Hareketli kol insana serbestçe çarpar | Hızlı bir eklem hareketinde kafaya darbe |
| **Kesme / delme** | Keskin tutucu, parça veya takım | Bıçaklı uç efektör |
| **Fırlatma** | Tutucu parçayı bırakır, parça savrulur | Hava basıncı kesilince vakumun bırakması |
| **Beklenmedik hareket** | Yazılım hatası, enkoder hatası, yeniden başlatma | Enerji geri gelince kolun aniden hareket etmesi |
| **Yerçekimiyle düşme** | Güç kesilince kol kendi ağırlığıyla çöker | Fren olmayan bir eklemin düşmesi |
| **Elektrik** | Yüksek gerilimli sürücü ve kablolar | Kapasitörlerde kalan yük |

## 9.2 Durdurma kategorileri (IEC 60204-1)

Bu kategoriler IEC 60204-1 [24] ve ISO 13850 [23]'te tanımlıdır:

| Kategori | Ne olur? | Ne zaman? |
|---|---|---|
| **Stop 0** | Motor gücü **hemen** kesilir, sistem kontrolsüz durur (frenler devreye girer) | Acil durumda, en basit çözüm |
| **Stop 1** | Önce **kontrollü** frenleme yapılır, durduktan sonra güç kesilir | Endüstriyel robot e-stop'unda en yaygın kullanım |
| **Stop 2** | Kontrollü durulur, güç **kesilmez** (konum tutulur) | Koruyucu durma; acil durdurma olarak kullanılamaz |

Acil durdurma yalnızca **Stop 0 veya Stop 1** olabilir [23], [24].

## 9.3 Güvenlik kontrol listesi

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

## Kaynaklar
[21] ISO 10218-1/-2:2025 · [22] ISO/TS 15066 · [23] ISO 13850 · [24] IEC 60204-1 · [25] ISO 13849-1 · [26] ISO 12100 · [27] Haddadin vd. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)
