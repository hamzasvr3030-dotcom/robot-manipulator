# 7 · Yazılım: URDF, ROS 2, MoveIt 2 Temelleri, Python

> **Çıktı türü:** Depo · **Dosyalar:** [`urdf/rrr_kol.urdf`](../urdf/rrr_kol.urdf), [`ros2/display.launch.py`](../ros2/display.launch.py), [`ros2/moveit_hareket.py`](../ros2/moveit_hareket.py)

> ### 🎯 Kısaca
> Gerçek bir robot yazılımı tek bir programdan oluşmaz. Kamera, planlayıcı, motor sürücüsü gibi **birçok küçük program** birbirleriyle konuşur.
> - **ROS 2:** Bu programların konuştuğu **ortak dil ve posta sistemi**dir.
> - **URDF:** Robotun **teknik resmidir**.
> - **MoveIt 2:** Robotun **GPS'i** gibidir: Çarpışmadan gidilecek rotayı hesaplar.

> 🧠 **Benzetme — ROS 2'nin haberleşme yolları:**
>
> | ROS kavramı | Günlük hayatta | Örnek |
> |---|---|---|
> | **Topic** | Radyo yayını: Yayıncı yayın yapar, dinlemek isteyen frekansı açar | Eklem açıları sürekli yayınlanır |
> | **Service** | Telefonla soru sorup cevap almak | "Tutucuyu kapat" → "Tamam" |
> | **Action** | Kargo takibi: İş uzun sürer, arada "yolda" bilgisi gelir, istersen iptal edersin | "Şu poza git" |

## 7.1 ROS 2 nedir?

**ROS 2 (Robot Operating System 2)** bir işletim sistemi değil, robot yazılımı için bir **ara katman (middleware)** ve araç ekosistemidir [13], [16]. Temel kavramları:

| Kavram | Açıklama | Örnek |
|---|---|---|
| **Node** | Tek bir iş yapan program | Kamera sürücüsü, IK çözücü |
| **Topic** | Yayınla/abone ol mantığıyla çalışan sürekli veri akışı | `/joint_states`, `/camera/image_raw` |
| **Service** | İstek/yanıt mantığıyla çalışan tek seferlik çağrı | "Tutucuyu kapat" |
| **Action** | Uzun süren, geri bildirim veren ve iptal edilebilen görev | "Şu poza git" |
| **Parameter** | Node ayarı | `robot_description` |
| **TF2** | Çerçeveler arası dönüşüm ağacı | `world → base_link → … → tool0` |

ROS 2, haberleşme katmanı olarak **DDS** kullanır. Kurulum için önerilen ortam: **Ubuntu 24.04 + ROS 2 Jazzy** (LTS) [13].

## 7.2 URDF — robotun tarifi

**URDF (Unified Robot Description Format)**, robotu XML ile tanımlar. Bir robot **link**'lerden (uzuvlar: görsel, çarpışma ve atalet bilgileri) ve **joint**'lerden (eklemler: tip, eksen, sınırlar) oluşur [14].

Bu depodaki [`urdf/rrr_kol.urdf`](../urdf/rrr_kol.urdf) dosyası, `kod/robot_kol.py` ile **aynı kolu** tanımlar. Kütleler de Konu 4'teki girdilerle aynıdır.

```xml
<joint name="joint2" type="revolute">
  <parent link="link1"/><child link="link2"/>
  <origin xyz="0.30 0 0"/>          <!-- L1: bir önceki eklemden uzaklık -->
  <axis xyz="0 -1 0"/>              <!-- y ekseni etrafında; + açı kolu kaldırır -->
  <limit lower="-2.618" upper="2.618" effort="8" velocity="2.09"/>  <!-- ±150° -->
</joint>
```

| | DH (Konu 1) | URDF |
|---|---|---|
| Parametre | 4 parametre, katı kurallar | Her eklem için serbest `origin xyz rpy` + `axis` |
| Amaç | Kinematik analiz | Simülasyon, görselleştirme, planlama |

Büyük projelerde URDF doğrudan yazılmaz, **xacro** makrolarıyla üretilir.

## 7.3 Modeli RViz'de görmek

```bash
# Ubuntu 24.04 + ROS 2 Jazzy
sudo apt install ros-jazzy-robot-state-publisher ros-jazzy-joint-state-publisher-gui ros-jazzy-rviz2
source /opt/ros/jazzy/setup.bash
check_urdf urdf/rrr_kol.urdf          # sözdizimi ve ağaç kontrolü (liburdfdom-tools)
ros2 launch ros2/display.launch.py
```

RViz açıldığında şu ayarları yap:
1. **Fixed Frame** = `world`
2. **Add → RobotModel** ekle ve Description Topic olarak `/robot_description` seç.
3. Açılan kaydırıcılarla eklemleri oynat.

