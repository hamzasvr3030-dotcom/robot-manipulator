# 🦾 Robotik Kol Takımı — Temel Bilgiler

**Temel Bilgiler Syllabus'u**ndaki **ortak dersler (O1–O7)** ile **robotik kol modülleri (K1–K7)** ve **Robotik Kol Projesi Hazırlık ve Uygulama Dosyası**ndaki 10 konuyu anlatan çalışma deposudur. Bütün konular **tek bir örnek kol** üzerinden işlenir. Her sayfada teori, çözümlü örnek, kendini sınama soruları ve somut bir çıktı var: şema, hesap, kod, grafik veya liste. Sayfalardaki tüm sayılar ve grafikler depodaki Python kodlarından üretilmiştir.

🌐 **Web sitesi (önerilen):** <https://hamzasvr3030-dotcom.github.io/robot-manipulator/>. Sitede menü, açık/koyu tema, düzgün formüller, **bu haftanın planı** ve interaktif laboratuvar bulunur.

![Örnek kol ve çalışma uzayı](gorseller/01_kol_semasi.png)

**Örnek kol:** Düşey düzlemde çalışan 3 eklemli düzlemsel RRR kol. Uzuv boyları $L_1 = 0.30$ m, $L_2 = 0.25$ m, $L_3 = 0.10$ m. Yük kapasitesi 0.5 kg. Bu değerler öğrenme amaçlıdır. Gerçek kolun değerleri Proje Kartı'nda belirlenecek.

## 📅 Takvim ve plan

