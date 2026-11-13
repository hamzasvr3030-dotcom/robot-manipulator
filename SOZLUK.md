# 📖 Terimler Sözlüğü

Sayfalarda geçen teknik terimlerin kısa ve sade açıklamaları. Son sütun, terimin ayrıntılı anlatıldığı yeri gösterir: 1–10 robotik kol konuları, O1–O7 ortak dersler.

| Terim | İngilizcesi | Ne demek? (sade) | Konu |
|---|---|---|---|
| **Manipülatör** | Manipulator | Eklemlerle birbirine bağlı uzuvlardan oluşan robot kol | 1 |
| **Uzuv** | Link | Kolun iki eklem arasındaki katı parçası, yani "kemiği" | 1 |
| **Eklem** | Joint | Uzuvları birbirine bağlayan hareketli bağlantı, yani "omuz" veya "dirsek" | 1 |
| **Döner eklem (R)** | Revolute | Bir eksen etrafında dönen eklem. Kapı menteşesi gibi | 1 |
| **Kayar eklem (P)** | Prismatic | Bir doğru boyunca kayan eklem. Çekmece gibi | 1 |
| **Serbestlik derecesi (DOF)** | Degrees of freedom | Kolun yapabildiği bağımsız hareketlerin sayısı | 1 |
| **Uç efektör** | End-effector | Kolun ucundaki işi yapan parça: tutucu, torç, vantuz vb. | 1 |
| **Çalışma uzayı** | Workspace | Kolun ucunun uzanabildiği bütün noktalar | 1 |
| **Poz** | Pose | Konum + yönelim birlikte. "Nerede ve hangi yöne bakıyor?" | 2 |
| **Homojen dönüşüm** | Homogeneous transform | Dönme ve taşıma bilgisini tek bir 4×4 tabloda tutan matris | 2 |
| **DH parametreleri** | Denavit–Hartenberg | Her eklemi 4 sayıyla tarif eden standart yöntem | 2 |
| **Düz kinematik** | Forward kinematics | Açılar biliniyor → uç nerede? | 2 |
| **Jacobian** | Jacobian | Eklem hızlarını uç hızına çeviren matris. "Eklemi biraz oynatırsam uç ne kadar oynar?" | 2 |
| **Tekillik** | Singularity | Kolun bir yönde hareket edemediği "kilitli" konum. Örneğin kol tamamen açıkken | 2 |
| **Ters kinematik (IK)** | Inverse kinematics | Uç şurada olmalı → açılar ne olmalı? | 3 |
| **Analitik çözüm** | Closed-form | Formülle doğrudan bulunan cevap | 3 |
| **Sayısal çözüm** | Numerical | Bir tahminle başlayıp adım adım yaklaşarak bulunan cevap | 3 |
| **DLS** | Damped least squares | Tekilliğe yakın konumlarda bile kararlı çalışan sayısal IK yöntemi | 3 |
| **Yol** | Path | Sadece geometri: hangi noktalardan geçileceği | 4 |
| **Yörünge** | Trajectory | Yol + zaman: her an konum, hız ve ivme | 4 |
| **Quintic polinom** | Quintic | Başta ve sonda hızı ve ivmesi sıfır olan, sarsıntısız hareket eğrisi | 4 |
| **Sarsıntı** | Jerk | İvmenin değişim hızı. Yüksek olursa titreşim yaratır | 4 |
| **Tork** | Torque | Döndürme kuvveti = kuvvet × kaldıraç uzunluğu [N·m] | 5 |
| **Redüktör** | Gearbox / reducer | Hızı düşürüp torku artıran dişli kutusu. Bisiklet vitesi gibi | 5 |
| **Çevrim oranı (N)** | Gear ratio | Redüktörün hızı kaç kat düşürdüğü | 5 |
| **Boşluk** | Backlash | Dişliler arasındaki küçük oynama payı. Hassasiyeti bozar | 5 |
| **Atalet** | Inertia | Bir cismin dönmeye karşı direnci [kg·m²] | 5 |
| **BLDC** | Brushless DC | Fırçasız motor: güçlü, verimli ve sessiz, ama sürücüsü karmaşık | 5 |
| **Step motor** | Stepper | Adım adım dönen ve enkodersiz konumlanabilen motor | 5 |
| **Enkoder** | Encoder | Motorun açısını ölçen sensör, yani robotun "gözü" | 6 |
| **Kapalı çevrim** | Closed loop | Ölç → karşılaştır → düzelt döngüsü | 6 |
| **PID** | PID | Hatanın şimdiki değerine (P), birikimine (I) ve değişim hızına (D) göre düzeltme yapan kontrolcü | 6 |
| **Kalıcı hata** | Steady-state error | Sistem durduktan sonra da kalan küçük hata | 6 |
| **Integral şişmesi** | Windup | Motor doymadayken integral teriminin gereksiz yere büyümesi | 6 |
| **Tutucu** | Gripper | Robotun "eli" | 7 |
| **Sürtünme katsayısı (μ)** | Friction coefficient | Yüzeylerin birbirinden ne kadar kolay kaydığını gösteren sayı | 7 |
| **ROS 2** | Robot Operating System 2 | Robot programlarının birbirleriyle konuştuğu ortak yazılım altyapısı | 8 |
| **Node / Topic / Service / Action** | — | Program / sürekli veri yayını / soru-cevap / uzun süren görev | 8 |
| **URDF** | Unified Robot Description Format | Robotun XML biçimindeki teknik tarifi: parçalar + eklemler | 8 |
| **MoveIt 2** | MoveIt 2 | Çarpışmasız hareket planlayan ROS 2 aracı. Robotun "GPS'i" | 8 |
| **RViz** | RViz | ROS'un 3B görselleştirme programı | 8 |
| **İç parametreler (K)** | Intrinsics | Kameranın odak uzaklığı ve görüntü merkezi. Pikseli metreye çevirmeye yarar | 9 |
| **El-göz kalibrasyonu** | Hand-eye calibration | Kameranın robota göre nerede durduğunu bulma işlemi | 9 |
| **Eşikleme** | Thresholding | Belirli bir renk aralığındaki pikselleri seçme | 9 |
| **Risk değerlendirmesi** | Risk assessment | Tehlikeleri bulma, büyüklüklerini tahmin etme ve önlem belirleme | 10 |
| **Acil durdurma** | Emergency stop (e-stop) | Robotu donanımla durduran mantar başlı kırmızı buton | 10 |
| **Stop 0 / 1 / 2** | Stop categories | 0: hemen güç kes · 1: önce yavaşla, sonra güç kes · 2: dur ama güç kalsın | 10 |
| **LOTO** | Lockout/Tagout | Bakım öncesi enerji kaynağını kilitleme ve etiketleme | 10 |

