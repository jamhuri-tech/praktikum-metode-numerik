"""Praktikum 6 - Nilai eigen dan nilai singular.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p06_kerangka.py
"""
import numpy as np
np.set_printoptions(precision=6, suppress=True)

A = np.array([[4.0, 1.0, 1.0],
              [1.0, 3.0, 1.0],
              [1.0, 1.0, 2.0]])
eig_tepat = np.sort(np.linalg.eigvalsh(A))[::-1]
print("nilai eigen acuan:", eig_tepat)

def pangkat(A, q0=None, maks=200, tol=1e-13):
    n = A.shape[0]
    q = np.ones(n)/np.sqrt(n) if q0 is None else q0/np.linalg.norm(q0)
    riwayat = []
    lam = 0.0
    for k in range(maks):
        # TODO 1a: kalikan, normalkan, lalu hasil bagi Rayleigh.
        z = q
        q = z/np.linalg.norm(z)
        lam_baru = 0.0
        riwayat.append(lam_baru)
        if abs(lam_baru - lam) < tol: break
        lam = lam_baru
    return lam, q, riwayat

def pangkat_invers(A, mu, maks=200, tol=1e-13):
    n = A.shape[0]
    M = A - mu*np.eye(n)
    q = np.ones(n)/np.sqrt(n); lam = 0.0
    for k in range(maks):
        # TODO 2a: ganti perkalian dengan penyelesaian sistem.
        z = q
        q = z/np.linalg.norm(z)
        lam_baru = q @ A @ q
        if abs(lam_baru - lam) < tol: return lam_baru, q, k+1
        lam = lam_baru
    return lam, q, maks

print()
print("="*70); print("KEGIATAN 1  Metode pangkat"); print("="*70)
lam, q, riw = pangkat(A)
print(f"nilai eigen dominan : {lam:.14f}")
print(f"galat               : {abs(lam-eig_tepat[0]):.3e}")
print(f"iterasi             : {len(riw)}")
print()
print(f"{'k':>3} {'lambda':>18} {'galat':>12}")
for k in (0,1,2,3,4,5,10,15,20):
    if k < len(riw):
        print(f"{k:3d} {riw[k]:18.12f} {abs(riw[k]-eig_tepat[0]):12.3e}")
nisbah = abs(eig_tepat[1]/eig_tepat[0])
print(f"\nnisbah |lambda2/lambda1| = {nisbah:.6f}")
print("galat berkurang kira-kira sebesar kuadrat nisbah itu tiap langkah,")
print(f"sebab hasil bagi Rayleigh: {nisbah**2:.6f}")

print()
print("="*70); print("KEGIATAN 2  Pangkat invers dengan pergeseran"); print("="*70)
for mu in (0.0, 1.5, 3.0, 5.0):
    lam, q, it = pangkat_invers(A, mu)
    dekat = eig_tepat[np.argmin(np.abs(eig_tepat - mu))]
    print(f"mu={mu:4.1f} -> lambda={lam:16.12f}  iterasi={it:3d}  "
          f"eigen terdekat dari mu = {dekat:.12f}")

print()
print("="*70); print("KEGIATAN 3  Iterasi QR"); print("="*70)
def qr_dasar(A, maks=100, tol=1e-13):
    Ak = A.copy()
    for k in range(maks):
        # TODO 3a: faktorkan, lalu kalikan terbalik. Urutannya menentukan.
        Q, R = np.linalg.qr(Ak)
        Ak = Ak
        luar = np.sum(np.abs(np.tril(Ak, -1)))
        if luar < tol: return Ak, k+1
    return Ak, maks
Ak, it = qr_dasar(A)
print(f"iterasi QR: {it}")
print("matriks akhir (diagonalnya nilai eigen):")
print(Ak)
print("diagonal   :", np.sort(np.diag(Ak))[::-1])
print("acuan      :", eig_tepat)
print("galat maks :", np.max(np.abs(np.sort(np.diag(Ak))[::-1] - eig_tepat)))
