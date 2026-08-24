"""Praktikum 3 - Sistem linear, metode langsung.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p03_kerangka.py
"""
import numpy as np
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

print()
print("=" * 70)
print("KEGIATAN 3  Faktorisasi LU dipakai ulang")
print("=" * 70)
rng = np.random.default_rng(20260824)
n = 400
A = rng.standard_normal((n, n)) + n*np.eye(n)
import time
B = rng.standard_normal((n, 20))

t0 = time.perf_counter()
# TODO 3a: dua puluh penyelesaian terpisah.
X1 = np.zeros_like(B)
t_solve = time.perf_counter() - t0

from scipy.linalg import lu_factor, lu_solve
t0 = time.perf_counter()
# TODO 3b: satu faktorisasi, lalu dua puluh substitusi.
lu, piv = lu_factor(A)
X2 = np.zeros_like(B)
t_lu = time.perf_counter() - t0

print(f"20 solve terpisah      : {t_solve*1000:8.1f} ms")
print(f"1 faktorisasi + 20 subs: {t_lu*1000:8.1f} ms")
print(f"nisbah                 : {t_solve/t_lu:8.2f} kali")
print(f"selisih hasil          : {np.max(np.abs(X1-X2)):.3e}")
