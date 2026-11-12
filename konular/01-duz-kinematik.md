# 1 · Düz Kinematik: Dönüşüm Matrisleri ve DH Parametreleri

> **Çıktı türü:** Hesap · **Kod:** [`kod/k01_duz_kinematik.py`](../kod/k01_duz_kinematik.py), [`kod/robot_kol.py`](../kod/robot_kol.py)

**Düz kinematik:** Eklem açıları $q$ verildiğinde uç efektörün konumunu ve yönelimini bulma problemidir. Çözümü her zaman vardır ve tektir.

## 1.1 Homojen dönüşüm matrisi

Bir çerçevenin başka bir çerçeveye göre **dönmesi** ($R$, 3×3) ve **ötelenmesi** ($p$, 3×1) tek bir 4×4 matriste birleştirilir [1, Bölüm 2], [3, Bölüm 3]:

```math
{}^{A}T_{B} = \begin{bmatrix} R & p \\ 0\;0\;0 & 1 \end{bmatrix},
\qquad
{}^{A}T_{C} = {}^{A}T_{B}\;{}^{B}T_{C}
```

Dönüşümler zincir boyunca **çarpılarak** birleşir. Örneğin $z$ ekseni etrafında $\theta$ kadar dönme:

```math
R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
```

## 1.2 Denavit–Hartenberg (DH) gösterimi

Denavit ve Hartenberg [6], ardışık iki eklem çerçevesi arasındaki dönüşümü **4 parametreyle** ifade etmeyi önerdi. Bu yöntemde çerçeveler kurallara göre yerleştirilir: $z_i$ eklem eksenidir, $x_i$ iki $z$ ekseninin ortak dikmesidir [2, Bölüm 3.2].

| Parametre | Anlamı |
|---|---|
| $a_i$ | Uzuv uzunluğu: $z_{i-1}$ ile $z_i$ arası, $x_i$ boyunca mesafe |
| $\alpha_i$ | Uzuv bükümü: $z_{i-1}$'den $z_i$'ye, $x_i$ etrafında açı |
| $d_i$ | Eklem kaçıklığı: $z_{i-1}$ boyunca mesafe (P eklemde değişken) |
| $\theta_i$ | Eklem açısı: $z_{i-1}$ etrafında açı (R eklemde değişken) |

Standart DH dönüşümü:

```math
{}^{i-1}T_{i} = R_z(\theta_i)\,T_z(d_i)\,T_x(a_i)\,R_x(\alpha_i) =
\begin{bmatrix}
c\theta_i & -s\theta_i c\alpha_i & s\theta_i s\alpha_i & a_i c\theta_i \\
s\theta_i & c\theta_i c\alpha_i & -c\theta_i s\alpha_i & a_i s\theta_i \\
0 & s\alpha_i & c\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}
```

> ⚠️ Craig [1] **değiştirilmiş (modified) DH** kullanır: Parametrelerin sırası ve indeksleri farklıdır. Sonuç aynı çıkar, ama iki kitaptaki tablolar birbirine karıştırılmamalıdır.

## 1.3 Örnek kolun DH tablosu

| $i$ | $a_i$ [m] | $\alpha_i$ | $d_i$ | $\theta_i$ |
|---|---|---|---|---|
| 1 | 0.30 | 0 | 0 | $q_1$ |
| 2 | 0.25 | 0 | 0 | $q_2$ |
| 3 | 0.10 | 0 | 0 | $q_3$ |

Matrisler çarpılınca kapalı form elde edilir. Kısaltmalar: $c_{12} = \cos(q_1+q_2)$, $s_{123} = \sin(q_1+q_2+q_3)$ vb.

```math
x = L_1 c_1 + L_2 c_{12} + L_3 c_{123},\qquad
y = L_1 s_1 + L_2 s_{12} + L_3 s_{123},\qquad
\varphi = q_1 + q_2 + q_3
```

## 1.4 Hesap: $q = (30°,\,45°,\,-30°)$

Program çıktısı (`python kod/k01_duz_kinematik.py`):

```text
0_T_1 =                                1_T_2 =
[[ 0.866  -0.5     0.      0.2598]     [[ 0.7071 -0.7071  0.      0.1768]
 [ 0.5     0.866   0.      0.15  ]      [ 0.7071  0.7071  0.      0.1768]
 [ 0.      0.      1.      0.    ]      [ 0.      0.      1.      0.    ]
 [ 0.      0.      0.      1.    ]]     [ 0.      0.      0.      1.    ]]

2_T_3 =                                0_T_3 = 0_T_1 · 1_T_2 · 2_T_3 =
[[ 0.866   0.5     0.      0.0866]     [[ 0.7071 -0.7071  0.      0.3952]
 [-0.5     0.866   0.     -0.05  ]      [ 0.7071  0.7071  0.      0.4622]
 [ 0.      0.      1.      0.    ]      [ 0.      0.      1.      0.    ]
 [ 0.      0.      0.      1.    ]]     [ 0.      0.      0.      1.    ]]

Uç efektör konumu: x = 0.3952 m, y = 0.4622 m, phi = 45.0°
Kapalı form kontrol: x = 0.3952 m, y = 0.4622 m  (fark: 5.6e-17)
```

**Elle doğrulama:**
- $x = 0.30\cos 30° + 0.25\cos 75° + 0.10\cos 45° = 0.2598 + 0.0647 + 0.0707 = 0.3952$ m ✔
- $y = 0.30\sin 30° + 0.25\sin 75° + 0.10\sin 45° = 0.1500 + 0.2415 + 0.0707 = 0.4622$ m ✔
- $\varphi = 30 + 45 - 30 = 45°$. Bu sonuç $0T_3$'ün dönme bloğunda da görülüyor: $\cos 45° = 0.7071$ ✔

![Düz kinematik](../gorseller/01_duz_kinematik.png)

## 1.5 Jacobian (sonraki konular için)

Eklem hızlarını uç hızlarına bağlayan matris $\dot{\mathbf{x}} = J(q)\,\dot{q}$ ile tanımlanır [2, Bölüm 4]:

```math
J(q) = \begin{bmatrix}
-(L_1 s_1 + L_2 s_{12} + L_3 s_{123}) & -(L_2 s_{12} + L_3 s_{123}) & -L_3 s_{123} \\
L_1 c_1 + L_2 c_{12} + L_3 c_{123} & L_2 c_{12} + L_3 c_{123} & L_3 c_{123} \\
1 & 1 & 1
\end{bmatrix}
```

$\det J = L_1 L_2 \sin q_2$ olduğu için $q_2 = 0$ veya $q_2 = \pm 180°$ konumlarında kol **tekil (singular)** olur. Bu konumlarda kol tam açılmış ya da kendi üzerine katlanmıştır ve bazı yönlerde hareket edemez. $J$ aynı zamanda statik kuvvet ilişkisini de verir: $\tau = J^{T} F$ [3, Bölüm 5].

## Kaynaklar
[1] Craig · [2] Spong vd. · [3] Lynch & Park · [6] Denavit & Hartenberg. Tam künyeler: [KAYNAKLAR.md](../KAYNAKLAR.md)
