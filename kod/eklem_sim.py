"""
eklem_sim.py — Tek eklem konum kontrolü simülatörü (O4, O6 ve Konu 6 için ortak).

Model (redüktör sonrası eklem tarafı):
    J*q'' + b*q' + tau_c*sign(q') + m*g*l*cos(q) = tau,   |tau| <= tau_maks
İsteğe bağlı "gerçek dünya" etkileri: ölçüm gürültüsü, ölçüm/komut gecikmesi,
Coulomb sürtünmesi, enkoder kuantalaması.
"""
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Model:
    J: float = 0.08           # atalet [kg·m²]
    b: float = 0.15           # viskoz sürtünme [N·m·s/rad]
    mgl: float = 0.9 * 9.81 * 0.20   # yerçekimi momenti katsayısı [N·m]
    tau_maks: float = 12.0    # tork sınırı [N·m]
    tau_c: float = 0.0        # Coulomb (kuru) sürtünme [N·m]
    enkoder: int = 4096       # adım/tur (0 = kuantalama yok)
    gurultu: float = 0.0      # ölçüm gürültüsü std [derece]
    gecikme: float = 0.0      # ölçüm gecikmesi [s]


@dataclass
class PID:
    Kp: float = 60.0
    Ki: float = 0.0
    Kd: float = 0.0
    anti_windup: bool = True
    turev_filtre: float = 0.005   # [s], 0 = filtre yok


def referans(t, hedef_derece, tip="quintic", sure=2.0):
    """Referans açı [rad]. tip: 'quintic' (yumuşak) veya 'basamak' (ani)."""
    hedef = np.radians(hedef_derece)
    if tip == "basamak":
        return np.full_like(t, hedef)
    tau = np.clip(t / sure, 0, 1)
    return hedef * (10 * tau**3 - 15 * tau**4 + 6 * tau**5)


def simule(pid: PID, model: Model = None, hedef=60.0, tip="quintic", T=5.0, dt=0.001, tohum=0):
    """Döndürür: dict(t, ref, q, olcum, u) — açılar derece, tork N·m."""
    m = model or Model()
    rng = np.random.default_rng(tohum)
    t = np.arange(0, T, dt)
    r = referans(t, hedef, tip)
    n, gec = len(t), int(round(m.gecikme / dt))
    q = qd = I = e_onceki = D = 0.0
    a = dt / (pid.turev_filtre + dt) if pid.turev_filtre > 0 else 1.0
    Q, OLC, U, gecmis = np.zeros(n), np.zeros(n), np.zeros(n), []
    adim = 2 * np.pi / m.enkoder if m.enkoder else 0
    for k in range(n):
        gecmis.append(q)
        q_olc = gecmis[max(0, k - gec)]
        if adim:
            q_olc = np.round(q_olc / adim) * adim
        q_olc += np.radians(m.gurultu) * rng.standard_normal() if m.gurultu else 0.0
        e = r[k] - q_olc
        if k:
            D += a * ((e - e_onceki) / dt - D)
        u_ham = pid.Kp * e + pid.Ki * I + pid.Kd * D
        u = float(np.clip(u_ham, -m.tau_maks, m.tau_maks))
        if not pid.anti_windup or u == u_ham:
            I += e * dt
        e_onceki = e
        surt = m.tau_c * np.sign(qd) if abs(qd) > 1e-4 else float(np.clip(u - m.mgl * np.cos(q), -m.tau_c, m.tau_c))
        qdd = (u - m.b * qd - surt - m.mgl * np.cos(q)) / m.J
        qd += qdd * dt
        q += qd * dt
        Q[k], OLC[k], U[k] = q, q_olc, u
    return {"t": t, "ref": np.degrees(r), "q": np.degrees(Q), "olcum": np.degrees(OLC), "u": U}


def olcutler(s, hedef=None, bant=0.02):
    """Basamak yanıtı ölçütleri: yükselme (%10→%90), aşım [%], yerleşme (±%2), kalıcı hata, RMSE."""
    t, q, ref = s["t"], s["q"], s["ref"]
    h = hedef if hedef is not None else ref[-1]
    son = q[-int(0.5 / (t[1] - t[0])):].mean()
    try:
        t10 = t[np.argmax(q >= 0.1 * h)]
        t90 = t[np.argmax(q >= 0.9 * h)]
        yuk = t90 - t10 if q.max() >= 0.9 * h else np.nan
    except ValueError:
        yuk = np.nan
    asim = max(0.0, (q.max() - h) / abs(h) * 100)
    disari = np.where(np.abs(q - h) > bant * abs(h))[0]
    yer = t[disari[-1]] if len(disari) else 0.0
    if len(disari) and disari[-1] == len(t) - 1:
        yer = np.nan
    return {"yukselme": yuk, "asim": asim, "yerlesme": yer, "kalici": h - son,
            "rmse": float(np.sqrt(np.mean((ref - q) ** 2))), "maks_tork": float(np.abs(s["u"]).max())}
