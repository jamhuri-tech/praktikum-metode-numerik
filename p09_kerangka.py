"""Praktikum 9 - Integrasi numerik.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p09_kerangka.py
"""
import numpy as np
# >>> pemeriksa
# Pemeriksa isian. Setiap kegiatan diakhiri pemeriksaan otomatis atas
# TODO-nya. Ujinya memakai persoalan kecil yang berbeda dari tabel pada
# modul, jadi lolosnya bukan karena angka tabel kebetulan sama. Kalau
# tertulis BELUM, baca pesannya: pesan itu menyebut angka yang keluar dari
# kode Anda dan angka yang seharusnya.
def cek_todo(label, uji):
    try:
        ok, pesan = uji()
    except Exception as e:
        ok, pesan = False, f"galat saat dijalankan: {type(e).__name__}: {e}"
    if ok:
        print(f"  [BENAR] {label}")
    else:
        print(f"  [BELUM] {label}")
        print(f"          {pesan}")
    return ok
pass  # <<< pemeriksa
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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_1a():
    v = trapesium(lambda x: x*x, 0.0, 1.0, 2)
    return abs(v - 0.375) < 1e-14, f"trapesium x^2 pada [0, 1], n = 2 = {float(v)!r}, seharusnya 0.375"
def _uji_1b():
    v2 = simpson(lambda x: x*x, 0.0, 1.0, 2); v3 = simpson(lambda x: x**3, 0.0, 1.0, 4)
    if abs(v2 - 1/3) > 1e-14:
        return False, f"simpson x^2 pada [0, 1], n = 2 = {float(v2)!r}, seharusnya tepat 1/3"
    return abs(v3 - 0.25) < 1e-14, f"simpson x^3 pada [0, 1], n = 4 = {float(v3)!r}, seharusnya tepat 0.25"
cek_todo("TODO 1a  trapesium", _uji_1a)
cek_todo("TODO 1b  simpson", _uji_1b)
pass  # <<< pemeriksa

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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_2b():
    if abs(trapesium(lambda x: x*x, 0.0, 1.0, 2) - 0.375) > 1e-14:
        return False, "isi TODO 1a lebih dahulu; Romberg dibangun di atas trapesium"
    v = romberg(lambda x: x**4, 0.0, 1.0, 3)[2, 2]
    return abs(v - 0.2) < 1e-12, f"Romberg R[2,2] untuk x^4 pada [0, 1] = {float(v)!r}, seharusnya tepat 0.2"
cek_todo("TODO 2b  ekstrapolasi Richardson", _uji_2b)
pass  # <<< pemeriksa

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
    if n == 4: _gauss4 = gauss  # pemeriksa

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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3a():
    return abs(_gauss4 - TEPAT) < 1e-4, f"Gauss 4 simpul untuk exp(-x^2) = {float(_gauss4)!r}, seharusnya dekat {TEPAT:.10f}"
cek_todo("TODO 3a  kuadratur Gauss", _uji_3a)
pass  # <<< pemeriksa
