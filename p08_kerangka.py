"""Praktikum 8 - Kuadrat terkecil dan diferensiasi numerik.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p08_kerangka.py
"""
import numpy as np

print("="*74)
print("KEGIATAN 1-2  Persamaan normal lawan QR")
print("="*74)
print(f"{'derajat':>8} {'kond(A)':>12} {'kond(A^T A)':>13} "
      f"{'galat normal':>14} {'galat QR':>12}")
m = 40
x = np.linspace(0, 1, m)
for d in (3, 5, 7, 9, 11, 13):
    A = np.vander(x, d+1, increasing=True)
    c_tepat = np.ones(d+1)
    b = A @ c_tepat
    kA = np.linalg.cond(A)
    kN = np.linalg.cond(A.T @ A)
    # TODO 1a: lewat persamaan normal.
    c_normal = np.zeros(d+1)
    Q, R = np.linalg.qr(A)
    # TODO 1b: lewat QR. Ruas kanannya apa?
    c_qr = np.zeros(d+1)
    gn = np.linalg.norm(c_normal - c_tepat)/np.linalg.norm(c_tepat)
    gq = np.linalg.norm(c_qr - c_tepat)/np.linalg.norm(c_tepat)
    print(f"{d:8d} {kA:12.3e} {kN:13.3e} {gn:14.3e} {gq:12.3e}")

print()
print("="*74)
print("KEGIATAN 3  Diferensiasi numerik dan h yang optimal")
print("="*74)
f = np.sin
df_tepat = np.cos(1.0)
x0 = 1.0
print(f"{'h':>10} {'maju':>14} {'pusat':>14}")
for k in range(1, 17):
    h = 10.0**(-k)
    # TODO 2a: beda maju dan beda pusat.
    maju = 0.0
    pusat = 0.0
    print(f"{h:10.1e} {abs(maju-df_tepat):14.3e} {abs(pusat-df_tepat):14.3e}")

eps = np.finfo(float).eps
print()
print(f"h optimal teori beda maju  ~ 2*sqrt(eps)     = {2*np.sqrt(eps):.3e}")
print(f"h optimal teori beda pusat ~ (3*eps)**(1/3)  = {(3*eps)**(1/3):.3e}")

print()
print("Langkah kompleks, yang bebas pengurangan berbahaya:")
for k in (4, 8, 12, 16, 20):
    h = 10.0**(-k)
    # TODO 3a: langkah kompleks. Ambil bagian khayal, lalu bagi h.
    kompleks = 0.0
    print(f"  h={h:8.1e}  galat={abs(kompleks-df_tepat):.3e}")
