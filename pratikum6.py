data_mahasiswa = []

def tambah():
    nama = input("1. Masukkan nama mahasiswa: ")
    nilai = validasi_nilai("2. Masukkan nilai mahasiswa: ")
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    cetak_pesan("Data berhasil ditambahkan!")

def tampilkan():
    if not data_mahasiswa:
        cetak_pesan("Belum ada data mahasiswa!")
    else:
        print("\n--- Daftar Nilai Mahasiswa ---")
        print("=" * 34)
        print("| NO |       NAMA       | NILAI |")
        print("-" * 33)
        for i, mhs in enumerate(data_mahasiswa, 1):
            print(f"|{i:3}.| {mhs['nama']:16} | {mhs['nilai']:6}|")
        print("=" * 34)

def hapus():
    nama = input("1. Masukkan nama mahasiswa yang ingin dihapus: ")
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            data_mahasiswa.remove(mhs)
            print("=" * 65)
            print(f"--- Data mahasiswa '{nama}' telah dihapus! ---")
            print("=" * 65)
            return
    print("=" * 65)
    print(f"--- Data mahasiswa '{nama}' tidak ditemukan! ---")
    print("=" * 65)

def ubah():
    nama = input("1. Masukkan nama mahasiswa yang ingin diubah: ")
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            mhs['nilai'] = validasi_nilai(f"2. Masukkan nilai baru untuk {nama}: ")
            print("=" * 55)
            print("|    --- Data berhasil diubah! ---    |")
            print("=" * 55)
            return
    print("=" * 55)
    print(f"--- Data mahasiswa '{nama}' tidak ditemukan! ---")
    print("=" * 55)


def validasi_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai >= 0:
                return nilai
            print("Nilai tidak boleh negatif.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def cetak_pesan(pesan):
    print("=" * 65)
    print(f"{pesan.center(65)}")
    print("=" * 65)


def menu():
    while True:
        print("\n" + "=" * 20 + "\n|   --- MENU ---   |\n" + "=" * 20)
        print("1. Tambah Data\n2. Tampilkan Data\n3. Hapus Data\n4. Ubah Data\n5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            ubah_hapus("hapus")
        elif pilihan == "4":
            ubah_hapus("ubah")
        elif pilihan == "5":
            cetak_pesan("Program selesai. Terima kasih!")
            break
        else:
            cetak_pesan("Pilihan tidak valid. Coba lagi!")

menu()
