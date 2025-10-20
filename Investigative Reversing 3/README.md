# 🚩 Kumpulan Write-up CTF oleh Yusril-git

Selamat datang di repositori saya! Di sini saya mendokumentasikan perjalanan saya dalam menyelesaikan berbagai tantangan Capture The Flag (CTF).

---

## Daftar Isi

### picoCTF 2019

#### 1. Investigative Reversing 3 (Forensic)

* **Kategori:** Forensic
**Deskripsi:** Diberikan sebuah file biner (`mystery`) ...
    ![Deskripsi Soal](images/1-soal.png)

* **Analisis:** ...lalu 1 byte disalin biasa.
    ![Logika di Ghidra](images/2-ghidra.png)
    Analisis pada biner `mystery` menggunakan Ghidra menunjukkan bahwa program ini adalah sebuah **enkoder steganografi**. Ditemukan pola enkripsi LSB (Least Significant Bit) yang unik: setelah 723 byte header, 8 byte gambar digunakan untuk menyembunyikan 1 karakter flag, lalu 1 byte disalin biasa.

* **Solusi:**
    Solusinya adalah dengan membuat skrip Python untuk membalik proses tersebut. Skrip ini membaca `encoded.bmp`, melewati header, dan mengekstrak bit-bit tersembunyi sesuai pola yang ditemukan untuk merekonstruksi flag.
    ```python
    # solve_ir3.py
    def solve_ir3():
        with open('encoded.bmp', 'rb') as f:
            f.seek(723)
            flag = ""
            for i in range(50):
                char_byte = 0
                for j in range(8):
                    img_byte = f.read(1)
                    lsb = ord(img_byte) & 1
                    char_byte = (char_byte << 1) | lsb
                
                flag += chr(int(bin(char_byte)[2:].zfill(8)[::-1], 2))
                f.read(1)
        print(flag)

    solve_ir3()
    ```

* **Flag:**
    `picoCTF{...jalankan skrip untuk mendapatkan flag...}`
    * **Flag:**
    `picoCTF{...jalankan skrip untuk mendapatkan flag...}`
    ![Hasil Skrip](images/3-hasil.png)

---