Tam plan için: **[Proje planı ve takvim](https://hamzasvr3030-dotcom.github.io/robot-manipulator/plan.html)**. Bu sayfada dönemler, modül haritası, iş grupları, H1–H3 ve T1–T14 haftaları, simülasyon planı, geçiş kriterleri ve riskler var.

| Dönem | Tarih | Ortak dersler | Robotik kol |
|---|---|---|---|
| P1 | 12–15 Kasım | O1, O3 | K1 (Konu 1), K2 (Konu 2) |
| P2 | 16–20 Kasım | O2, O4 | K3 (Konu 3), K4 (Konu 5) |
| Sınav | 21–29 Kasım | — | — |
| P3 | 30 Kasım – 6 Aralık | O5 | **K7 güvenlik (zorunlu)** (Konu 10), K5 (Konu 4, 6) |
| P4 | 7–20 Aralık | O6 | K5, K6 (Konu 7, 8, 9) |
| P5 | 21 Aralık – 10 Ocak | O7, tekrar | K6 · 4–10 Ocak hafif hafta |
| Sınav | 11–24 Ocak | — | — |
| P6 | 25 Ocak sonrası | Proje içi öğrenme | Test sonuçlarından çıkan konular |

> ⚠️ O2 ve K7 (güvenlik) **ilk elektrik testinden (07–13 Aralık) önce** tamamlanır. Güvenlik modülleri eksikse ilgili test yapılmaz.

## 🧱 Ortak dersler (tüm takımlar)

| Modül | Sayfa | Dönem | Süre | Çıktı |
|---|---|---|---|---|
| O1 | [Matematik ve fizik minimumu](ortak/o1-matematik-fizik.md) | P1 | 5 sa | Çözümlü soru kâğıdı ([`kod/o1_cozumlu.py`](kod/o1_cozumlu.py)) |
| O2 | [Elektrik ve güç temelleri](ortak/o2-elektrik-guc.md) | P2 | 4 sa | Güç dağıtım şeması taslağı |
| O3 | [Yazılım altyapısı](ortak/o3-yazilim-altyapisi.md) | P1 | 5 sa | Ekip deposu ve kod/commit kuralları ([`kod/o3_csv_grafik.py`](kod/o3_csv_grafik.py)) |
| O4 | [Kontrol temelleri ve PID](ortak/o4-kontrol-pid.md) | P2 | 6 sa | P, PI, PID karşılaştırma grafiği ([`kod/o4_adim_yaniti.py`](kod/o4_adim_yaniti.py)) |
| O5 | [ROS 2 temelleri](ortak/o5-ros2.md) | P3 | 8 sa | Yayıncı/abone paketi ve launch ([`ros2/kol_ornek/`](ros2/kol_ornek)) |
| O6 | [Simülasyon ve veri analizi](ortak/o6-simulasyon-veri.md) | P4 | 4 sa | Senaryo kayıt şablonu ([`kod/o6_senaryo.py`](kod/o6_senaryo.py)) |
| O7 | [Mühendislik pratiği ve kayıt düzeni](ortak/o7-muhendislik-pratigi.md) | P5 | 2 sa | Haftalık rapor şablonu ([`sablonlar/`](sablonlar)) |

## 🦾 Robotik kol konuları

| # | Konu | Syllabus | Ay sonu hedefi | Doğrulama |
|---|------|---|---|-------|
| 1 | [Robot manipülatör temelleri](konular/01-temeller.md): eklem tipleri, serbestlik derecesi, çalışma uzayı | K1 | Seçilen kolu şemada anlatır | 🖼️ Şema |
| 2 | [Düz kinematik](konular/02-duz-kinematik.md): dönüşüm matrisleri, DH parametreleri | K2 | Verilen kol için uç nokta konumunu hesaplar | 🧮 Hesap |
| 3 | [Ters kinematik](konular/03-ters-kinematik.md): analitik ve sayısal çözüm fikri | K3 | 2–3 eklemli kol için çözer | 💻 Kod |
| 4 | [Eklem uzayı ve kartezyen yörünge planlama](konular/04-yorunge-planlama.md) | K5 | Basit bir yörünge üretir | 📈 Grafik |
| 5 | [Motorlar](konular/05-motorlar.md): servo, step, BLDC, tork, redüktör, sürücü seçimi | K4 | Eklem torku hesabı yapar | 📊 Hesap sayfası |
| 6 | [Kontrol](konular/06-kontrol.md): PID, konum/hız döngüsü, geri besleme (potansiyometre/enkoder) | K5 | Simülasyonda eklem takibi gösterir | 📈 Grafik |
| 7 | [Tutucu (gripper) tasarımı ve temel sensörler](konular/07-tutucu.md) | K6 | Tutucu seçenekleri notu | 📝 Not |
| 8 | [Yazılım](konular/08-yazilim.md): URDF, ROS 2, MoveIt 2 temelleri, Python | K6 | Modeli yükler, hareket planlar | 📦 Depo |
| 9 | [Algılama](konular/09-algilama.md) (hedefe bağlı): kamera, nesne konumu, kamera–robot kalibrasyonu | K6 | Temel görüntü işleme örneği | 🖥️ Çıktı |
| 10 | [Güvenlik](konular/10-guvenlik.md): sıkışma/ezilme riski, acil durdurma, güç kesme | K7 | Güvenlik kontrol listesi | ✅ Liste |

**Her sayfa aynı düzende ilerler:** 📋 Syllabus kutusu (dönem, süre, sorumlu kişi, ön koşul) → 🎯 Kısaca → 🧠 Benzetme → teori ve uygulama → ⚡ Akılda kalsın → ✍️ Kendini test et (cevaplar tıklayınca açılır).

**Yardımcı sayfalar:**
- 🎮 **[İnteraktif laboratuvar](https://hamzasvr3030-dotcom.github.io/robot-manipulator/interaktif.html):** Konu 2–6 için hazır örnekler ve canlı adım adım hesap.
- 📖 **[Terimler sözlüğü](SOZLUK.md)** · 📚 **[Kaynakça](KAYNAKLAR.md)**

## 🗂️ Depo yapısı

```text
robot-manipulator/
├── README.md, plan.html     ← bu sayfa, proje planı (veri: _data/plan.yml)
├── ortak/                   ← O1–O7 ortak ders sayfaları
├── konular/                 ← 1–10 robotik kol konu sayfaları
├── kod/
│   ├── robot_kol.py         ← ortak model: DH, düz/ters kinematik, Jacobian
│   ├── eklem_sim.py         ← tek eklem PID simülatörü (gürültü, gecikme, sürtünme seçenekli)
│   ├── k01_sema.py … k09_goruntu.py    ← konu betikleri
│   ├── o1_ … o6_*.py                    ← ortak ders betikleri
│   └── tork_hesap_sayfasi.csv           ← Konu 5 hesap sayfası (Excel'de açılır)
├── veri/                    ← O6'nın ürettiği deney kayıtları (CSV)
├── sablonlar/               ← senaryo kaydı ve haftalık rapor şablonları
├── gorseller/               ← kodların ürettiği grafikler
├── urdf/rrr_kol.urdf        ← örnek kolun ROS modeli
└── ros2/                    ← RViz launch, MoveIt 2 örneği, kol_ornek paketi (O5)
```

## ▶️ Çalıştırma

```bash
pip install -r requirements.txt     # yalnızca numpy + matplotlib
cd kod
python k02_duz_kinematik.py         # her betik sonucu ekrana yazar, grafiği gorseller/ klasörüne kaydeder
python o6_senaryo.py && python o3_csv_grafik.py   # önce deney kaydı üretilir, sonra CSV'den grafik çizilir
```

Gerçek kolun değerleri belli olunca `kod/robot_kol.py` dosyasındaki `L` değerlerini, `kod/k05_tork.py` dosyasının başındaki girdileri ve `urdf/rrr_kol.urdf` dosyasını güncelleyin.

## ⚠️ Notlar
- Bu depo eğitim amaçlıdır. Güvenlik listesi gerçek bir risk değerlendirmesinin ve İSG görüşünün yerine geçmez.
- Python kodları çalıştırılıp doğrulandı. ROS 2 / MoveIt dosyaları ve `kol_ornek` paketi resmî dokümantasyona göre yazıldı, ancak ROS kurulu bir makinede test edilmedi.
- Takvim ve modül bilgileri danışman onayına sunulacak taslak belgelerden alınmıştır. Belgeler güncellenirse `_data/plan.yml` dosyası da güncellenmelidir.
