class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.head
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return removed

    def peek(self):
        if self.is_empty():
            return None
        return self.head

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def display_all(self):
        if self.is_empty():
            print("[ANTRIAN] Antrian kosong.")
            return
        current = self.head
        nomor = 1
        while current:
            print(f"{nomor}. {current.nama.upper()} → {current.keluhan}")
            current = current.next
            nomor += 1

def main():
    antrian = queue()
    nomor_antrian = 1

    print("====================================")
    print(" SISTEM ANTRIAN POLI UMUM")
    print(" RS Sehat Bersama")
    print("====================================\n")

    print("[CEK] Apakah antrian kosong? → ", end="")
    print("YA, antrian masih kosong." if antrian.is_empty() else "TIDAK, ada pasien.")

    print()
    antrian.enqueue("Budi", "demam tinggi")
    print(f"[DAFTAR] Budi terdaftar dengan keluhan: demam tinggi (No. Antrian: {nomor_antrian})")
    nomor_antrian += 1

    antrian.enqueue("Ani", "batuk pilek")
    print(f"[DAFTAR] Ani terdaftar dengan keluhan: batuk pilek (No. Antrian: {nomor_antrian})")
    nomor_antrian += 1

    antrian.enqueue("Citra", "sakit kepala")
    print(f"[DAFTAR] Citra terdaftar dengan keluhan: sakit kepala (No. Antrian: {nomor_antrian})")
    nomor_antrian += 1

    print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

    depan = antrian.peek()
    if depan:
        print(f"[PEEK] Pasien berikutnya: {depan.nama.upper()} — {depan.keluhan}")

    print()
    panggil = antrian.dequeue()
    if panggil:
        print(f"[PANGGIL] Dokter memanggil: {panggil.nama.upper()} (keluhan: {panggil.keluhan})")

    antrian.enqueue("Dodi", "nyeri perut")
    print(f"[DAFTAR] Dodi terdaftar dengan keluhan: nyeri perut (No. Antrian: {nomor_antrian})")
    nomor_antrian -= 1

    print("\n[ANTRIAN SAAT INI]")
    antrian.display_all()
    print()

    panggil = antrian.dequeue()
    if panggil:
        print(f"[PANGGIL] Dokter memanggil: {panggil.nama.upper()} (keluhan: {panggil.keluhan})")

    print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

    print()
    antrian.clear()
    print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    print("[CEK] Apakah antrian kosong? → ", end="")
    print("YA, antrian sudah kosong" if antrian.is_empty() else "TIDAK, masih ada pasien.")

    print()
    print("====================================")
    print("Simulasi Selesai!")
    print("====================================\n")

if __name__ == "__main__":
    main()