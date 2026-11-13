# O5 · ROS 2 Temelleri

> 📋 **Syllabus:** O5 · **Dönem:** P3 (30 Kasım – 6 Aralık) · **Tahmini süre:** 8 saat · **Kimler:** tüm ekip, öncelik Kişi 4 ve Kişi 5 · **Çıktı:** Basit bir yayıncı/abone paketi ve launch dosyası (Git deposunda) · **Paket:** [`ros2/kol_ornek/`](https://github.com/hamzasvr3030-dotcom/robot-manipulator/tree/main/ros2/kol_ornek)

> ### 🎯 Kısaca
> ROS 2, robot yazılımını **küçük programlara (düğüm/node)** böler. Bu programlar birbirleriyle **mesajlarla** konuşur:
> - Kamera düğümü görüntü **yayınlar**.
> - Algılama düğümü bu görüntüye **abone olur**.
> - Planlayıcıya "şuraya git" **aksiyonu** gönderilir.
>
> Bu sayfada temel kavramları, bir çalışma alanının (workspace) nasıl kurulduğunu ve robot kol için yazılmış örnek paketi göreceksin.

> 🧠 **Benzetme:**
> - **Topic (konu)**, bir radyo kanalıdır. Yayıncı yayın yapar, dinlemek isteyen kanalı açar, istediği kadar dinleyici olabilir.
> - **Service**, telefonla soru sorup cevap almaktır.
> - **Action**, kargo takibi gibidir: Uzun süren bir iştir, arada "yolda" bilgisi gelir ve iş iptal edilebilir.
> - **TF**, bütün parçaların "kim kime göre nerede" bilgisini tutan bir **aile ağacıdır**.

## O5.1 Temel kavramlar

| Kavram | Açıklama | Robot kol örneği |
|---|---|---|
| **Düğüm (node)** | Tek işi olan program | `robot_state_publisher`, `move_group`, kamera sürücüsü |
| **Konu (topic)** + yayıncı/abone | Sürekli veri akışı, bire-çok | `/joint_states` (`sensor_msgs/JointState`) |
| **Servis** | İstek ve yanıt | Tutucuyu aç/kapat |
| **Aksiyon** | Uzun süren ve geri bildirim veren görev | `FollowJointTrajectory`: "Bu yörüngeyi izle" |
| **Parametre** | Düğüm ayarı | `frekans_hz`, `robot_description` |
| **Launch dosyası** | Birçok düğümü ayarlarıyla tek komutla başlatır | `display.launch.py` |
| **colcon çalışma alanı** | Paketlerin derlendiği klasör (`src/`, `build/`, `install/`) | `~/kol_ws` |
| **TF** | Koordinat çerçevelerinin ağacı | `world → base_link → link1 → link2 → link3 → tool0` |
| **rosbag** | Konuları kaydedip sonra aynen oynatır | Deney verisini saklamak (O6) |
| **URDF** | Robotun XML tarifi | [`urdf/rrr_kol.urdf`](../urdf/rrr_kol.urdf) (Konu 8) |

## O5.2 Çalışma alanı kurulumu ve örnek paket

Bu depodaki [`ros2/kol_ornek`](https://github.com/hamzasvr3030-dotcom/robot-manipulator/tree/main/ros2/kol_ornek) paketinde iki düğüm var:
- **`yayinci`**: Kolun eklem açılarını 10 Hz ile `ornek/eklem_durumu` konusuna yayınlar.
- **`abone`**: Bu açıları dinler, **Konu 2'deki düz kinematikle** uç konumunu hesaplar ve `ornek/uc_konumu` konusuna yayınlar.

```bash
# 1) Çalışma alanını oluştur ve paketi içine kopyala
mkdir -p ~/kol_ws/src && cd ~/kol_ws/src
cp -r <bu-depo>/ros2/kol_ornek .

# 2) Derle ve ortamı yükle
cd ~/kol_ws
source /opt/ros/jazzy/setup.bash
colcon build --packages-select kol_ornek
source install/setup.bash

# 3) İki düğümü launch dosyasıyla birlikte başlat
ros2 launch kol_ornek ornek.launch.py
#   Her saniye bir satır yazılır:  [uc_hesaplayici]: q = (q1, q2, q3)°  →  uç = (x, y) m

# 4) Başka bir terminalde incele
ros2 node list                         # /eklem_yayinci, /uc_hesaplayici
ros2 topic list                        # /ornek/eklem_durumu, /ornek/uc_konumu
ros2 topic echo /ornek/uc_konumu       # uç konumu mesajları
ros2 topic hz /ornek/eklem_durumu      # ≈ 10 Hz
ros2 param set /eklem_yayinci frekans_hz 20.0   # yalnızca başlangıçta okunur: yeniden başlatınca etkili olur
rqt_graph                              # düğüm–konu bağlantı şeması
```

**Yayıncının çekirdeği** ([`yayinci.py`](https://github.com/hamzasvr3030-dotcom/robot-manipulator/blob/main/ros2/kol_ornek/kol_ornek/yayinci.py)):

```python
self.pub = self.create_publisher(JointState, "ornek/eklem_durumu", 10)   # konu adı, kuyruk boyu
self.create_timer(self.dt, self.yayinla)                                  # periyodik çağrı
...
msg.name = ["joint1", "joint2", "joint3"]
msg.position = [q1, q2, q3]            # radyan
self.pub.publish(msg)
```

**Abonenin çekirdeği** ([`abone.py`](https://github.com/hamzasvr3030-dotcom/robot-manipulator/blob/main/ros2/kol_ornek/kol_ornek/abone.py)):

```python
self.create_subscription(JointState, "ornek/eklem_durumu", self.geldi, 10)
def geldi(self, msg):                 # her mesajda çağrılır
    x, y = duz_kinematik(msg.position)
```

> ℹ️ Paket ROS 2'nin `ament_python` yapısına uygun yazıldı ve Python sözdizimi kontrol edildi. Ancak ROS 2 kurulu bir makinede **derlenip çalıştırılmadı**. İlk kurulumda bir sorun çıkarsa hata mesajıyla birlikte ekibe bildirin.

## O5.3 TF: koordinat çerçeveleri ağacı

```text
world
 └── base_link            (taban)
      └── link1            joint1 (q1)
           └── link2       joint2 (q2)
                └── link3  joint3 (q3)
                     └── tool0   (uç efektör, sabit)
                          └── camera_link?   (el-göz kalibrasyonundan gelir, Konu 9)
```

- `robot_state_publisher`, URDF ve `/joint_states` bilgisinden bu ağacı sürekli yayınlar.
- Ağacı görmek için: `ros2 run tf2_tools view_frames` (bir PDF üretir).
- İki çerçeve arasındaki anlık dönüşümü görmek için: `ros2 run tf2_ros tf2_echo base_link tool0`.

## O5.4 rosbag: kaydet ve tekrar oynat

```bash
ros2 bag record -o deney_2026_12_08 /joint_states /ornek/uc_konumu   # kaydet (Ctrl+C ile bitir)
ros2 bag info deney_2026_12_08                                       # içerik ve süre
ros2 bag play deney_2026_12_08                                       # aynı mesajları aynı zamanlamayla yeniden yayınla
```

## ✍️ Kendini sına (syllabus soruları)

<details>
<summary><b>1.</b> Hız komutu hangi konuya ve hangi mesaj tipiyle gönderilir?</summary>
<br>
Mobil robotlarda (rover, otonom araç) genellikle <code>/cmd_vel</code> konusuna <code>geometry_msgs/Twist</code> mesajı gönderilir. Bu mesaj doğrusal ve açısal hızı taşır.<br><br>
<b>Robot kolda karşılığı farklıdır:</b> Kol "hızla" değil, <b>eklem yörüngesiyle</b> sürülür. MoveIt ve <code>ros2_control</code>, <code>joint_trajectory_controller</code>'a <code>control_msgs/action/FollowJointTrajectory</code> aksiyonu gönderir. Bu aksiyon, zaman damgalı eklem konumları içeren bir <code>trajectory_msgs/JointTrajectory</code> taşır. Doğrudan hız kontrolü gerekirse <code>std_msgs/Float64MultiArray</code> ile bir hız denetleyicisi de kullanılabilir.
</details>
<details>
<summary><b>2.</b> rosbag ile kaydedilen veri neden tekrar oynatılabilir olmalıdır?</summary>
<br>
Gerçek deney pahalıdır ve tekrar etmek zordur. Kayıt tekrar oynatılabilirse:
<ul>
<li>Algoritma (filtre, algılama, kontrol analizi) <b>aynı veriyle</b> defalarca denenebilir, iki sürüm adil şekilde karşılaştırılabilir.</li>
<li>Hata <b>yeniden üretilip</b> ayıklanabilir.</li>
<li>Robot ya da laboratuvar olmadan da çalışılabilir.</li>
</ul>
Bunun için kayda zaman damgaları, TF (<code>/tf</code>, <code>/tf_static</code>) ve gerekli bütün konular dahil edilmeli, kullanılan parametreler ve sürümler de not edilmelidir.
</details>
<details>
<summary><b>3.</b> TF ağacında bir çerçeve eksikse hangi sorun çıkar?</summary>
<br>
O çerçeveye bağlı hiçbir dönüşüm hesaplanamaz:
<ul>
<li>RViz modeli veya sensör verisini gösteremez.</li>
<li>Düğümler <i>"Could not transform … frame does not exist"</i> hatası verir.</li>
<li>MoveIt planlama yapamaz.</li>
<li>Kamerada görülen bir nesne robot koordinatına çevrilemez (Konu 9).</li>
</ul>
Ağaç tek bir kökten kopmadan ilerlemelidir. Her çerçevenin tek bir ebeveyni olur.
</details>

## ⚡ Akılda kalsın
- **Düğüm** = program. **Konu** = sürekli veri. **Servis** = soru-cevap. **Aksiyon** = uzun görev. **Parametre** = ayar.
- Çalışma alanı: `src/` → `colcon build` → `source install/setup.bash`.
- **TF** ağacı tek köklü olmalı, kopuk çerçeve olmamalıdır.
- **rosbag** = deneyi şişeye koymak: Aynı veriyle tekrar tekrar test edilir.

## Kaynaklar
[13] ROS 2 Dokümantasyonu · [14] URDF eğitimleri · [16] Macenski vd. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)

---
[← O4 · Kontrol ve PID](o4-kontrol-pid.md) · [🏠 Ana sayfa](../README.md) · [📖 Sözlük](../SOZLUK.md) · [O6 · Simülasyon ve veri →](o6-simulasyon-veri.md)
