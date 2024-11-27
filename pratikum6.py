# Daftar untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan():
    if len(data_mahasiswa) == 0:
        print("Belum ada data yang tersedia.\n")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, data in enumerate(data_mahasiswa, start=1):
            print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}")
        print()

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [data for data in data_mahasiswa if data["nama"].lower() != nama.lower()]
    print(f"Data mahasiswa dengan nama {nama} berhasil dihapus.\n")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    for data in data_mahasiswa:
        if data["nama"].lower() == nama.lower():
            nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
            data["nilai"] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.\n")
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Program utama
while True:
    print("=== Menu Program Daftar Nilai Mahasiswa ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
