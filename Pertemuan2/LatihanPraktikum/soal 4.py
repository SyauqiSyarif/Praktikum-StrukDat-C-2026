nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

# 1. Menambahkan data siswa baru 
print()
nilai_siswa["SO4"] = {
    "nama": "fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90,
}

# 2. Menghitung nilai akhir setiap siswa
print("nilai akhir siswa:")
for kode in nilai_siswa:
    tugas = nilai_siswa[kode]["tugas"]
    uts = nilai_siswa[kode]["uts"]
    uas = nilai_siswa[kode]["uas"]

    nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

    print(nilai_siswa[kode]["nama"], "=", nilai_akhir)

# 3. Menampilkan siswa dengan nilai UAS > 80
print()
print("Siswa dengan nilai UAS di atas 80:")
for kode in nilai_siswa:
    if nilai_siswa[kode]["uas"] > 80:
        print(nilai_siswa[kode]["nama"])