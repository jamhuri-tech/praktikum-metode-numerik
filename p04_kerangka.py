"""Praktikum 4 - Sistem linear, metode iteratif.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p04_kerangka.py
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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
_A3 = np.array([[4.0, 1.0, 0.0], [1.0, 4.0, 1.0], [0.0, 1.0, 4.0]])
_b3 = np.array([1.0, 2.0, 3.0])
_x3 = np.linalg.solve(_A3, _b3)
def _uji_1a():
    x, s = jacobi(_A3, _b3, maks=500)
    if not np.allclose(x, _x3, atol=1e-8):
        return False, f"jacobi pada sistem 3x3 memberi {np.round(x, 6).tolist()}, seharusnya {np.round(_x3, 6).tolist()}"
    return len(s) < 100, f"hasilnya benar tetapi butuh {len(s)} iterasi; seharusnya sekitar 23"
def _uji_1b():
    x, s = gauss_seidel(_A3, _b3, maks=500)
    if not np.allclose(x, _x3, atol=1e-8):
        return False, f"gauss_seidel pada sistem 3x3 memberi {np.round(x, 6).tolist()}, seharusnya {np.round(_x3, 6).tolist()}"
    return len(s) < 50, f"hasilnya benar tetapi butuh {len(s)} iterasi; seharusnya sekitar 12"
# SOR yang omega-nya belum dipakai berubah menjadi Gauss-Seidel dan tetap
# konvergen ke jawaban yang benar. Yang membedakan hanya cacah iterasinya.
def _uji_1c():
    A10 = matriks_uji(10); b10 = np.ones(10)
    xg, sg = gauss_seidel(A10, b10, maks=2000)
    if not np.allclose(A10 @ xg, b10, atol=1e-8):
        return False, "isi TODO 1b lebih dahulu; SOR diperiksa dengan membandingkannya terhadap Gauss-Seidel"
    xs, ss = sor(A10, b10, 1.5, maks=2000)
    if not np.allclose(A10 @ xs, b10, atol=1e-8):
        return False, "sor dengan omega = 1.5 tidak konvergen ke jawaban yang benar"
    return len(ss) < 0.8*len(sg), f"sor dengan omega = 1.5 memakai {len(ss)} iterasi, Gauss-Seidel {len(sg)}; omega belum ikut dihitung"
cek_todo("TODO 1a  jacobi", _uji_1a)
cek_todo("TODO 1b  gauss_seidel", _uji_1b)
cek_todo("TODO 1c  sor", _uji_1c)
pass  # <<< pemeriksa

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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
# Tidak membandingkan matriksnya, supaya rumusnya tidak terbaca di sini.
# Untuk matriks tridiagonal (-1, 2, -1) teorinya sudah diketahui:
# jari-jari spektral Jacobi cos(pi/(n+1)), dan Gauss-Seidel kuadratnya.
def _uji_2a():
    teori = np.cos(np.pi/(n + 1))
    if abs(rj - teori) > 1e-9:
        return False, f"jari-jari spektral Jacobi = {rj:.9f}, seharusnya {teori:.9f}"
    return abs(rg - rj**2) < 1e-9, f"jari-jari spektral Gauss-Seidel = {rg:.9f}, seharusnya kuadrat Jacobi, {rj**2:.9f}"
cek_todo("TODO 2a  matriks iterasi", _uji_2a)
pass  # <<< pemeriksa

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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3b():
    return abs(w_teori - 1.8577877368177955) < 1e-9, f"w_teori = {float(w_teori)!r}, seharusnya 1.857787736817..."
cek_todo("TODO 3b  omega optimal", _uji_3b)
pass  # <<< pemeriksa
