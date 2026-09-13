"""Praktikum 5 - Sistem nonlinear dan optimasi.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p05_kerangka.py
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

def F(v):
    x, y = v
    return np.array([x**2 + y**2 - 4.0, np.exp(x) + y - 1.0])

def J(v):
    x, y = v
    # TODO 1a: matriks Jacobi 2x2.
    return np.eye(2)

def newton_sistem(F, J, x0, tol=1e-12, maks=50):
    x = np.array(x0, float); riwayat = [x.copy()]
    for k in range(maks):
        # TODO 1b: selesaikan sistem, jangan menghitung invers.
        s = np.zeros_like(x)
        x = x + s; riwayat.append(x.copy())
        if np.linalg.norm(F(x)) < tol: break
    return x, riwayat

def broyden(F, x0, B0=None, tol=1e-12, maks=100):
    x = np.array(x0, float)
    B = np.eye(len(x)) if B0 is None else B0.copy()
    riwayat = [x.copy()]
    for k in range(maks):
        s = np.linalg.solve(B, -F(x))
        xb = x + s; y = F(xb) - F(x)
        # TODO 2a: pembaruan Broyden.
        B = B
        x = xb; riwayat.append(x.copy())
        if np.linalg.norm(F(x)) < tol: break
    return x, riwayat

print("="*70); print("KEGIATAN 1  Newton untuk sistem"); print("="*70)
akar, hn = newton_sistem(F, J, [1.0, -1.0])
print("akar      :", akar)
print("|F(akar)| :", np.linalg.norm(F(akar)))
print("iterasi   :", len(hn)-1)
print()
print(f"{'k':>3} {'x':>20} {'y':>20} {'|F|':>12}")
for k, v in enumerate(hn):
    print(f"{k:3d} {v[0]:20.14f} {v[1]:20.14f} {np.linalg.norm(F(v)):12.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
_F2 = lambda v: np.array([v[0]**2 - 2.0, v[1] - 1.0])
_J2 = lambda v: np.array([[2*v[0], 0.0], [0.0, 1.0]])
def _uji_1a():
    j1 = J(np.array([1.0, -1.0])); j2 = J(np.array([0.5, 2.0]))
    ok = (np.allclose(j1, [[2.0, -2.0], [np.e, 1.0]])
          and np.allclose(j2, [[1.0, 4.0], [np.exp(0.5), 1.0]]))
    return ok, f"J(1, -1) = {np.round(j1, 6).tolist()}, seharusnya [[2, -2], [2.718282, 1]]"
def _uji_1b():
    x, h = newton_sistem(_F2, _J2, [1.0, 0.0])
    if not np.allclose(x, [2**0.5, 1.0], atol=1e-12):
        return False, f"newton_sistem pada x^2 = 2, y = 1 memberi {x.tolist()}, seharusnya [1.414214, 1]"
    return len(h) - 1 <= 8, f"akarnya benar tetapi butuh {len(h)-1} iterasi; seharusnya sekitar 5"
cek_todo("TODO 1a  matriks Jacobi", _uji_1a)
cek_todo("TODO 1b  newton_sistem", _uji_1b)
pass  # <<< pemeriksa

print()
print("="*70); print("KEGIATAN 2  Broyden tanpa Jacobi"); print("="*70)
ab, hb = broyden(F, [1.0, -1.0], B0=J(np.array([1.0, -1.0])))
print("akar      :", ab)
print("iterasi   :", len(hb)-1)
print(f"Newton  : {len(hn)-1} iterasi, {2*(len(hn)-1)} evaluasi (F dan J)")
print(f"Broyden : {len(hb)-1} iterasi, {len(hb)} evaluasi F, 1 Jacobi")
print()
print(f"{'k':>3} {'|F| Newton':>14} {'|F| Broyden':>14}")
for k in range(max(len(hn), len(hb))):
    a = f"{np.linalg.norm(F(hn[k])):14.3e}" if k < len(hn) else " "*14
    b = f"{np.linalg.norm(F(hb[k])):14.3e}" if k < len(hb) else " "*14
    print(f"{k:3d} {a} {b}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
# Broyden yang B-nya tidak diperbarui menjadi metode chord: tetap
# konvergen, hanya jauh lebih lambat. Yang membedakan cacah iterasinya.
def _uji_2a():
    x, h = broyden(_F2, [1.0, 0.0], B0=_J2(np.array([1.0, 0.0])))
    if not np.allclose(x, [2**0.5, 1.0], atol=1e-10):
        return False, f"broyden memberi {x.tolist()}, seharusnya [1.414214, 1]"
    return len(h) - 1 <= 12, f"konvergen tetapi butuh {len(h)-1} iterasi, seharusnya sekitar 6; B belum diperbarui, ini masih metode chord"
cek_todo("TODO 2a  pembaruan Broyden", _uji_2a)
pass  # <<< pemeriksa

print()
print("="*70); print("KEGIATAN 3  Newton yang melenceng, dan pencarian garis"); print("="*70)
np.seterr(all="ignore")

f  = lambda x: np.arctan(x)
df = lambda x: 1.0/(1.0 + x*x)

def newton_1d(x0, pakai_garis, maks=40):
    """Newton dengan pilihan peredaman. Langkah dipotong separuh terus
    selama |f| belum turun, itulah pencarian garis mundur yang paling
    sederhana."""
    x = float(x0)
    for k in range(maks):
        s = -f(x)/df(x)
        lam = 1.0
        if pakai_garis:
            # TODO 3b: potong separuh selama |f| belum turun.
            pass
        x = x + lam*s
        if not np.isfinite(x):
            return "meledak", k+1, x
        if abs(f(x)) < 1e-12:
            return "konvergen", k+1, x
    return "macet", maks, x

print("Mencari akar arctan(x) = 0, yang jelas x = 0.")
print()
print(f"{'x0':>8} {'Newton polos':>26} {'Newton + garis':>26}")
for x0 in (0.5, 1.0, 1.3, 1.3917, 1.4, 2.0, 5.0):
    a = newton_1d(x0, False)
    b = newton_1d(x0, True)
    print(f"{x0:8.4f} {a[0]:>14s} it={a[1]:3d} {b[0]:>14s} it={b[1]:3d}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3b():
    polos, garis = newton_1d(5.0, False)[0], newton_1d(5.0, True)[0]
    return garis == "konvergen", f"dari x0 = 5 dengan pencarian garis hasilnya '{garis}', seharusnya 'konvergen'"
cek_todo("TODO 3b  pencarian garis", _uji_3b)
pass  # <<< pemeriksa
