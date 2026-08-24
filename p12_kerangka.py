"""Praktikum 12 - PDP bergantung waktu.

Lengkapi setiap bagian bertanda TODO. Jalankan berkas ini sesudah setiap
kegiatan, jangan menunggu sampai seluruhnya selesai.

    python3 p12_kerangka.py
"""
import numpy as np

print("="*74); print("KEGIATAN 1  Persamaan panas, skema eksplisit dan bilangan r")
print("="*74)
# u_t = u_xx pada (0,1), u(0)=u(1)=0, u(x,0)=sin(pi x) -> u = e^{-pi^2 t} sin(pi x)
def panas_eksplisit(n, r, T=0.05):
    h = 1.0/(n+1); dt = r*h*h
    m = int(round(T/dt)); dt = T/m
    r = dt/h**2
    x = np.linspace(0, 1, n+2)[1:-1]
    u = np.sin(np.pi*x)
    for k in range(m):
        u = u + r*(np.roll(u, 1) - 2*u + np.roll(u, -1))
        u[0] = u[0] + 0.0   # batas nol: roll sudah salah di ujung, betulkan
        u_kiri = np.concatenate(([0.0], u[:-1]))
        u_kanan = np.concatenate((u[1:], [0.0]))
    return x, u

def panas_eksplisit_benar(n, r_minta, T=0.05):
    h = 1.0/(n+1); dt = r_minta*h*h
    m = max(int(round(T/dt)), 1); dt = T/m; r = dt/h**2
    x = np.linspace(0, 1, n+2)[1:-1]
    u = np.sin(np.pi*x)
    for k in range(m):
        kiri = np.concatenate(([0.0], u[:-1]))
        kanan = np.concatenate((u[1:], [0.0]))
        # TODO 1a: stensil tiga titik.
        u = u
    return x, u, r, m

def panas_implisit(n, r_minta, T=0.05):
    h = 1.0/(n+1); dt = r_minta*h*h
    m = max(int(round(T/dt)), 1); dt = T/m; r = dt/h**2
    x = np.linspace(0, 1, n+2)[1:-1]
    u = np.sin(np.pi*x)
    # TODO 1b: matriks skema implisit, I + rA.
    A = np.eye(n)
    for k in range(m):
        u = np.linalg.solve(A, u)
    return x, u, r, m

n = 39; T = 0.05
tepat = lambda x, t: np.exp(-np.pi**2*t)*np.sin(np.pi*x)
print(f"n = {n}, T = {T}")
print(f"{'r diminta':>10} {'r dipakai':>10} {'langkah':>8} "
      f"{'galat eksplisit':>18} {'galat implisit':>17}")
for rm in (0.10, 0.25, 0.49, 0.50, 0.51, 0.60, 2.00):
    x, ue, r, m = panas_eksplisit_benar(n, rm, T)
    _, ui, _, _ = panas_implisit(n, rm, T)
    ge = np.max(np.abs(ue - tepat(x, T)))
    gi = np.max(np.abs(ui - tepat(x, T)))
    ge_s = f"{ge:18.3e}" if np.isfinite(ge) and ge < 1e10 else f"{'MELEDAK':>18}"
    print(f"{rm:10.2f} {r:10.4f} {m:8d} {ge_s} {gi:17.3e}")
print("\nSyarat kestabilan von Neumann untuk skema eksplisit: r <= 1/2.")

print()
print("="*74); print("KEGIATAN 2  Orde kekonvergenan skema implisit"); print("="*74)
print(f"{'n':>5} {'galat implisit r=0.5':>22} {'orde':>7}")
sebelum = None
for n2 in (9, 19, 39, 79, 159):
    x, u, r, m = panas_implisit(n2, 0.5, T)
    g = np.max(np.abs(u - tepat(x, T)))
    orde = np.log2(sebelum/g) if sebelum else float('nan')
    print(f"{n2:5d} {g:22.6e} {orde:7.3f}")
    sebelum = g

print()
print("="*74); print("KEGIATAN 3  Adveksi dan syarat CFL"); print("="*74)
a = 1.0; T2 = 1.0

def adveksi_upwind(n, C_minta, awal="sinus"):
    """u_t + a u_x = 0 pada [0,1] periodik, skema upwind. Satu putaran penuh."""
    h = 1.0/n
    dt = C_minta*h/a
    m = max(int(round(T2/dt)), 1); dt = T2/m; C = a*dt/h
    x = np.linspace(0, 1, n, endpoint=False)
    u0 = (np.sin(2*np.pi*x) if awal == "sinus"
          else np.where((x > 0.3) & (x < 0.6), 1.0, 0.0))
    u = u0.copy()
    for k in range(m):
        # TODO 3a: skema upwind. Ke arah mana selisihnya diambil?
        u = u
        if not np.all(np.isfinite(u)):
            return x, u, u0, C, m
    return x, u, u0, C, m

print("Bagian A. Kestabilan, dengan syarat awal berundak yang memuat")
print("frekuensi tinggi. Sesudah satu putaran penuh, u harus kembali semula.")
print()
print(f"{'C diminta':>10} {'C dipakai':>10} {'langkah':>8} {'maks |u|':>16}")
for Cm in (0.50, 0.90, 1.00, 1.02, 1.05, 1.10, 1.20):
    x, u, u0, C, m = adveksi_upwind(200, Cm, "undak")
    mx = np.max(np.abs(u))
    mx_s = f"{mx:16.3e}" if np.isfinite(mx) else f"{'MELEDAK':>16}"
    print(f"{Cm:10.2f} {C:10.4f} {m:8d} {mx_s}")
print()
print("Syarat CFL untuk upwind: C = a*dt/h <= 1.")
print("Pada C = 1 tepat, skemanya menjadi penggeseran tepat satu sel,")
print("sehingga galatnya nol. Itu kebetulan yang menyenangkan dan bukan")
print("sesuatu yang dapat diandalkan pada persoalan nyata.")

print()
print("Bagian B. Difusi numerik: meskipun stabil, puncaknya meluruh.")
print(f"{'C':>8} {'maks |u| sesudah satu putaran':>32} {'galat maks':>14}")
for Cm in (0.25, 0.50, 0.90, 1.00):
    x, u, u0, C, m = adveksi_upwind(200, Cm, "sinus")
    print(f"{C:8.4f} {np.max(np.abs(u)):32.4f} {np.max(np.abs(u-u0)):14.3e}")
print("Nilai yang benar 1.0000. Makin kecil C, makin banyak yang hilang.")