## 7.4 MoveIt 2 ile hareket planlama

**MoveIt 2**, ROS 2'nin hareket planlama çatısıdır [15]. Şu işleri yapar:
- IK (KDL, TRAC-IK, pick_ik)
- Çarpışma denetimi (FCL)
- Planlayıcılar (OMPL, Pilz, STOMP, CHOMP)
- Yörünge zaman parametrelemesi (TOTG / Ruckig)
- `ros2_control` ile yürütme

**Adımlar:**

1. **Setup Assistant** ile yapılandırma paketini üret:
   ```bash
   sudo apt install ros-jazzy-moveit
   ros2 launch moveit_setup_assistant setup_assistant.launch.py
   ```
   - URDF olarak `urdf/rrr_kol.urdf` dosyasını yükle.
   - *Self-Collisions* matrisini üret.
   - *Planning Group* tanımla: ad `arm`, Kinematic Chain `base_link → tool0`, Solver `KDL`.
   - *Robot Poses* bölümünde `hazir` adlı bir poz tanımla (örneğin q = 0°, 90°, −90°).
   - Paketi `rrr_kol_moveit_config` adıyla kaydet.

2. **3 DOF'luk kol için önemli ayar:** Kol 6 serbestlikli bir pozu tam sağlayamaz. Bu yüzden `config/kinematics.yaml` dosyasında `position_only_ik: true` ayarı yapılmalı, ya da hedef poz kolun x–z düzleminde verilmelidir.

3. **Demoyu çalıştır:** RViz'deki *MotionPlanning* panelinde hedef pozu sürükle, **Plan** ve **Execute** butonlarına bas.
   ```bash
   colcon build && source install/setup.bash
   ros2 launch rrr_kol_moveit_config demo.launch.py
   ```

4. **Python ile planlama:** [`ros2/moveit_hareket.py`](../ros2/moveit_hareket.py) dosyası `moveit_py` (MoveItPy) API'siyle önce `hazir` pozuna, sonra kartezyen bir hedefe plan yapıp yürütür. Bu betiği çalıştırmak için MoveIt'in resmî *MoveIt Python API* eğitimindeki launch yapısı gerekir [15].

> ℹ️ ROS 2 ve MoveIt dosyaları bu depoda resmî dokümantasyona göre yazıldı, ancak ROS kurulu bir makinede **test edilmedi**. URDF'nin XML yapısı ve eklem zinciri Python ile doğrulandı.

## 7.5 ROS'suz Python ile çalışmak

Bu depodaki `kod/` klasörü yalnızca **numpy ve matplotlib** kullanır. Daha kapsamlı çalışmalar için şu kütüphaneler kullanılabilir:
- **Robotics Toolbox for Python** (Corke): DH/URDF modelleri, IK, yörünge, Swift ve PyPlot görselleştirme [5]
- **Modern Robotics kütüphanesi** (Lynch & Park): Kitaptaki algoritmaların doğrudan karşılıkları [3]
- **PyBullet / MuJoCo**: URDF yükleyen fizik simülasyonu

## ⚡ Akılda kalsın
- **Node** = tek bir iş yapan program. **Topic** = sürekli akan veri. **Service** = soru-cevap. **Action** = uzun süren görev.
- **URDF** = link'ler (parçalar) + joint'ler (eklemler). Bu depodaki URDF dosyası Python modeliyle **aynı kolu** tanımlar.
- **MoveIt 2** = IK + çarpışma kontrolü + yol planlama + yürütme, hepsi bir arada.
- Önerilen başlangıç: **Ubuntu 24.04 + ROS 2 Jazzy**. Önce modeli RViz'de aç, sonra MoveIt Setup Assistant'ı çalıştır.

## ✍️ Kendini test et
<details>
<summary><b>Soru:</b> Kameradan saniyede 30 görüntü geliyor. Topic mi, service mi kullanılır?</summary>
<br>
Topic. Veri sürekli akıyor; her görüntü için ayrıca soru sormaya gerek yok.
</details>
<details>
<summary><b>Soru:</b> URDF'de bir eklemin dönme yönünü hangi etiket belirler?</summary>
<br>
<axis xyz="..."/> etiketi. Bu depoda tüm eklemlerde (0, −1, 0) kullanılıyor.
</details>

## Kaynaklar
[3] Lynch & Park · [5] Corke · [13] ROS 2 Dokümantasyonu · [14] URDF eğitimleri · [15] MoveIt 2 Dokümantasyonu · [16] Macenski vd. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← 6 · Tutucu](06-tutucu.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [8 · Algılama →](08-algilama.md)
