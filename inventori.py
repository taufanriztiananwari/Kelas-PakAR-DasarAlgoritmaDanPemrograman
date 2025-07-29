import json
import os

INVENTORY_FILE = "data_barang.json"

def load_data():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def tambah_barang():
    nama = input("Nama barang: ")
    stok = int(input("Jumlah stok: "))
    harga = float(input("Harga per item: "))
    data = load_data()
    data.append({"nama": nama, "stok": stok, "harga": harga})
    save_data(data)
    print("Barang berhasil ditambahkan.")

def tampilkan_barang():
    data = load_data()
    print("\nDaftar Barang:")
    for i, barang in enumerate(data):
        print(f"{i+1}. {barang['nama']} - Stok: {barang['stok']}, Harga: Rp{barang['harga']:.2f}")

def edit_barang():
    tampilkan_barang()
    data = load_data()
    index = int(input("Pilih nomor barang yang ingin diedit: ")) - 1
    if 0 <= index < len(data):
        data[index]['nama'] = input("Nama baru: ")
        data[index]['stok'] = int(input("Stok baru: "))
        data[index]['harga'] = float(input("Harga baru: "))
        save_data(data)
        print("Barang berhasil diedit.")
    else:
        print("Nomor tidak valid.")

def hapus_barang():
    tampilkan_barang()
    data = load_data()
    index = int(input("Pilih nomor barang yang ingin dihapus: ")) - 1
    if 0 <= index < len(data):
        del data[index]
        save_data(data)
        print("✅ Barang berhasil dihapus.")
    else:
        print("Nomor tidak valid.")

def laporan_ringkas():
    data = load_data()
    total_barang = len(data)
    total_nilai = sum(item['stok'] * item['harga'] for item in data)
    print(f"\n📊 Total barang: {total_barang}")
    print(f"💰 Total nilai inventori: Rp{total_nilai:.2f}")

def menu():
    while True:
        print("\n Menu Aplikasi Inventori")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Laporan Ringkas")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_barang()
        elif pilihan == "3":
            edit_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            laporan_ringkas()
        elif pilihan == "6":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

menu()
