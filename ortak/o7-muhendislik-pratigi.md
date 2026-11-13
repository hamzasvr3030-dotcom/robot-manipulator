# O7 · Mühendislik Pratiği ve Kayıt Düzeni

> 📋 **Syllabus:** O7 · **Dönem:** P5 (21 Aralık – 10 Ocak) · **Tahmini süre:** 2 saat · **Kimler:** tüm ekip · **Çıktı:** Proje haftalık raporu (takip çizelgesindeki Haftalık Form) · **Şablon:** [`sablonlar/haftalik_rapor.md`](../sablonlar/haftalik_rapor.md)

> ### 🎯 Kısaca
> İyi bir ekip yalnızca çalışan bir robot yapmaz. **Ne istediğini** yazar (gereksinim), **nasıl test edeceğini** önceden söyler (test planı ve çıkış kriteri), ve **ne olduğunu kaydeder** (hata, değişiklik ve olay kaydı, haftalık ve aylık rapor). Böylece:
> - Herkes aynı hedefe çalışır.
> - Bir sorun çıktığında geriye dönüp bakılabilir.
> - Proje başkasına devredilebilir.

> 🧠 **Benzetme:** "Kol hedefe ulaşıyor" demek, "yemek güzel olmuş" demek gibidir: Herkes farklı bir şey anlar. "10 denemenin 9'unda uç, hedefe 5 mm içinde ulaşıyor" demek ise **tarif**tir: Herkes aynı şeyi ölçer, aynı sonuca varır.

## O7.1 Gereksinim yazımı

İyi bir gereksinim tek bir şey söyler, **ölçülebilir** ve **test edilebilir**dir.

| ❌ Belirsiz | ✅ Ölçülebilir |
|---|---|
| Kol hızlı olmalı. | Kol, A'dan B'ye 0.4 m'lik hareketi **en fazla 2 s'de** tamamlamalıdır. |
| Kol yeterince güçlü olmalı. | Kol, tam erişimde **0.5 kg** yükü yatay konumda en az **60 s** tutabilmelidir. |
| Hassas olmalı. | Tekrarlanabilirlik: 10 tekrarda bitiş konumunun std'si **≤ 2 mm** olmalıdır. |
| Güvenli olmalı. | Acil durdurmaya basıldıktan sonra kol **en fazla 0.5 s içinde** durmalı ve güç kesilince düşmemelidir. |
| Tutucu çalışmalı. | Tutucu, 20–60 mm çaplı nesneleri **20 denemenin en az 18'inde** düşürmeden kaldırmalıdır. |

> ℹ️ Kolun yük, erişim ve hassasiyet değerleri **Proje Kartı'nda** belirlenir. Yukarıdaki sayılar yalnızca örnektir.

## O7.2 Test planı ve çıkış kriteri

Her testin önceden yazılmış bir **amacı**, **yöntemi** ve **geçti/kaldı kriteri** vardır. Proje planındaki her haftanın bir çıkış kriteri vardır ([Proje planı](../plan.html)).

| Alan | Örnek: T2 tek eklem testi |
|---|---|
| Amaç | Motor, sürücü ve enkoder zincirinin doğru çalıştığını göstermek |
| Ön koşul | O2 ve güvenlik modülü tamam, e-stop bağlı, eklem yüksüz |
| Yöntem | ±90°'lik 5 adım komutu gönder. Yönü, sınır anahtarını ve enkoder sayımını kontrol et |
| Ölçülecek | Komut ile ölçülen açı arasındaki fark, yön, sınırda durma |
| **Çıkış kriteri** | 5 adımın 5'inde yön doğru, son konum hatası < 1°, sınır anahtarında motor duruyor |
| Kayıt | Senaryo kaydı (O6), veri dosyası, haftalık form |

## O7.3 Kayıtlar ve formlar