| **Dönme matrisi** | Rotation matrix | Bir vektörü belli bir açıyla döndüren tablo. Uzunluğu korur, tersi transpozudur | O1 |
| **atan2** | atan2 | Dört bölgede de doğru açıyı veren arktanjant fonksiyonu | O1 |
| **Standart sapma** | Standard deviation | Ölçümlerin ortalama etrafında ne kadar dağıldığı, yani gürültünün büyüklüğü | O1 |
| **Sabit hata** | Bias | Bütün ölçümlerin aynı yöne kayması. Ortalama almakla gitmez, kalibrasyonla düzelir | O1 |
| **Ohm yasası** | Ohm's law | V = I·R: gerilim, akım ve direnç ilişkisi | O2 |
| **LiPo, "S" sayısı** | LiPo, cell count | Lityum polimer batarya. 3S = 3 hücre seri = 11.1 V nominal | O2 |
| **C-oranı** | C-rating | Bataryanın sürekli verebileceği akımın kapasiteye oranı (30C × 2.2 Ah = 66 A) | O2 |
| **Regülatör (BEC, DC-DC)** | Regulator | Yüksek gerilimden mantık devreleri için 5 V veya 3.3 V üreten devre | O2 |
| **Dal (branch)** | Branch | Git'te ana koddan ayrılıp bağımsız çalışılan kopya | O3 |
| **Birleştirme isteği (PR)** | Pull request | Bir dalın ana koda eklenmesi için yapılan, incelenip onaylanan istek | O3 |
| **Sanal ortam** | Virtual environment | Projeye özel Python paketleri klasörü (`venv`) | O3 |
| **Yükselme zamanı** | Rise time | Yanıtın %10'dan %90'a çıkma süresi | O4 |
| **Aşım** | Overshoot | Yanıtın hedefi yüzde kaç geçtiği | O4 |
| **Yerleşme zamanı** | Settling time | Yanıtın ±%2 bandına girip bir daha çıkmadığı an | O4 |
| **Kaskad döngü** | Cascade loop | İç içe akım → hız → konum kontrol döngüleri | O4 |
| **colcon** | colcon | ROS 2 paketlerini derleyen araç (`colcon build`) | O5 |
| **Launch dosyası** | Launch file | Birden çok ROS düğümünü ayarlarıyla tek komutla başlatan dosya | O5 |
| **TF** | Transform tree | ROS'ta bütün koordinat çerçevelerinin "kim kime göre nerede" ağacı | O5 |
| **rosbag** | rosbag | ROS konularını kaydedip aynı zamanlamayla yeniden oynatan araç | O5 |
| **RMSE** | Root mean square error | Hatanın karelerinin ortalamasının karekökü. Büyük hataları daha çok cezalandırır | O6 |
| **Tekrarlanabilirlik** | Repeatability | Aynı hareket tekrarlandığında sonuçların ne kadar tutarlı olduğu (std) | O6 |
| **Çıkış kriteri** | Exit criterion | Bir işin "bitti" sayılması için önceden yazılmış, ölçülebilir koşul | O7 |
| **Gereksinim** | Requirement | Sistemin ne yapması gerektiğini tek, ölçülebilir ve test edilebilir biçimde söyleyen cümle | O7 |
---
[🏠 Ana sayfa](README.md) · [🎮 İnteraktif laboratuvar](interaktif.html) · [📚 Kaynakça](KAYNAKLAR.md)
