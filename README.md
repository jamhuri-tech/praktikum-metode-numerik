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
| `pNN_kerangka.ipynb` | bekerja di Kaggle, dan inilah yang dikumpulkan |

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

## Membuka di Kaggle, satu klik

Seluruh praktikum dikerjakan sebagai notebook di Kaggle. Kaggle menyimpan
setiap versi notebook di akun Anda, sehingga pekerjaan lama mudah dicari dan
dibuka lagi. Masuk ke akun Kaggle lebih dahulu, lalu klik praktikumnya:

[Praktikum 1](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p01_kerangka.ipynb)
· [2](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p02_kerangka.ipynb)
· [3](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p03_kerangka.ipynb)
· [4](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p04_kerangka.ipynb)
· [5](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p05_kerangka.ipynb)
· [6](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p06_kerangka.ipynb)
· [7](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p07_kerangka.ipynb)
· [8](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p08_kerangka.ipynb)
· [9](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p09_kerangka.ipynb)
· [10](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p10_kerangka.ipynb)
· [11](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p11_kerangka.ipynb)
· [12](https://www.kaggle.com/kernels/welcome?src=https://github.com/jamhuri-tech/praktikum-metode-numerik/blob/main/p12_kerangka.ipynb)

Kaggle membuat salinan notebook kerangka di akun Anda. Sesudah terbuka:

1. Ganti judul notebook menjadi `pNN - Nama - NIM`
2. Biarkan **Accelerator** bernilai *None*: seluruh praktikum berukuran kecil
   dan tidak memerlukan GPU

Kalau tautannya tidak berjalan, unduh berkas `.ipynb` dari repositori ini,
lalu unggah ke notebook baru melalui menu **File** pada penyunting Kaggle.

## Bekerja di komputer sendiri

Cara ini boleh dipakai untuk mencoba, tetapi yang dikumpulkan tetap tautan
notebook Kaggle.

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

### Pemeriksa isian

Setiap kegiatan diakhiri pemeriksaan otomatis atas `TODO`-nya. Sesudah tabel
kegiatan tercetak, muncul baris seperti ini:

```
Periksa isian kegiatan ini:
  [BENAR] TODO 1a  selisih terbagi
  [BELUM] TODO 1b  skema Horner
          polinomial 1 + 2x + x(x-1) di x = 3 dihitung [1.0], seharusnya 13
```

- **`[BENAR]`** berarti isian itu lolos uji.
- **`[BELUM]`** berarti belum. Baris di bawahnya menyebut angka yang keluar
  dari kode Anda dan angka yang seharusnya. Selama `TODO` belum diisi,
  seluruhnya tertulis `[BELUM]`, dan itu wajar.
- **`[SENDIRI]`** hanya ada pada Praktikum 1 dan tidak diperiksa otomatis.
  Cocokkan sendiri hasilnya dengan petunjuk pada barisnya.

Ujinya memakai persoalan kecil yang berbeda dari tabel pada modul, jadi tidak
dapat diloloskan dengan menyalin angka tabel. Sebagian `TODO` bergantung pada
`TODO` sebelumnya; kalau pesannya meminta mengisi yang lain lebih dahulu,
kerjakan yang itu.

`[BENAR]` hanya memastikan kodenya menghitung dengan benar. Pertanyaan pada
setiap kegiatan tetap harus Anda jawab sendiri.

Jangan mengubah bagian pemeriksa: yang diapit `# >>> pemeriksa` dan
`# <<< pemeriksa`, serta baris yang diakhiri `# pemeriksa`. Pada notebook,
jalankan sel berurutan dari atas, sebab pemeriksa memakai peubah dari sel
kegiatannya.

### Dua jebakan khas notebook

**Menjalankan sel tidak berurutan.** Notebook mengingat peubah dari sel mana
pun yang pernah dijalankan, dalam urutan apa pun. Kode yang tampak benar dapat
berjalan hanya karena sebuah peubah masih tersisa dari percobaan sebelumnya,
lalu gagal total di komputer orang lain. Sebelum mengumpulkan, **selalu**
jalankan ulang dari atas pada sesi yang bersih dengan **Save Version → Save &
Run All (Commit)**.

**Mengira keluaran tersimpan adalah bukti.** Angka yang tercetak di bawah sel
bisa saja berasal dari kode yang sudah diubah sesudahnya. Itulah sebabnya yang
dikumpulkan tautan *versi tersimpan*, bukan notebook yang sedang disunting:
Kaggle menjalankan ulang versi itu dari atas pada sesi yang bersih.

## Yang dikumpulkan

Yang dikumpulkan bukan berkas, melainkan **tautan notebook Kaggle** yang sudah
disimpan sebagai versi dan dibuka untuk publik.

1. Tulis jawaban setiap pertanyaan pada sel **Markdown** di bawah kegiatannya.
   Jawaban yang hanya berisi angka tanpa penjelasan dinilai separuh.
2. Klik **Save Version**, pilih **Save & Run All (Commit)**, lalu tunggu sampai
   selesai.
3. Buka versi yang tersimpan. Pastikan notebook berjalan sampai akhir tanpa
   galat dan seluruh pemeriksa tertulis `[BENAR]`. Kalau belum, perbaiki, lalu
   simpan versi baru.
4. Klik **Share**, lalu ubah aksesnya menjadi **Public**.
5. Salin alamat notebook, yang berbentuk
   `https://www.kaggle.com/code/nama-akun/judul-notebook`, lalu kumpulkan
   alamat itu.

Tautan itu selalu menampilkan versi tersimpan yang terakhir. Karena itu,
jangan menyimpan versi yang belum benar sesudah mengumpulkan.

---

## Lingkungan uji

Seluruh berkas dijalankan dan diperiksa dengan Python 3.13.5, NumPy 2.1.3,
Matplotlib 3.10.0, dan SciPy 1.15.3. Kaggle sudah memuat keempatnya.

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
