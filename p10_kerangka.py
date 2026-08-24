"""Praktikum 10 - Persamaan diferensial biasa.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p10_kerangka.py
"""
import numpy as np

def euler(f, y0, t0, T, n):
    t = np.linspace(t0, T, n+1); h = (T-t0)/n
    y = np.zeros(n+1); y[0] = y0
    for k in range(n):
        # TODO 1a: satu langkah Euler.
        y[k+1] = y[k]
    return t, y

def rk4(f, y0, t0, T, n):
    t = np.linspace(t0, T, n+1); h = (T-t0)/n
    y = np.zeros(n+1); y[0] = y0
    for k in range(n):
        k1 = f(t[k], y[k])
        # TODO 1b: tiga kemiringan sisanya, lalu rata-rata berbobot.
        k2 = k1
        k3 = k1
        k4 = k1
        y[k+1] = y[k] + h*k1
    return t, y

f = lambda t, y: y - t*t + 1.0
tepat = lambda t: (t+1)**2 - 0.5*np.exp(t)
y0, t0, T = 0.5, 0.0, 2.0

print("="*70); print("KEGIATAN 1  Orde Euler dan RK4"); print("="*70)
print(f"{'n':>6} {'galat Euler':>16} {'orde':>7} {'galat RK4':>16} {'orde':>7}")
se = sr = None
for n in (10, 20, 40, 80, 160, 320):
    ge = abs(euler(f, y0, t0, T, n)[1][-1] - tepat(T))
    gr = abs(rk4(f, y0, t0, T, n)[1][-1] - tepat(T))
    oe = np.log2(se/ge) if se else float('nan')
    orr = np.log2(sr/gr) if sr else float('nan')
    print(f"{n:6d} {ge:16.6e} {oe:7.3f} {gr:16.6e} {orr:7.3f}")
    se, sr = ge, gr
print()
print("Biaya sama, mutu berbeda: RK4 memakai 4 evaluasi f tiap langkah.")
for n in (10, 40):
    print(f"  Euler n={4*n:4d} ({4*n} eval) galat={abs(euler(f,y0,t0,T,4*n)[1][-1]-tepat(T)):.3e}")
    print(f"  RK4   n={n:4d} ({4*n} eval) galat={abs(rk4(f,y0,t0,T,n)[1][-1]-tepat(T)):.3e}")

print()
print("="*70); print("KEGIATAN 2  Kekakuan"); print("="*70)
lam = -1000.0
g = lambda t, y: lam*(y - np.cos(t)) - np.sin(t)
g_tepat = lambda t: np.cos(t)
def euler_implisit(y0, t0, T, n):
    t = np.linspace(t0, T, n+1); h = (T-t0)/n
    y = np.zeros(n+1); y[0] = y0
    for k in range(n):
        # y[k+1] = y[k] + h*(lam*(y[k+1]-cos t) - sin t), linear -> langsung
        tb = t[k+1]
        # TODO 2b: Euler implisit, diselesaikan langsung karena linear.
        y[k+1] = y[k]
    return t, y

print(f"lambda = {lam}, selang [0, 3], penyelesaian tepat y = cos t")
print(f"{'n':>7} {'h':>10} {'h*|lambda|':>12} {'Euler eksplisit':>18} {'Euler implisit':>17}")
for n in (100, 500, 1400, 1500, 3000, 6000):
    h = 3.0/n
    te, ye = euler(g, 1.0, 0.0, 3.0, n)
    ti, yi = euler_implisit(1.0, 0.0, 3.0, n)
    ge = np.max(np.abs(ye - g_tepat(te)))
    gi = np.max(np.abs(yi - g_tepat(ti)))
    ge_s = f"{ge:18.3e}" if np.isfinite(ge) else f"{'MELEDAK':>18}"
    print(f"{n:7d} {h:10.5f} {h*abs(lam):12.3f} {ge_s} {gi:17.3e}")
print("\nSyarat kestabilan Euler eksplisit: h*|lambda| < 2, yaitu h < 0.002,")
print(f"artinya n > {3.0/0.002:.0f}. Cocokkan dengan tabel.")

print()
print("="*70); print("KEGIATAN 3  Langkah adaptif"); print("="*70)
def rk45_adaptif(f, y0, t0, T, tol=1e-8, h0=0.1):
    t, y, h = t0, y0, h0
    ts, ys, hs = [t], [y], []
    while t < T:
        h = min(h, T - t)
        # dua langkah setengah lawan satu langkah penuh, ekstrapolasi Richardson
        _, y1 = rk4(f, y, t, t+h, 1)
        _, y2 = rk4(f, y, t, t+h, 2)
        # TODO 3a: taksiran galat dari dua langkah setengah.
        # Nilai nol di bawah membuat setiap langkah diterima, sehingga
        # kerangka ini tetap berhenti sebelum diisi. Ganti dengan rumusnya.
        galat = 0.0
        if galat < tol or h < 1e-12:
            t += h; y = y2[-1] + (y2[-1]-y1[-1])/15
            ts.append(t); ys.append(y); hs.append(h)
        h *= min(2.0, max(0.2, 0.9*(tol/max(galat, 1e-18))**0.2))
    return np.array(ts), np.array(ys), np.array(hs)

f2 = lambda t, y: -2.0*t*y*y                # y' = -2ty^2, y(0)=1 -> y=1/(1+t^2)
tepat2 = lambda t: 1.0/(1.0 + t*t)
ts, ys, hs = rk45_adaptif(f2, 1.0, 0.0, 5.0, tol=1e-8)
print(f"langkah dipakai   : {len(hs)}")
print(f"h terkecil        : {hs.min():.5f} pada t = {ts[np.argmin(hs)]:.3f}")
print(f"h terbesar        : {hs.max():.5f} pada t = {ts[np.argmax(hs)]:.3f}")
print(f"galat maksimum    : {np.max(np.abs(ys - tepat2(ts))):.3e}")
n_seragam = len(hs)
_, yu = rk4(f2, 1.0, 0.0, 5.0, n_seragam)
print(f"RK4 seragam {n_seragam} langkah, galat akhir = "
      f"{abs(yu[-1]-tepat2(5.0)):.3e}")
