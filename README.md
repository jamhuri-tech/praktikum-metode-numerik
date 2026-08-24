# Kode Praktikum Metode Numerik

Berkas kerangka untuk **Modul Praktikum Metode Numerik**, dua belas pertemuan
laboratorium pada Program Studi Matematika, Fakultas Sains dan Teknologi,
Universitas Islam Negeri Maulana Malik Ibrahim Malang.

Mendampingi buku **Metode Numerik: Teori, Algoritma, dan Analisis Galat**
karya Mohammad Jamhuri dan Juhari, 332 halaman, terbit di
[Google Play Books](https://play.google.com/store/books/details?id=ehEFEgAAQBAJ).

---

## Yang ada di sini

Setiap praktikum tersedia dalam dua bentuk berisi hal yang sama persis:

| Berkas | Untuk |
|---|---|
| `pNN_kerangka.py` | bekerja di komputer sendiri |
| `pNN_kerangka.ipynb` | bekerja di Google Colab atau Kaggle |

Bagian inti setiap program sengaja dikosongkan dan ditandai `# TODO`. Itulah
yang Anda kerjakan di laboratorium. Selebihnya sudah tersedia supaya sembilan
puluh menit Anda habis untuk memahami, bukan untuk mengetik ulang.

| # | Berkas | Pokok bahasan | Bab buku |
|---|---|---|---|
| 1 | `p01_kerangka` | Galat dan aritmetika titik-kambang | 1 |
| 2 | `p02_kerangka` | Akar persamaan nonlinear | 2 |
| 3 | `p03_kerangka` | Sistem linear: metode langsung | 3 |
| 4 | `p04_kerangka` | Sistem linear: metode iteratif | 4 |
| 5 | `p05_kerangka` | Sistem nonlinear dan optimasi | 5 |
| 6 | `p06_kerangka` | Nilai eigen dan nilai singular | 6 |
| 7 | `p07_kerangka` | Interpolasi polinomial dan spline | 7, 8 |
| 8 | `p08_kerangka` | Kuadrat terkecil dan diferensiasi numerik | 9, 10 |
| 9 | `p09_kerangka` | Integrasi numerik | 11, 12 |
| 10 | `p10_kerangka` | Persamaan diferensial biasa | 13, 14 |
| 11 | `p11_kerangka` | Masalah nilai batas | 15, 17 |
| 12 | `p12_kerangka` | PDP bergantung waktu | 16, 18 |

---

## Membuka di Colab, satu klik

Ganti `NN` dengan nomor praktikumnya:

```
https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/pNN_kerangka.ipynb
```

[Praktikum 1](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p01_kerangka.ipynb)
· [2](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p02_kerangka.ipynb)
· [3](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p03_kerangka.ipynb)
· [4](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p04_kerangka.ipynb)
· [5](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p05_kerangka.ipynb)
· [6](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p06_kerangka.ipynb)
· [7](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p07_kerangka.ipynb)
· [8](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p08_kerangka.ipynb)
· [9](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p09_kerangka.ipynb)
· [10](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p10_kerangka.ipynb)
· [11](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p11_kerangka.ipynb)
· [12](https://colab.research.google.com/github/jamhuri-tech/praktikum-metode-numerik/blob/main/p12_kerangka.ipynb)

> **Notebook yang dibuka dari GitHub bersifat hanya baca.** Sebelum mulai
> bekerja, pilih **File → Save a copy in Drive**.

## Membuka di Kaggle

Tidak sesederhana Colab: tidak ada satu alamat yang tinggal diklik, dan Anda
harus sudah masuk ke akun Kaggle.

1. Buka [kaggle.com](https://www.kaggle.com), lalu **Create → New Notebook**
2. Di dalam penyunting, pilih **File → Open Notebook**
3. Pada dialognya pilih sumber **GitHub**, masukkan alamat repositori ini, lalu
   pilih berkas `.ipynb` yang diinginkan
4. Setelan **Accelerator** biarkan *None*: seluruh praktikum berukuran kecil
   dan tidak memerlukan GPU

Kalau menyulitkan, unduh saja berkas `.ipynb` dari repositori ini lalu
unggah lewat dialog yang sama. Hasilnya sama.

## Bekerja di komputer sendiri

```bash
git clone https://github.com/jamhuri-tech/praktikum-metode-numerik.git
cd praktikum-metode-numerik
python3 -m venv metnum && source metnum/bin/activate
pip install numpy scipy matplotlib
python3 p01_kerangka.py
```

---

## Cara memakainya

**Setiap kerangka sudah berjalan sampai selesai sejak awal**, meskipun seluruh
`TODO` masih kosong. Angkanya belum benar, dan memang begitu maksudnya:
jalankan sekali sebelum mengubah apa pun untuk memastikan Python dan NumPy
sudah siap.

Sesudah itu, kerjakan `TODO` berurutan dan jalankan ulang setiap kali satu
selesai. Menemukan satu kekeliruan di antara satu perubahan jauh lebih cepat
daripada mencarinya di antara sepuluh.

Angka yang benar untuk setiap kegiatan tercetak pada modul, di bagian
**"Yang seharusnya Anda lihat"**. Seluruh angka itu keluaran sungguhan, bukan
taksiran, jadi Anda dapat memeriksa diri sendiri tanpa menunggu asisten.

### Dua jebakan khas notebook

**Menjalankan sel tidak berurutan.** Notebook mengingat peubah dari sel mana
pun yang pernah dijalankan, dalam urutan apa pun. Kode yang tampak benar dapat
berjalan hanya karena sebuah peubah masih tersisa dari percobaan sebelumnya,
lalu gagal total di komputer orang lain. Sebelum mengumpulkan, **selalu**
jalankan ulang dari atas pada mesin bersih: *Restart and run all* pada Colab,
*Save Version* pada Kaggle.

**Mengira keluaran tersimpan adalah bukti.** Angka yang tercetak di bawah sel
bisa saja berasal dari kode yang sudah diubah sesudahnya. Itulah sebabnya yang
dikumpulkan berkas `.py`, bukan `.ipynb`.

---

## Lingkungan uji

Seluruh berkas dijalankan dan diperiksa dengan Python 3.13.5, NumPy 2.1.3,
Matplotlib 3.10.0, dan SciPy 1.15.3. Colab dan Kaggle sudah memuat keempatnya.

## Ketentuan pemakaian

Hak cipta © 2026 Mohammad Jamhuri dan Juhari.

Berkas di sini boleh dipakai dan digandakan untuk keperluan pengajaran dan
belajar dengan menyebutkan sumbernya. Pemakaian untuk tujuan komersial
memerlukan izin tertulis dari penyusun.

## Yang tidak ada di sini

Kunci jawaban dan buku pegangan dosen tidak diterbitkan di repositori ini.
Pengampu dapat memintanya melalui surel di bawah.

## Kekeliruan dan usulan

Buka *issue* pada repositori ini, atau kirim surel ke
`m.jamhuri@mat.uin-malang.ac.id`.
