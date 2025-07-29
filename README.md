# Aplikasi Inventori Toko Kecil

Aplikasi ini dibuat menggunakan Python untuk mencatat, menampilkan, dan mengelola data inventori toko kecil.

## Struktur File
- `inventori.py` → Program utama
- `data_barang.json` → File penyimpanan data

## Library yang Digunakan
- `json` → untuk menyimpan data ke file
- `os` → untuk memeriksa keberadaan file

## Diagram Alur
1. Program dijalankan
2. Muncul menu utama
3. User memilih salah satu opsi:
   - Tambah barang → isi data → simpan
   - Tampilkan daftar
   - Edit data berdasarkan index
   - Hapus data berdasarkan index
   - Laporan ringkas (jumlah dan nilai total)

## User Manual
### Cara Menjalankan
- Jalankan `inventori.py` di terminal:
  ```
  python inventori.py
  ```

### Fitur Utama
- Tambah, edit, hapus, dan tampilkan daftar barang
- Menampilkan laporan ringkas

## Contoh Uji Coba
- Tambah barang: input "Pensil", stok 10, harga 2000
- Edit barang ke-1: ubah jadi "Pulpen", stok 20, harga 2500
- Hapus barang ke-1
