"""
Konu 5 — Tek eklem PID konum kontrolü simülasyonu.

Model (redüktör sonrası eklem tarafı):
    J*q'' + b*q' + m*g*l*cos(q) = tau      ,  |tau| <= tau_maks
Enkoder: 4096 adım/tur (kuantalama), kontrol periyodu 1 ms.
Referans: 0° -> 60° quintic yörünge (2 s) + 3 s bekleme.
P, PD ve PID (anti-windup'lı, türev filtreli) karşılaştırılır.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

CIKTI = Path(__file__).resolve().parent.parent / "gorseller"

J, b = 0.08, 0.15            # atalet [kg·m²], viskoz sürtünme [N·m·s/rad]
mgl = 0.9 * 9.81 * 0.20      # yerçekimi momenti katsayısı [N·m]
tau_maks = 12.0              # motor+redüktörün verebileceği maks tork [N·m]
enk_cozunurluk = 2 * np.pi / 4096
dt, T_son = 0.001, 5.0
t = np.arange(0, T_son, dt)

# Referans yörünge (quintic, 0 -> 60°)
Th, q_son = 2.0, np.radians(60)
tau_n = np.clip(t / Th, 0, 1)
q_ref = q_son * (10 * tau_n**3 - 15 * tau_n**4 + 6 * tau_n**5)


def simule(Kp, Ki, Kd):
    q, qd, integral, e_onceki, turev = 0.0, 0.0, 0.0, 0.0, 0.0
    a = dt / (0.005 + dt)            # türev için 1. derece alçak geçiren filtre (5 ms)
    Q, U = np.zeros_like(t), np.zeros_like(t)
    for k in range(len(t)):
        q_olcum = np.round(q / enk_cozunurluk) * enk_cozunurluk  # enkoder kuantalaması
        e = q_ref[k] - q_olcum
        if k:
            turev += a * ((e - e_onceki) / dt - turev)  # filtrelenmiş türev
        u_ham = Kp * e + Ki * integral + Kd * turev
        u = np.clip(u_ham, -tau_maks, tau_maks)
        if u == u_ham:                 # anti-windup: doymada integrali dondur
            integral += e * dt
        e_onceki = e
        qdd = (u - b * qd - mgl * np.cos(q)) / J
        qd += qdd * dt
        q += qd * dt                   # yarı-örtük Euler
        Q[k], U[k] = q, u
    return Q, U


kazanclar = {"P   (Kp=60)": (60, 0, 0),
             "PD  (Kp=60, Kd=4)": (60, 0, 4),
             "PID (Kp=60, Ki=150, Kd=4)": (60, 150, 4)}
renk = ["#C44E52", "#DD8452", "#4C72B0"]
fig, ax = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
ax[0].plot(t, np.degrees(q_ref), "k--", lw=1.5, label="referans")
for (ad, K), c in zip(kazanclar.items(), renk):
    Q, U = simule(*K)
    e = np.degrees(q_ref - Q)
    print(f"{ad:28s}  maks |hata| = {np.abs(e).max():6.2f}°   "
          f"sürekli hal hatası = {e[-1]:+.3f}°   maks tork = {np.abs(U).max():.2f} N·m")
    ax[0].plot(t, np.degrees(Q), color=c, label=ad)
    ax[1].plot(t, e, color=c)
    ax[2].plot(t, U, color=c)
ax[0].set_ylabel("q [°]"); ax[0].legend(fontsize=8); ax[0].set_title("Eklem konum takibi")
ax[1].set_ylabel("hata [°]"); ax[1].axhline(0, color="k", lw=0.5)
ax[2].set_ylabel("tork [N·m]"); ax[2].set_xlabel("t [s]")
ax[2].axhline(tau_maks, color="gray", ls=":"); ax[2].axhline(-tau_maks, color="gray", ls=":")
for a in ax: a.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(CIKTI / "05_pid.png", dpi=130)
