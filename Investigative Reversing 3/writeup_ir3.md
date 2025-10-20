# Write-up Lengkap: Investigative Reversing 3 (picoCTF 2019)

Ini adalah rincian langkah demi langkah untuk menyelesaikan tantangan Forensik "Investigative Reversing 3" dari picoCTF 2019.

---

### Analisis Awal

- **Aset:** Tantangan ini memberikan 1 file biner (`mystery`) dan 1 file gambar (`encoded.bmp`).
- **Enumerasi:** Menggunakan perintah `file`, diketahui bahwa `mystery` adalah biner Linux 64-bit yang **"not stripped"**. Ini berarti nama fungsi dan simbol di dalamnya tidak dihapus, yang sangat mempermudah analisis. File `encoded.bmp` adalah gambar Bitmap biasa.

---

### Membedah Logika Program

Kunci utama tantangan ini ada di dalam biner `mystery`. Dengan membukanya di Ghidra, fungsi `main` dapat dianalisis dengan mudah.

Dari hasil dekompilasi, terungkap fakta penting: program ini adalah sebuah **ENKODER**, bukan dekoder. Logikanya adalah sebagai berikut:
1.  Program membaca sebuah flag dari file `flag.txt` dan gambar asli dari `original.bmp` (file-file ini ada di server, bukan di komputer kita).
2.  Program menyalin **723 byte pertama** (yang merupakan header file BMP) dari gambar asli ke file output `encoded.bmp`.
3.  Selanjutnya, program menyembunyikan flag menggunakan steganografi LSB (Least Significant Bit) dengan pola yang unik:
    - **Sembunyikan 1 karakter** flag (yang terdiri dari 8 bit) ke dalam **8 byte** data gambar.
    - Setelah itu, **salin 1 byte** data gambar berikutnya tanpa ada perubahan.
    - Pola ini diulang terus-menerus hingga seluruh karakter flag berhasil disembunyikan di dalam gambar.

---

### Solusi

Tugas kita adalah membalik proses enkripsi ini. Untuk melakukannya, kita perlu membuat skrip yang dapat membaca file `encoded.bmp`, melewati 723 byte header, dan kemudian mengekstrak bit-bit yang tersembunyi sesuai dengan pola yang telah kita temukan. Skrip solusi (`solve_ir3.py`) melakukan tugas ini untuk merekonstruksi flag yang asli.