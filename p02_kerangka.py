"""Praktikum 2 - Akar persamaan nonlinear.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p02_kerangka.py
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

f  = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2

def bagi_dua(f, a, b, tol=1e-12, maks=200):
    riwayat = []
    fa = f(a)
    for k in range(maks):
        c = 0.5*(a+b); fc = f(c); riwayat.append(c)
        if b-a < tol: break
        # TODO 1a: dua baris. Bandingkan TANDA, bukan hasil kali.
        if np.sign(fc) == np.sign(fa):
            pass
        else:
            pass
    return c, riwayat

def newton(f, df, x0, tol=1e-14, maks=100):
    riwayat = [x0]; x = x0
    for k in range(maks):
        # TODO 1b: satu baris rumus Newton.
        x = x
        riwayat.append(x)
        if abs(f(x)) < tol: break
    return x, riwayat

def secant(f, x0, x1, tol=1e-14, maks=100):
    riwayat = [x0, x1]
    for k in range(maks):
        fx0, fx1 = f(x0), f(x1)
        if fx1 == fx0: break
        # TODO 1c: rumus secant.
        x2 = x1
        riwayat.append(x2)
        x0, x1 = x1, x2
        if abs(f(x1)) < tol: break
    return x1, riwayat

akar = 2.0945514815423265
print("="*70); print("KEGIATAN 1  Tiga metode, satu persoalan"); print("="*70)
print("akar acuan:", akar)
for nama, (r, h) in (("bagi dua", bagi_dua(f, 2, 3)),
                     ("Newton", newton(f, df, 2.0)),
                     ("secant", secant(f, 2.0, 2.2))):
    print(f"{nama:10s} akar={r:.16f}  iterasi={len(h)-1}")

print()
print("orde konvergensi, galat tiap iterasi")
print(f"{'k':>3} {'bagi dua':>12} {'Newton':>12} {'secant':>12}")
_, hb = bagi_dua(f, 2, 3); _, hn = newton(f, df, 2.0); _, hs = secant(f, 2.0, 2.2)
for k in range(8):
    b = abs(hb[k]-akar) if k < len(hb) else float('nan')
    n = abs(hn[k]-akar) if k < len(hn) else float('nan')
    s = abs(hs[k]-akar) if k < len(hs) else float('nan')
    print(f"{k:3d} {b:12.3e} {n:12.3e} {s:12.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_1a():
    r, h = bagi_dua(lambda x: x*x - 2, 1.0, 2.0, tol=1e-10)
    return abs(r - 2**0.5) < 1e-9, f"bagi_dua pada x^2 - 2 di [1, 2] memberi {r!r}, seharusnya dekat 1.41421356"
def _uji_1b():
    r, h = newton(lambda x: x*x - 2, lambda x: 2*x, 1.0)
    if abs(r - 2**0.5) > 1e-12:
        return False, f"newton pada x^2 - 2 dari 1 memberi {r!r}, seharusnya 1.4142135623730951"
    return len(h) - 1 <= 6, f"akarnya benar tetapi butuh {len(h)-1} iterasi; Newton seharusnya paling banyak 6"
def _uji_1c():
    r, h = secant(lambda x: x*x - 2, 1.0, 2.0)
    if abs(r - 2**0.5) > 1e-12:
        return False, f"secant pada x^2 - 2 dari 1 dan 2 memberi {r!r}, seharusnya 1.4142135623730951"
    return len(h) - 2 <= 9, f"akarnya benar tetapi butuh {len(h)-2} iterasi; secant seharusnya paling banyak 9"
cek_todo("TODO 1a  bagi_dua", _uji_1a)
cek_todo("TODO 1b  newton", _uji_1b)
cek_todo("TODO 1c  secant", _uji_1c)
pass  # <<< pemeriksa

print()
print("="*70); print("KEGIATAN 2  Mengukur orde konvergensi"); print("="*70)
print("taksiran orde p dari tiga galat berurutan")
def orde(h):
    e = [abs(x-akar) for x in h if abs(x-akar) > 0]
    out = []
    for k in range(1, len(e)-1):
        if e[k-1] > 0 and e[k] > 0 and e[k+1] > 1e-16:
            # TODO 2a: taksiran orde dari tiga galat berurutan.
            out.append(float('nan'))
    return out
print("Newton :", " ".join(f"{p:.3f}" for p in orde(hn)[:3]))
# Taksiran pertama secant dilewati: galatnya sempat naik pada langkah
# pertama, sehingga nisbahnya tidak bermakna.
print("secant :", " ".join(f"{p:.3f}" for p in orde(hs)[1:4]))
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_2a():
    p = orde([akar + 1e-1, akar + 1e-2, akar + 1e-4, akar + 1e-8])
    if not p or p[0] != p[0]:
        return False, "orde() masih mengembalikan nan"
    return abs(p[0] - 2) < 1e-6, f"galat 1e-1, 1e-2, 1e-4 seharusnya memberi orde 2, bukan {p[0]:.4f}"
cek_todo("TODO 2a  orde", _uji_2a)
pass  # <<< pemeriksa

print()
print("="*70); print("KEGIATAN 3  Ketika Newton kehilangan kekuadratikannya")
print("="*70)
print("Newton pada akar kembar f(x) = (x-1)^2")
g  = lambda x: (x-1)**2
dg = lambda x: 2*(x-1)
_, hg = newton(g, dg, 2.0, tol=1e-30, maks=12)
for k in range(0, 11, 2):
    print(f"  k={k:2d}  galat={abs(hg[k]-1.0):.3e}")
