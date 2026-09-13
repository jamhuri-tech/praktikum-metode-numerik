"""Praktikum 1 - Galat dan aritmetika titik-kambang.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai: kekeliruan lebih mudah
ditemukan selagi masih satu bagian.

    python3 p01_kerangka.py
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
from decimal import Decimal

# ============================================================ KEGIATAN 1
print("=" * 66)
print("KEGIATAN 1  Apa yang benar-benar tersimpan")
print("=" * 66)

print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print("0.1 + 0.2        ->", repr(0.1 + 0.2))
print("nilai tepat 0.1  ->", Decimal(0.1))

# TODO 1a: cetak selisih (0.1 + 0.2) - 0.3 sebagai Decimal, lalu bandingkan
#          dengan 2.0**-54. Pakai Decimal(...) pada keduanya.

# TODO 1b: cari epsilon mesin tanpa memakai np.finfo. Mulai dari eps = 1.0,
#          bagi dua terus selama 1.0 + eps/2 masih berbeda dari 1.0.
eps = 1.0
# while ... :
#     ...
print("epsilon mesin    ->", eps)
print("np.finfo         ->", np.finfo(float).eps)
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
print("  [SENDIRI] TODO 1a  kedua baris Decimal yang Anda cetak harus sama persis")
def _uji_1b():
    return eps == 2.220446049250313e-16, f"eps = {eps!r}, seharusnya 2.220446049250313e-16"
cek_todo("TODO 1b  epsilon mesin", _uji_1b)
pass  # <<< pemeriksa


# ============================================================ KEGIATAN 2
print()
print("=" * 66)
print("KEGIATAN 2  Galat yang menumpuk")
print("=" * 66)


def jumlah_naif(x, n):
    """Jumlahkan x sebanyak n kali dengan cara biasa."""
    s = 0.0
    # TODO 2a: satu perulangan, satu baris di dalamnya.
    return s


def jumlah_kahan(x, n):
    """Penjumlahan terkompensasi, Algoritma 1.1 pada buku.

    Gagasannya: c menyimpan bagian yang hilang pada penjumlahan sebelumnya,
    lalu mengembalikannya pada penjumlahan berikutnya.
    """
    s = 0.0
    c = 0.0
    for _ in range(n):
        y = x - c
        t = s + y
        # TODO 2b: dua baris. Hitung c dari t, s, dan y, lalu perbarui s.
        pass
    return s


print(f"{'n':>9} {'naif':>24} {'galat naif':>12} {'galat Kahan':>13}")
for n in (10, 100, 1000, 10_000, 100_000, 1_000_000):
    naif = jumlah_naif(0.1, n)
    kahan = jumlah_kahan(0.1, n)
    benar = n / 10
    print(f"{n:9d} {naif:24.16f} {abs(naif - benar):12.3e} "
          f"{abs(kahan - benar):13.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_2a():
    s = jumlah_naif(0.1, 3)
    return s == 0.30000000000000004, f"jumlah_naif(0.1, 3) = {s!r}, seharusnya 0.30000000000000004"
def _uji_2b():
    s = jumlah_kahan(0.1, 10)
    if s == 0.9999999999999999:
        return False, "jumlah_kahan(0.1, 10) = 0.9999999999999999, sama dengan penjumlahan biasa; koreksi c belum bekerja"
    return s == 1.0, f"jumlah_kahan(0.1, 10) = {s!r}, seharusnya tepat 1.0"
cek_todo("TODO 2a  jumlah_naif", _uji_2a)
cek_todo("TODO 2b  jumlah_kahan", _uji_2b)
pass  # <<< pemeriksa


# ============================================================ KEGIATAN 3
print()
print("=" * 66)
print("KEGIATAN 3  Pengurangan bilangan yang berdekatan")
print("=" * 66)


def akar_naif(a, b, c):
    """Rumus abc apa adanya."""
    d = np.sqrt(b * b - 4 * a * c)
    # TODO 3a: kembalikan kedua akar dengan rumus abc yang biasa.
    return 0.0, 0.0


def akar_stabil(a, b, c):
    """Rumus abc yang menghindari pengurangan bilangan berdekatan.

    Ketika 4ac jauh lebih kecil daripada b*b, nilai sqrt(D) hampir sama
    dengan |b|, sehingga salah satu pembilang -b +/- sqrt(D) nyaris nol dan
    angka bermaknanya habis. Jalan keluarnya: hitung akar yang aman lebih
    dahulu, lalu peroleh akar satunya dari hasil kali kedua akar, c/a.
    """
    d = np.sqrt(b * b - 4 * a * c)
    q = -0.5 * (b + np.copysign(d, b))
    # TODO 3b: kembalikan q/a dan c/q.
    return 0.0, 1.0


print(f"{'c':>10} {'akar kecil naif':>24} {'akar kecil stabil':>24} "
      f"{'galat relatif naif':>20}")
for k in range(1, 9):
    c = 10.0**(-2 * k)
    a, b = 1.0, 1.0
    kecil_naif = akar_naif(a, b, c)[0]
    kecil_stabil = akar_stabil(a, b, c)[1]
    galat = abs(kecil_naif - kecil_stabil) / abs(kecil_stabil)
    print(f"{c:10.1e} {kecil_naif:24.16e} {kecil_stabil:24.16e} {galat:20.3e}")
# >>> pemeriksa
print()
print("Periksa isian kegiatan ini:")
def _uji_3a():
    r = sorted(float(v) for v in akar_naif(1.0, -3.0, 2.0))
    return r == [1.0, 2.0], f"akar_naif(1, -3, 2) = {r}, seharusnya akar 1 dan 2"
def _uji_3b():
    r = sorted(float(v) for v in akar_stabil(1.0, -3.0, 2.0))
    if r != [1.0, 2.0]:
        return False, f"akar_stabil(1, -3, 2) = {r}, seharusnya akar 1 dan 2"
    kecil = float(akar_stabil(1.0, 1.0, 1e-16)[1])
    return abs(kecil + 1e-16) < 1e-28, f"akar kecil x^2 + x + 1e-16 = {kecil!r}, seharusnya -1e-16"
cek_todo("TODO 3a  akar_naif", _uji_3a)
cek_todo("TODO 3b  akar_stabil", _uji_3b)
pass  # <<< pemeriksa
