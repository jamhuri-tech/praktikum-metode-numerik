"""Praktikum 11 - Masalah nilai batas.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p11_kerangka.py
"""
import numpy as np
from scipy.optimize import brentq

print("="*70); print("KEGIATAN 1  Metode tembak"); print("="*70)
# y'' = -y, y(0)=0, y(pi/2)=1  ->  y = sin x
def integrasi(s, n=400, L=np.pi/2):
    """RK4 pada sistem orde satu, dari y(0)=0, y'(0)=s."""
    h = L/n; y = np.array([0.0, s])
    F = lambda t, v: np.array([v[1], -v[0]])
    t = 0.0
    for k in range(n):
        # TODO 1a: RK4 pada sistem. Sama seperti Praktikum 10,
        # bedanya y sekarang vektor.
        k1 = F(t, y)
        y = y + h*k1; t += h
    return y[0]

print(f"{'tebakan s':>12} {'y(pi/2)':>14} {'sisa':>12}")
for s in (0.0, 0.5, 1.0, 1.5, 2.0):
    print(f"{s:12.4f} {integrasi(s):14.8f} {integrasi(s)-1.0:12.3e}")
s_bagus = brentq(lambda s: integrasi(s) - 1.0, 0.0, 2.0, xtol=1e-14)
print(f"\ns yang benar = {s_bagus:.14f}   (seharusnya y'(0) = cos 0 = 1)")
print(f"galat        = {abs(s_bagus-1.0):.3e}")

print()
print("="*70); print("KEGIATAN 2  Beda hingga untuk masalah nilai batas"); print("="*70)
# -u'' = f, u(0)=u(1)=0, f = pi^2 sin(pi x) -> u = sin(pi x)
def bnb_beda_hingga(n):
    h = 1.0/(n+1)
    x = np.linspace(0, 1, n+2)[1:-1]
    # TODO 2a: susun matriks beda hingga. Jangan lupa pembaginya.
    A = (np.diag(2*np.ones(n)) + np.diag(-np.ones(n-1), 1)
         + np.diag(-np.ones(n-1), -1))
    b = np.pi**2*np.sin(np.pi*x)
    return x, np.linalg.solve(A, b)
print(f"{'n':>6} {'h':>10} {'galat maks':>14} {'orde':>7}")
sebelum = None
for n in (7, 15, 31, 63, 127, 255):
    x, u = bnb_beda_hingga(n)
    g = np.max(np.abs(u - np.sin(np.pi*x)))
    orde = np.log2(sebelum/g) if sebelum else float('nan')
    print(f"{n:6d} {1/(n+1):10.5f} {g:14.6e} {orde:7.3f}")
    sebelum = g

print()
print("="*70); print("KEGIATAN 3  Poisson dua dimensi"); print("="*70)
# -Laplace u = f pada (0,1)^2, u=0 di batas, f = 2 pi^2 sin(pi x) sin(pi y)
def poisson2d(n):
    h = 1.0/(n+1)
    x = np.linspace(0, 1, n+2)[1:-1]
    X, Y = np.meshgrid(x, x, indexing='ij')
    T = (np.diag(2*np.ones(n)) + np.diag(-np.ones(n-1), 1)
         + np.diag(-np.ones(n-1), -1))
    I = np.eye(n)
    # TODO 3a: Laplacian lima titik lewat hasil kali Kronecker.
    A = np.kron(T, I)/h**2
    f = 2*np.pi**2*np.sin(np.pi*X)*np.sin(np.pi*Y)
    u = np.linalg.solve(A, f.ravel()).reshape(n, n)
    return X, Y, u
print(f"{'n':>5} {'ukuran A':>12} {'galat maks':>14} {'orde':>7} {'kond(A)':>12}")
sebelum = None
for n in (7, 15, 31, 63):
    X, Y, u = poisson2d(n)
    g = np.max(np.abs(u - np.sin(np.pi*X)*np.sin(np.pi*Y)))
    orde = np.log2(sebelum/g) if sebelum else float('nan')
    h = 1.0/(n+1)
    T = (np.diag(2*np.ones(n)) + np.diag(-np.ones(n-1), 1)
         + np.diag(-np.ones(n-1), -1))
    A = (np.kron(T, np.eye(n)) + np.kron(np.eye(n), T))/h**2
    print(f"{n:5d} {n*n:6d}x{n*n:<5d} {g:14.6e} {orde:7.3f} "
          f"{np.linalg.cond(A):12.3e}")
    sebelum = g
print("\nUkuran matriks tumbuh seperti n^2 x n^2. Pada n=63 itu 3969x3969,")
print("dan pada n=127 sudah 16129x16129: di sinilah metode iteratif masuk.")
