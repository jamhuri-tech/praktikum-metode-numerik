"""Praktikum 9 - Integrasi numerik.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p09_kerangka.py
"""
import numpy as np
f = lambda x: np.exp(-x*x)
a, b = 0.0, 1.0
from math import erf, sqrt, pi
TEPAT = 0.5*sqrt(pi)*erf(1.0)

def trapesium(f, a, b, n):
    x = np.linspace(a, b, n+1); h = (b-a)/n
    # TODO 1a: aturan trapesium majemuk, tervektor.
    return 0.0

def simpson(f, a, b, n):
    if n % 2: n += 1
    x = np.linspace(a, b, n+1); h = (b-a)/n
    # TODO 1b: aturan Simpson. Bobotnya berselang-seling 4 dan 2.
    return 0.0

print("="*70); print("KEGIATAN 1  Orde trapesium dan Simpson"); print("="*70)
print(f"{'n':>6} {'galat trapesium':>18} {'orde':>7} {'galat Simpson':>16} {'orde':>7}")
st = ss = None
for n in (2, 4, 8, 16, 32, 64, 128):
    gt = abs(trapesium(f, a, b, n) - TEPAT)
    gs = abs(simpson(f, a, b, n) - TEPAT)
    ot = np.log2(st/gt) if st else float('nan')
    os_ = np.log2(ss/gs) if ss else float('nan')
    print(f"{n:6d} {gt:18.6e} {ot:7.3f} {gs:16.6e} {os_:7.3f}")
    st, ss = gt, gs

print()
print("="*70); print("KEGIATAN 2  Romberg"); print("="*70)
def romberg(f, a, b, k):
    R = np.zeros((k, k))
    R[0, 0] = trapesium(f, a, b, 1)
    for i in range(1, k):
        R[i, 0] = trapesium(f, a, b, 2**i)
        for j in range(1, i+1):
            # TODO 2b: ekstrapolasi Richardson.
            R[i, j] = R[i, j-1]
    return R
R = romberg(f, a, b, 6)
print("tabel Romberg, galat mutlak tiap unsur:")
for i in range(6):
    print("  " + " ".join(f"{abs(R[i,j]-TEPAT):11.3e}" if j <= i else " "*11
                          for j in range(6)))
print(f"\nR[5,5] galat = {abs(R[5,5]-TEPAT):.3e}  memakai {2**5+1} evaluasi f")
print(f"trapesium dengan 33 evaluasi galat = {abs(trapesium(f,a,b,32)-TEPAT):.3e}")

print()
print("="*70); print("KEGIATAN 3  Kuadratur Gauss-Legendre"); print("="*70)
print(f"{'n simpul':>9} {'galat Gauss':>16} {'galat Simpson (n eval sama)':>30}")
for n in (2, 3, 4, 5, 6, 8, 10):
    xg, wg = np.polynomial.legendre.leggauss(n)
    xm = 0.5*(b-a)*xg + 0.5*(a+b)
    # TODO 3a: jumlah berbobot Gauss, sudah dipetakan ke [a, b].
    gauss = 0.0
    m = n if n % 2 == 0 else n-1
    simp = simpson(f, a, b, max(m, 2))
    print(f"{n:9d} {abs(gauss-TEPAT):16.3e} {abs(simp-TEPAT):30.3e}")

print()
print("Integran yang menantang: |x - 0.3| pada [0,1]")
g = lambda x: np.abs(x - 0.3)
TEPAT_G = 0.5*(0.3**2) + 0.5*(0.7**2)
for n in (10, 20, 40, 80):
    xg, wg = np.polynomial.legendre.leggauss(n)
    xm = 0.5*xg + 0.5
    gauss = 0.5*np.sum(wg*g(xm))
    print(f"  Gauss n={n:3d} galat={abs(gauss-TEPAT_G):.3e}   "
          f"Simpson n={n:3d} galat={abs(simpson(g,0,1,n)-TEPAT_G):.3e}")
