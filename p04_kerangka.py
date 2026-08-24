"""Praktikum 4 - Sistem linear, metode iteratif.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p04_kerangka.py
"""
import numpy as np

def matriks_uji(n):
    """Beda hingga 1D: tridiagonal (-1, 2, -1), simetris definit positif."""
    A = np.diag(2.0*np.ones(n)) + np.diag(-np.ones(n-1), 1) + np.diag(-np.ones(n-1), -1)
    return A

def jacobi(A, b, x0=None, tol=1e-10, maks=20000):
    n = len(b); x = np.zeros(n) if x0 is None else x0.copy()
    D = np.diag(A); R = A - np.diag(D)
    sisa = []
    for k in range(maks):
        # TODO 1a: satu baris Jacobi, pakai D dan R.
        x = x
        r = np.linalg.norm(b - A @ x)/np.linalg.norm(b); sisa.append(r)
        if r < tol: break
    return x, sisa

def gauss_seidel(A, b, tol=1e-10, maks=20000):
    n = len(b); x = np.zeros(n); sisa = []
    for k in range(maks):
        for i in range(n):
            # TODO 1b: satu baris Gauss-Seidel.
            x[i] = x[i]
        r = np.linalg.norm(b - A @ x)/np.linalg.norm(b); sisa.append(r)
        if r < tol: break
    return x, sisa

def sor(A, b, w, tol=1e-10, maks=20000):
    n = len(b); x = np.zeros(n); sisa = []
    for k in range(maks):
        for i in range(n):
            baru = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ x[i+1:])/A[i, i]
            # TODO 1c: campurkan nilai lama dengan nilai Gauss-Seidel.
            x[i] = baru
        r = np.linalg.norm(b - A @ x)/np.linalg.norm(b); sisa.append(r)
        if r < tol: break
    return x, sisa

def jari_jari(M):
    return np.max(np.abs(np.linalg.eigvals(M)))

print("=" * 70)
print("KEGIATAN 1  Tiga metode pada persoalan yang sama, n = 40")
print("=" * 70)
n = 40
A = matriks_uji(n); b = np.ones(n)
xj, sj = jacobi(A, b); xg, sg = gauss_seidel(A, b); xs, ss = sor(A, b, 1.85)
tepat = np.linalg.solve(A, b)
for nama, x, s in (("Jacobi", xj, sj), ("Gauss-Seidel", xg, sg), ("SOR w=1.85", xs, ss)):
    print(f"{nama:14s} iterasi={len(s):6d}  galat={np.linalg.norm(x-tepat):.3e}")

print()
print("=" * 70)
print("KEGIATAN 2  Jari-jari spektral meramalkan lajunya")
print("=" * 70)
D = np.diag(np.diag(A)); L = np.tril(A, -1); U = np.triu(A, 1)
# TODO 2a: susun kedua matriks iterasi.
Mj = np.eye(n)
Mg = np.eye(n)
rj, rg = jari_jari(Mj), jari_jari(Mg)
print(f"jari-jari spektral Jacobi       : {rj:.6f}")
print(f"jari-jari spektral Gauss-Seidel : {rg:.6f}")
print(f"nisbah kuadrat rj^2/rg          : {rj**2/rg:.6f}")
print(f"ramalan iterasi Jacobi   ~ log(tol)/log(rho) = {np.log(1e-10)/np.log(rj):8.0f}")
print(f"ramalan iterasi G-Seidel ~                     {np.log(1e-10)/np.log(rg):8.0f}")
print(f"iterasi sesungguhnya            : {len(sj)}  dan  {len(sg)}")

print()
print("=" * 70)
print("KEGIATAN 3  Mencari omega terbaik untuk SOR")
print("=" * 70)
print(f"{'omega':>6} {'iterasi':>9}")
terbaik = (None, 10**9)
for w in np.arange(1.0, 1.99, 0.05):
    _, s = sor(A, b, w)
    if len(s) < terbaik[1]: terbaik = (w, len(s))
    if abs(w - round(w, 2)) < 1e-9 and round(w*100) % 10 == 0:
        print(f"{w:6.2f} {len(s):9d}")
# TODO 3b: omega optimal menurut teori.
w_teori = 1.0
print(f"\nomega terbaik hasil percobaan : {terbaik[0]:.2f} ({terbaik[1]} iterasi)")
print(f"omega optimal menurut teori    : {w_teori:.4f}")
_, s_opt = sor(A, b, w_teori)
print(f"iterasi pada omega teori       : {len(s_opt)}")
