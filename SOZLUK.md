# 📖 Terimler Sözlüğü

Sayfalarda geçen teknik terimlerin kısa ve sade açıklamaları. Parantez içindeki numara, terimin ayrıntılı anlatıldığı konuyu gösterir.

| Terim | İngilizcesi | Ne demek? (sade) | Konu |
|---|---|---|---|
| **Manipülatör** | Manipulator | Eklemlerle birbirine bağlı uzuvlardan oluşan robot kol | 0 |
| **Uzuv** | Link | Kolun iki eklem arasındaki katı parçası, yani "kemiği" | 0 |
| **Eklem** | Joint | Uzuvları birbirine bağlayan hareketli bağlantı, yani "omuz" veya "dirsek" | 0 |
| **Döner eklem (R)** | Revolute | Bir eksen etrafında dönen eklem. Kapı menteşesi gibi | 0 |
| **Kayar eklem (P)** | Prismatic | Bir doğru boyunca kayan eklem. Çekmece gibi | 0 |
| **Serbestlik derecesi (DOF)** | Degrees of freedom | Kolun yapabildiği bağımsız hareketlerin sayısı | 0 |
| **Uç efektör** | End-effector | Kolun ucundaki işi yapan parça: tutucu, torç, vantuz vb. | 0 |
| **Çalışma uzayı** | Workspace | Kolun ucunun uzanabildiği bütün noktalar | 0 |
| **Poz** | Pose | Konum + yönelim birlikte. "Nerede ve hangi yöne bakıyor?" | 1 |
| **Homojen dönüşüm** | Homogeneous transform | Dönme ve taşıma bilgisini tek bir 4×4 tabloda tutan matris | 1 |
| **DH parametreleri** | Denavit–Hartenberg | Her eklemi 4 sayıyla tarif eden standart yöntem | 1 |
| **Düz kinematik** | Forward kinematics | Açılar biliniyor → uç nerede? | 1 |
| **Jacobian** | Jacobian | Eklem hızlarını uç hızına çeviren matris. "Eklemi biraz oynatırsam uç ne kadar oynar?" | 1 |
| **Tekillik** | Singularity | Kolun bir yönde hareket edemediği "kilitli" konum. Örneğin kol tamamen açıkken | 1 |
| **Ters kinematik (IK)** | Inverse kinematics | Uç şurada olmalı → açılar ne olmalı? | 2 |
| **Analitik çözüm** | Closed-form | Formülle doğrudan bulunan cevap | 2 |
| **Sayısal çözüm** | Numerical | Bir tahminle başlayıp adım adım yaklaşarak bulunan cevap | 2 |
| **DLS** | Damped least squares | Tekilliğe yakın konumlarda bile kararlı çalışan sayısal IK yöntemi | 2 |
| **Yol** | Path | Sadece geometri: hangi noktalardan geçileceği | 3 |
| **Yörünge** | Trajectory | Yol + zaman: her an konum, hız ve ivme | 3 |
| **Quintic polinom** | Quintic | Başta ve sonda hızı ve ivmesi sıfır olan, sarsıntısız hareket eğrisi | 3 |
| **Sarsıntı** | Jerk | İvmenin değişim hızı. Yüksek olursa titreşim yaratır | 3 |
| **Tork** | Torque | Döndürme kuvveti = kuvvet × kaldıraç uzunluğu [N·m] | 4 |
| **Redüktör** | Gearbox / reducer | Hızı düşürüp torku artıran dişli kutusu. Bisiklet vitesi gibi | 4 |
| **Çevrim oranı (N)** | Gear ratio | Redüktörün hızı kaç kat düşürdüğü | 4 |
| **Boşluk** | Backlash | Dişliler arasındaki küçük oynama payı. Hassasiyeti bozar | 4 |
| **Atalet** | Inertia | Bir cismin dönmeye karşı direnci [kg·m²] | 4 |
| **BLDC** | Brushless DC | Fırçasız motor: güçlü, verimli ve sessiz, ama sürücüsü karmaşık | 4 |
| **Step motor** | Stepper | Adım adım dönen ve enkodersiz konumlanabilen motor | 4 |
| **Enkoder** | Encoder | Motorun açısını ölçen sensör, yani robotun "gözü" | 5 |
| **Kapalı çevrim** | Closed loop | Ölç → karşılaştır → düzelt döngüsü | 5 |
| **PID** | PID | Hatanın şimdiki değerine (P), birikimine (I) ve değişim hızına (D) göre düzeltme yapan kontrolcü | 5 |
| **Kalıcı hata** | Steady-state error | Sistem durduktan sonra da kalan küçük hata | 5 |
| **Integral şişmesi** | Windup | Motor doymadayken integral teriminin gereksiz yere büyümesi | 5 |
| **Tutucu** | Gripper | Robotun "eli" | 6 |
| **Sürtünme katsayısı (μ)** | Friction coefficient | Yüzeylerin birbirinden ne kadar kolay kaydığını gösteren sayı | 6 |
| **ROS 2** | Robot Operating System 2 | Robot programlarının birbirleriyle konuştuğu ortak yazılım altyapısı | 7 |
| **Node / Topic / Service / Action** | — | Program / sürekli veri yayını / soru-cevap / uzun süren görev | 7 |
| **URDF** | Unified Robot Description Format | Robotun XML biçimindeki teknik tarifi: parçalar + eklemler | 7 |
| **MoveIt 2** | MoveIt 2 | Çarpışmasız hareket planlayan ROS 2 aracı. Robotun "GPS'i" | 7 |
| **RViz** | RViz | ROS'un 3B görselleştirme programı | 7 |
| **İç parametreler (K)** | Intrinsics | Kameranın odak uzaklığı ve görüntü merkezi. Pikseli metreye çevirmeye yarar | 8 |
| **El-göz kalibrasyonu** | Hand-eye calibration | Kameranın robota göre nerede durduğunu bulma işlemi | 8 |
| **Eşikleme** | Thresholding | Belirli bir renk aralığındaki pikselleri seçme | 8 |
| **Risk değerlendirmesi** | Risk assessment | Tehlikeleri bulma, büyüklüklerini tahmin etme ve önlem belirleme | 9 |
| **Acil durdurma** | Emergency stop (e-stop) | Robotu donanımla durduran mantar başlı kırmızı buton | 9 |
| **Stop 0 / 1 / 2** | Stop categories | 0: hemen güç kes · 1: önce yavaşla, sonra güç kes · 2: dur ama güç kalsın | 9 |
| **LOTO** | Lockout/Tagout | Bakım öncesi enerji kaynağını kilitleme ve etiketleme | 9 |

---
[🏠 Ana sayfa](README.md) · [🎮 İnteraktif kol](interaktif.html) · [📚 Kaynakça](KAYNAKLAR.md)
