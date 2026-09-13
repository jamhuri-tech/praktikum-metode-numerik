"""Praktikum 8 - Kuadrat terkecil dan diferensiasi numerik.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p08_kerangka.py
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

print("="*74)
print("KEGIATAN 1  Persamaan normal lawan QR")
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
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
# Pada derajat 13 persamaan normal memang memberi koefisien yang jauh
# meleset; itulah pelajarannya. Karena itu yang diperiksa sisanya, bukan
# galat koefisiennya.
def _uji_1a():
    sisa = np.linalg.norm(A @ c_normal - b)/np.linalg.norm(b)
    return sisa < 1e-6, f"sisa relatif persamaan normal = {sisa:.3e}, seharusnya berorde 1e-9"
def _uji_1b():
    galat = np.linalg.norm(c_qr - 1.0)/np.linalg.norm(np.ones_like(c_qr))
    return galat < 1e-5, f"galat relatif koefisien lewat QR = {galat:.3e}, seharusnya berorde 1e-8"
cek_todo("TODO 1a  persamaan normal", _uji_1a)
cek_todo("TODO 1b  QR", _uji_1b)
pass  # <<< pemeriksa

print()
print("="*74)
print("KEGIATAN 2  Lembah pada galat diferensiasi")
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
    if k == 3: _beda3 = (maju, pusat)  # pemeriksa

eps = np.finfo(float).eps
print()
print(f"h optimal teori beda maju  ~ 2*sqrt(eps)     = {2*np.sqrt(eps):.3e}")
print(f"h optimal teori beda pusat ~ (3*eps)**(1/3)  = {(3*eps)**(1/3):.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_2a():
    mj, ps = _beda3
    if abs(mj - 0.5398814803603269) > 1e-12:
        return False, f"beda maju pada h = 1e-3 = {float(mj)!r}, seharusnya 0.539881480360..."
    return abs(ps - 0.5403022158177451) < 1e-12, f"beda pusat pada h = 1e-3 = {float(ps)!r}, seharusnya 0.540302215817..."
cek_todo("TODO 2a  beda maju dan pusat", _uji_2a)
pass  # <<< pemeriksa

print()
print("="*74)
print("KEGIATAN 3  Langkah kompleks")
print("="*74)
print("Langkah kompleks, yang bebas pengurangan berbahaya:")
for k in (4, 8, 12, 16, 20):
    h = 10.0**(-k)
    # TODO 3a: langkah kompleks. Ambil bagian khayal, lalu bagi h.
    kompleks = 0.0
    print(f"  h={h:8.1e}  galat={abs(kompleks-df_tepat):.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3a():
    return abs(kompleks - np.cos(1.0)) < 1e-15, f"langkah kompleks pada h = 1e-20 = {float(kompleks)!r}, seharusnya cos(1) = 0.5403023058681398"
cek_todo("TODO 3a  langkah kompleks", _uji_3a)
pass  # <<< pemeriksa
