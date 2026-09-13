"""Praktikum 3 - Sistem linear, metode langsung.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p03_kerangka.py
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
np.set_printoptions(precision=6, suppress=False, linewidth=100)

def gauss_pivot(A, b):
    """Eliminasi Gauss dengan pivoting parsial. A dan b tidak diubah."""
    A = A.astype(float).copy(); b = b.astype(float).copy()
    n = len(b)
    for k in range(n-1):
        # TODO 1b: cari baris pivot, lalu tukar baris A DAN unsur b.
        p = k
        if p != k:
            pass
        for i in range(k+1, n):
            m = A[i, k]/A[k, k]
            A[i, k:] -= m*A[k, k:]; b[i] -= m*b[k]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:])/A[i, i]
    return x

def gauss_tanpa_pivot(A, b):
    A = A.astype(float).copy(); b = b.astype(float).copy()
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            # TODO 1a: pengali, eliminasi baris, dan ruas kanannya.
            m = 0.0
            pass
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        # TODO 1c: substitusi mundur.
        x[i] = b[i]
    return x

print("=" * 70)
print("KEGIATAN 1  Pivoting bukan hiasan")
print("=" * 70)
eps = 1e-18
A = np.array([[eps, 1.0], [1.0, 1.0]])
b = np.array([1.0, 2.0])
tepat = np.array([1.0, 1.0])          # untuk eps -> 0
print("A =", A.tolist(), " b =", b.tolist())
print("tanpa pivoting ->", gauss_tanpa_pivot(A, b))
print("dengan pivoting->", gauss_pivot(A, b))
print("numpy solve    ->", np.linalg.solve(A, b))
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_1ac():
    A3 = np.array([[2.0, 1.0, 1.0], [4.0, -6.0, 0.0], [-2.0, 7.0, 2.0]])
    x = gauss_tanpa_pivot(A3, np.array([5.0, -2.0, 9.0]))
    return np.allclose(x, [1.0, 1.0, 2.0], rtol=0, atol=1e-12), f"gauss_tanpa_pivot memberi {np.round(x, 6).tolist()}, seharusnya [1, 1, 2]"
def _uji_1b():
    x = gauss_pivot(np.array([[1e-18, 1.0], [1.0, 1.0]]), np.array([1.0, 2.0]))
    return np.allclose(x, [1.0, 1.0], rtol=0, atol=1e-12), f"gauss_pivot pada pivot 1e-18 memberi {x.tolist()}, seharusnya [1, 1]; baris belum ditukar"
cek_todo("TODO 1a dan 1c  gauss_tanpa_pivot", _uji_1ac)
cek_todo("TODO 1b  gauss_pivot", _uji_1b)
pass  # <<< pemeriksa

print()
print("=" * 70)
print("KEGIATAN 2  Bilangan kondisi dan matriks Hilbert")
print("=" * 70)
print(f"{'n':>3} {'kond(H)':>12} {'galat relatif':>15} {'sisa relatif':>14}")
for n in range(2, 13):
    # TODO 2a: susun matriks Hilbert n x n, H[i][j] = 1/(i+j+1).
    H = np.eye(n)
    x_tepat = np.ones(n)
    b = H @ x_tepat
    x = gauss_pivot(H, b)
    # TODO 2b: bilangan kondisi, galat relatif, dan sisa relatif.
    kond = 0.0
    galat = 0.0
    sisa = 0.0
    print(f"{n:3d} {kond:12.3e} {galat:15.3e} {sisa:14.3e}")
    if n == 6: _hilbert6 = (H.copy(), kond, galat, sisa)  # pemeriksa
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_2a():
    H6 = _hilbert6[0]
    ok = H6.shape == (6, 6) and H6[0, 0] == 1.0 and H6[2, 3] == 1/6 and H6[5, 5] == 1/11
    return ok, f"untuk n = 6, H[0,0] = {H6[0,0]}, H[2,3] = {H6[2,3]}, seharusnya 1 dan 1/6"
def _uji_2b():
    _, kd, gl, ss = _hilbert6
    if not 1.4e7 < kd < 1.6e7:
        return False, f"kond(H) untuk n = 6 = {kd:.3e}, seharusnya sekitar 1.495e+07"
    if not 1e-14 < gl < 1e-7:
        return False, f"galat relatif untuk n = 6 = {gl:.3e}, seharusnya berorde 1e-10"
    return 0.0 <= ss < 1e-12, f"sisa relatif untuk n = 6 = {ss:.3e}, seharusnya berorde 1e-16"
cek_todo("TODO 2a  matriks Hilbert", _uji_2a)
cek_todo("TODO 2b  kondisi, galat, sisa", _uji_2b)
pass  # <<< pemeriksa

print()
print("=" * 70)
print("KEGIATAN 3  Faktorisasi LU dipakai ulang")
print("=" * 70)
rng = np.random.default_rng(20260824)
n = 400
A = rng.standard_normal((n, n)) + n*np.eye(n)
import time
B = rng.standard_normal((n, 20))

from scipy.linalg import lu_factor, lu_solve
# Panggilan pertama selalu lebih lambat karena pustaka baru dimuat dan
# memori baru disiapkan. Karena itu setiap cara diulang lima kali dan
# yang dicatat waktu tercepatnya.
t_solve = t_lu = float("inf")
for ulang in range(5):
    t0 = time.perf_counter()
    # TODO 3a: dua puluh penyelesaian terpisah.
    X1 = np.zeros_like(B)
    t_solve = min(t_solve, time.perf_counter() - t0)

    t0 = time.perf_counter()
    # TODO 3b: satu faktorisasi, lalu dua puluh substitusi.
    lu, piv = lu_factor(A)
    X2 = np.zeros_like(B)
    t_lu = min(t_lu, time.perf_counter() - t0)

print(f"20 solve terpisah      : {t_solve*1000:8.1f} ms")
print(f"1 faktorisasi + 20 subs: {t_lu*1000:8.1f} ms")
print(f"nisbah                 : {t_solve/t_lu:8.2f} kali")
print(f"selisih hasil          : {np.max(np.abs(X1-X2)):.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3a():
    return np.allclose(A @ X1, B, atol=1e-8), "A @ X1 belum sama dengan B"
def _uji_3b():
    return np.allclose(A @ X2, B, atol=1e-8), "A @ X2 belum sama dengan B"
cek_todo("TODO 3a  dua puluh solve", _uji_3a)
cek_todo("TODO 3b  satu faktorisasi", _uji_3b)
pass  # <<< pemeriksa
