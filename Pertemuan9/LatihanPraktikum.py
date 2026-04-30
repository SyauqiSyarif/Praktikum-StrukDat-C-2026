#1. Parkir Dua Arah - Penelusuran Maju & Mundur
print()
print("1. Parkir Dua Arah - Penelusuran Maju & Mundur")
print()
class Node:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:  
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        print("[Mundur]")
        current = self.tail
        while current:
            print(current.plat)
            current = current.prev


if __name__ == "__main__":
    parkir = DoubleLinkedList()
    parkir.tambah_kendaraan("B 1234 ABC")
    parkir.tambah_kendaraan("D 5678 XYZ")
    parkir.tambah_kendaraan("A 9999 TUV")
    parkir.tampilkan_maju()
    parkir.tampilkan_mundur()


#2. Hapus Kendaraan dari Tengah — Update Dua Arah
print()
print("2. Hapus Kendaraan dari Tengah — Update Dua Arah")
print()

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def hapus_kendaraan(self, plat):
        current = self.head
        while current:
            if current.plat == plat:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif current.next is None:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True  
            current = current.next
        return False  

    def tampilkan_maju(self):
        current = self.head
        while current:
            print(current.plat)
            current = current.next


if __name__ == "__main__":
    parkir = DoubleLinkedList()
    parkir.tambah_kendaraan("B 1111 AA")
    parkir.tambah_kendaraan("D 2222 BB")
    parkir.tambah_kendaraan("A 3333 CC")
    parkir.tambah_kendaraan("B 4444 DD")

    print("Sebelum:")
    parkir.tampilkan_maju()

    print()
    parkir.hapus_kendaraan("A 3333 CC")

    print("Sesudah:")
    parkir.tampilkan_maju()

#3. Antrean Giliran Petugas Valet — Rotasi Melingkar
print()
print("3. Antrean Giliran Petugas Valet — Rotasi Melingkar")
print()

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def giliran_berikutnya(self, n):
        """Mencetak giliran ke-1 s/d n, mulai dari head, berputar melingkar."""
        if self.head is None:
            print("Tidak ada petugas.")
            return

        current = self.head
        for i in range(1, n + 1):
            print(f"Giliran {i}: {current.nama}")
            current = current.next  

if __name__ == "__main__":
    valet = CircularLinkedList()
    valet.tambah_petugas("Andi")
    valet.tambah_petugas("Budi")
    valet.tambah_petugas("Citra")
    valet.tambah_petugas("Dewi")

    valet.giliran_berikutnya(6)