| Kayıt / form | Ne zaman? |
|---|---|
| **Proje Kartı** | Proje başında. Hedef, DOF, erişim, yük ve ekip burada belirlenir. Kart onaylanmadan motor ve mekanik seçimleri kesinleşmez |
| **Satın Alma** | Her malzeme ihtiyacında (Çalışma Tablosu "Satın Alma" sayfası) |
| **Envanter** | Malzeme teslim alınınca. Her parçaya envanter kodu verilir (DM-ELK-xxxx) |
| **Rezervasyon** | Laboratuvar veya cihaz kullanımı öncesinde |
| **Cihaz Eğitim ve Yetki Formu** | 3B yazıcı, tezgâh ve benzeri cihazları kullanmadan önce |
| **Olay ve Kaza Kayıt Formu** | Her olayda veya ramak kala durumunda, küçük olsa bile |
| **Malzeme Ödünç ve Teslim Formu** | Ödünç alınan veya verilen parça için |
| **Hata ve değişiklik kaydı** | Bir hata bulunduğunda veya tasarım değiştiğinde (örneğin GitHub Issues) |
| **Haftalık Form** | Her hafta (Haftalık Çalışma Takip Çizelgesi) |
| **Aylık ilerleme raporu** | Her ayın sonunda |

**Hata kaydı örneği:**

| No | Tarih | Bulan | Belirti | Kök neden | Çözüm | Durum |
|---|---|---|---|---|---|---|
| H-007 | 2026-12-10 | Kişi 3 | Eklem 2 ters yöne dönüyor | Motor kabloları ters bağlanmış | Yazılımda yön çarpanı −1 yapıldı, kablo etiketlendi | Kapandı |

## O7.4 Haftalık rapor (çıktı)

Dosya olarak: [`sablonlar/haftalik_rapor.md`](../sablonlar/haftalik_rapor.md). Alanlar, Haftalık Çalışma Takip Çizelgesi'ndeki sütunlarla aynıdır:

| Alan | Örnek (H1, değerler yalnızca örnektir) |
|---|---|
| Hafta / tarih | H1 · 12–15 Kasım 2026 |
| Hedef | Proje Kartı, kol hedefi, malzeme listesi ve sipariş teyidi, ROS 2 kurulumu, düz ve ters kinematik |
| Çıkış kriteri | Onaylı kart, sipariş teyidi, kurulu ortam |
| Kişi saatleri | Kişi 1: 4 sa · Kişi 2: 3 sa · Kişi 3: 5 sa · Kişi 4: 6 sa · Kişi 5: 4 sa · **Toplam: 22 sa** |
| Durum | Planlandı / Devam ediyor / **Tamamlandı** / Gecikti |
| Çıkış kriteri sağlandı mı? | Evet / **Kısmen** / Hayır |
| Engel / not | "ESC-3 için yedek parça siparişi verildi" gibi. Ders, hastalık ve teslim gecikmesi de buraya yazılır |
| Gelecek hafta | H2 hedefleri |

## ✍️ Kendini sına (syllabus sorusu)

<details>
<summary><b>1.</b> "Çalışıyor" yerine ölçülebilir bir çıkış kriteri yazın.</summary>
<br>
Syllabus'taki örnek: "5 denemede 4'ünde hedef noktaya 10 cm içinde ulaşır." Robot kol için örnekler:
<ul>
<li><b>Ters kinematik (simülasyon):</b> Çalışma uzayından rastgele seçilen 100 hedefin hepsinde FK(IK(hedef)) ile hedef arasındaki fark < 0.1 mm. Erişilemeyen hedefler "çözüm yok" olarak raporlanmalı.</li>
<li><b>PID (T8–T9):</b> 0° → 60° quintic yörüngede RMSE < 0.5° ve tepe tork < 8 N·m. 3 denemenin 3'ünde sağlanmalı.</li>
<li><b>Tut-bırak (T12–T13):</b> 20 denemenin en az 17'sinde nesne hedef kutuya bırakılır. Bitiş konumunun std'si ≤ 3 mm.</li>
<li><b>Güvenlik (T7):</b> E-stop 5 denemenin 5'inde kolu 0.5 s içinde durdurur. Güç kesildiğinde eklemler 1°'den fazla düşmez.</li>
</ul>
</details>

## ⚡ Akılda kalsın
- Gereksinim **tek, ölçülebilir ve test edilebilir** olmalıdır. "Hızlı" yerine "2 s içinde" yazılır.
- Test başlamadan **çıkış kriteri** yazılır.
- Olay, hata ve değişiklik **küçük de olsa kaydedilir**.
- Haftalık form + aylık rapor = projenin hafızası.

## Kaynaklar
[36] NASA Systems Engineering Handbook · [26] ISO 12100. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← O6 · Simülasyon ve veri](o6-simulasyon-veri.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [1 · Temeller →](../konular/01-temeller.md)
