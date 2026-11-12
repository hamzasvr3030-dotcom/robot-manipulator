"""
robot_kol.py — Tüm örneklerde kullanılan ortak robot modeli.

Model: Düşey düzlemde çalışan 3 eklemli düzlemsel kol (RRR).
  - x ekseni yatay, y ekseni yukarı (yerçekimi -y yönünde)
  - Tüm eklemler döner (revolute), eksenleri düzleme dik (z)
  - Uç efektör pozu: (x, y, phi)  ->  phi = q1 + q2 + q3

Standart DH parametreleri (Craig/Spong gösterimi):
    i |  a_i  | alpha_i | d_i | theta_i
    1 |  L1   |    0    |  0  |   q1
    2 |  L2   |    0    |  0  |   q2
    3 |  L3   |    0    |  0  |   q3
"""
import numpy as np

# Uzuv boyları [m]
L = (0.30, 0.25, 0.10)

# Eklem sınırları [rad]
Q_MIN = np.radians([-180.0, -150.0, -150.0])
Q_MAX = np.radians([180.0, 150.0, 150.0])


def dh(a, alpha, d, theta):
    """Standart DH homojen dönüşüm matrisi  i-1_T_i."""
    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha), np.sin(alpha)
    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0.0,      sa,       ca,      d],
        [0.0,     0.0,      0.0,    1.0],
    ])


def dh_tablosu(q, L=L):
    """Her eklem için (a, alpha, d, theta) satırları."""
    return [(L[i], 0.0, 0.0, q[i]) for i in range(3)]


def duz_kinematik(q, L=L):
    """
    Düz kinematik. Döndürür: [T0_0, T0_1, T0_2, T0_3] (4x4 matrisler listesi).
    Son eleman uç efektörün taban çerçevesine göre pozudur.
    """
    T = np.eye(4)
    cerceveler = [T.copy()]
    for a, alpha, d, theta in dh_tablosu(q, L):
        T = T @ dh(a, alpha, d, theta)
        cerceveler.append(T.copy())
    return cerceveler


def uc_poz(q, L=L):
    """Uç efektör (x, y, phi)."""
    T = duz_kinematik(q, L)[-1]
    return np.array([T[0, 3], T[1, 3], np.arctan2(T[1, 0], T[0, 0])])


def eklem_konumlari(q, L=L):
    """Çizim için eklem noktaları (4x2): taban, eklem2, eklem3, uç."""
    return np.array([T[:2, 3] for T in duz_kinematik(q, L)])


def jacobian(q, L=L):
    """(x, y, phi) için 3x3 analitik Jacobian."""
    q1, q2, q3 = q
    s1, s12, s123 = np.sin(q1), np.sin(q1 + q2), np.sin(q1 + q2 + q3)
    c1, c12, c123 = np.cos(q1), np.cos(q1 + q2), np.cos(q1 + q2 + q3)
    L1, L2, L3 = L
    return np.array([
        [-(L1 * s1 + L2 * s12 + L3 * s123), -(L2 * s12 + L3 * s123), -L3 * s123],
        [ (L1 * c1 + L2 * c12 + L3 * c123),  (L2 * c12 + L3 * c123),  L3 * c123],
        [1.0, 1.0, 1.0],
    ])


def wrap(a):
    """Açıyı (-pi, pi] aralığına getirir."""
    return (np.asarray(a) + np.pi) % (2 * np.pi) - np.pi


def ters_kinematik_analitik(x, y, phi, L=L, dirsek=+1):
    """
    Analitik (kapalı form) ters kinematik.
    dirsek=+1 -> 'dirsek aşağı' (q2>0), dirsek=-1 -> 'dirsek yukarı' (q2<0)
    Erişilemeyen hedefte ValueError fırlatır.
    """
    L1, L2, L3 = L
    # 1) Bilek noktası: uçtan L3 kadar geri git
    xw = x - L3 * np.cos(phi)
    yw = y - L3 * np.sin(phi)
    # 2) İki uzuvlu kol için kosinüs teoremi
    c2 = (xw**2 + yw**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(c2) > 1.0:
        raise ValueError(f"Hedef çalışma uzayı dışında (cos q2 = {c2:.3f})")
    s2 = dirsek * np.sqrt(1.0 - c2**2)
    q2 = np.arctan2(s2, c2)
    q1 = np.arctan2(yw, xw) - np.arctan2(L2 * s2, L1 + L2 * c2)
    q3 = phi - q1 - q2
    return wrap(np.array([q1, q2, q3]))


def ters_kinematik_sayisal(hedef, q0, L=L, lam=0.01, tol=1e-6, maks_iter=200):
    """
    Sayısal ters kinematik — sönümlü en küçük kareler (Levenberg–Marquardt):
        dq = J^T (J J^T + lam^2 I)^-1 e
    Döndürür: (q, iterasyon_sayisi, hata_gecmisi)
    """
    q = np.array(q0, dtype=float)
    hedef = np.asarray(hedef, dtype=float)
    gecmis = []
    for k in range(maks_iter):
        e = hedef - uc_poz(q, L)
        e[2] = wrap(e[2])
        gecmis.append(np.linalg.norm(e))
        if gecmis[-1] < tol:
            return wrap(q), k, gecmis
        J = jacobian(q, L)
        dq = J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(3), e)
        q = q + dq
    return wrap(q), maks_iter, gecmis
