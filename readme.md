# TLC Backup
Script [Python](https://www.python.org) untuk melakukan backup submission yang Accepted dari [Tokilearning](http://tokilearning.org/).

Dikarenakan tokilearning alias TLC akan dinonaktifkan, penting bagi pengguna untuk melakukan backup submission.

## Penggunaan

1. Jika anda belum memiliki python, [Download Python](https://www.python.org/downloads/) versi 3.x.y
2. Pastikan python dan pip dapat diakses cari command line (cmd/terminal)

    ```
    python -V
    ```

    ```
    pip -V
    ```

3. Install dependensi script
    ```
    pip install requests, beautifulsoup4
    ```
4. Login ke tokilearning. Simpan PHPSESSID dengan cara :
    
    a. Jika anda pengguna Firefox, pada laman tokilearning klik kanan -> View Page Info -> Security -> View Cookies -> Ambil bagian Content untuk Name : PHPSESSID. Nilai berupa sebuah string acak.

    b. Jika anda pengguna Chrome, pada laman tokilearning klik kanan -> Inspect -> tab Resource (jika tidak ada, klik icon >>) -> Resources -> Cookies -> tokilearning.org -> Ambil bagian Value untuk Name : PHPSESSID. Nilai berupa sebuah string acak.

5. Download script

    a. Jika anda pengguna git. Clone repo ini

    b. Jika anda bukan pengguna git. Script dapat di download dengan mengeklik tombol Download ZIP di kanan atas, lalu extract ke suatu direktori

6. Masuk ke direktori penyimpanan script dengan command line (cmd/terminal). Jalankan script dengan memasukkan PHPSESSID yang diperoleh

    ```
    python tlc_backup.py your_PHPSESSID
    ```

7. File submission akan berada di direktori script berada dengan format [ID Soal]_[Nama Soal]_[ID Submission].[pas|c|cpp]

## Lain-lain
Terinspirasi dari [GTL](https://github.com/matematikaadit/gtl)