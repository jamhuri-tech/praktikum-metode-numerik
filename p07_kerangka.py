"""Praktikum 7 - Interpolasi polinomial dan spline.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p07_kerangka.py
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
from scipy.interpolate import CubicSpline

runge = lambda x: 1.0/(1.0 + 25.0*x**2)

def selisih_terbagi(x, y):
    n = len(x); c = y.astype(float).copy()
    for j in range(1, n):
        # TODO 1a: satu kolom tabel selisih terbagi.
        c[j:] = c[j:]
    return c

def newton_eval(x, c, t):
    n = len(x); p = np.full_like(np.atleast_1d(t), c[-1], dtype=float)
    for k in range(n-2, -1, -1):
        # TODO 1b: satu langkah skema Horner.
        p = p
    return p

def simpul_seragam(n): return np.linspace(-1, 1, n+1)
def simpul_chebyshev(n):
    # TODO 2b: simpul Chebyshev pada [-1, 1].
    return np.linspace(-1, 1, n+1)

t = np.linspace(-1, 1, 2001)
benar = runge(t)

print("="*70); print("KEGIATAN 1-2  Selisih terbagi Newton dan fenomena Runge"); print("="*70)
print(f"{'n':>4} {'galat maks seragam':>22} {'galat maks Chebyshev':>22}")
for n in (5, 10, 15, 20, 25, 30):
    hasil = []
    for simpul in (simpul_seragam, simpul_chebyshev):
        x = simpul(n); y = runge(x)
        c = selisih_terbagi(x, y)
        hasil.append(np.max(np.abs(newton_eval(x, c, t) - benar)))
    print(f"{n:4d} {hasil[0]:22.6e} {hasil[1]:22.6e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_1a():
    c = selisih_terbagi(np.array([0.0, 1.0, 2.0]), np.array([1.0, 3.0, 7.0]))
    return np.allclose(c, [1.0, 2.0, 1.0]), f"selisih terbagi titik (0,1), (1,3), (2,7) = {c.tolist()}, seharusnya [1, 2, 1]"
def _uji_1b():
    p = newton_eval(np.array([0.0, 1.0, 2.0]), np.array([1.0, 2.0, 1.0]), np.array([3.0]))
    return np.allclose(p, [13.0]), f"polinomial 1 + 2x + x(x-1) di x = 3 dihitung {p.tolist()}, seharusnya 13"
def _uji_2b():
    s = np.sort(simpul_chebyshev(4))
    acuan = [-1.0, -2**-0.5, 0.0, 2**-0.5, 1.0]
    return np.allclose(s, acuan, atol=1e-12), f"simpul_chebyshev(4) = {np.round(s, 6).tolist()}, seharusnya [-1, -0.707107, 0, 0.707107, 1]"
cek_todo("TODO 1a  selisih terbagi", _uji_1a)
cek_todo("TODO 1b  skema Horner", _uji_1b)
cek_todo("TODO 2b  simpul Chebyshev", _uji_2b)
pass  # <<< pemeriksa

print()
print("="*70); print("KEGIATAN 3  Spline kubik natural"); print("="*70)
print(f"{'n':>4} {'galat spline':>16} {'orde terukur':>14}")
sebelum = None
for n in (5, 10, 20, 40, 80, 160):
    x = np.linspace(-1, 1, n+1); y = runge(x)
    s = CubicSpline(x, y, bc_type='natural')
    g = np.max(np.abs(s(t) - benar))
    orde = np.log2(sebelum/g) if sebelum else float('nan')
    print(f"{n:4d} {g:16.6e} {orde:14.3f}")
    sebelum = g
