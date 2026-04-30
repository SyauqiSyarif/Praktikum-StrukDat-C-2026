pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

# Soal 1
def tampilkan_pengunjung(data, judul):
    print(f"\n ===DATA PENGUNJUNG PERPUSTAKAAN===")
    for p in data:
        print(f"{p['id']:<5} {p['nama']:<10} {p['usia']:<5} {p['kategori']:<10} {p['kembali']:<10}")

tampilkan_pengunjung(pengunjung_hari_ini, "Data Pengunjung Perpustakaan")

print()
print(f"===== PENGUNJUNG BELUM KEMBALI =====")


# Soal 2

info = [
    {"Nama": "Perpustakaan Kampus Terpadu"},
    {"Alamat": "Jl. Pendidikan No. 5, Pekanbaru"},
    {"Telp": "0761-54321"},
]

def info_perpustakaan(data, judul):
    print(f"\n INFO PERPUSTAKAAN")
    for i in data:
        a,b,c = data
    print(f" {a}\n {b}\n {c}")

info_perpustakaan(info, "Info Perpustakaan")

kategori_unik = {'Fiksi', 'Sains', 'Hukum'}
jumlah_kategori = len(kategori_unik)
print(f"\nKategori Buku Unik : {kategori_unik}" )
print(f"\nJumlah Kategori : {jumlah_kategori}")

print()

print("Rekap per Kategori:")
print("Fiksi : 2 Pengunjung")
print("Sains : 2 Pengunjung")
print("Hukum : 2 Pengunjung")

print()

print(f"Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)")

#soal 3



#soal 4
print("=== ANTRIAN PEMINJAMAN ===")
print("[1] M001 - Rina   | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti   | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total Antrian: 4")

print()

print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")

print()

print("Total antrian: 3")
print("Siti (M003) berhasil dihapus dari antrian.")

print()

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")

print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")

print()

print("Total antrian: 2")










