class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if id_buku < current.id_buku:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif id_buku > current.id_buku:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
                else:                    break
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def inorder(self):
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        self._inorder_helper(self.root, 1)

    def _inorder_helper(self, node, counter):
        if node is not None:
            counter = self._inorder_helper(node.left, counter)
            print(f"{counter}. {node.id_buku} - {node.judul}")
            counter += 1
            counter = self._inorder_helper(node.right, counter)
        return counter

    def search(self, id_buku):
        current = self.root
        while current is not None:
            if current.id_buku == id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    def height(self):
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height)


def main():
    print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"\n')
    bst = BinarySearchTree()
    
    data_buku = [
        (50, "Dasar Pemrograman"),
        (30, "Struktur Data"),
        (70, "Kecerdasan Buatan"),
        (20, "Matematika Diskrit"),
        (40, "Basis Data"),
        (60, "Jaringan Komputer"),
        (80, "Sistem Operasi")
    ]
    
    for id_buku, judul in data_buku:
        bst.insert(id_buku, judul)
    
    print()
    bst.inorder()
    print()
    
    hasil = bst.search(60)
    print(f"[SEARCH] Mencari ID 60...", end=" ")
    if hasil:
        print(f"Ditemukan! Judul: {hasil.judul}")
    else:
        print("Data tidak ditemukan.")
    
    hasil = bst.search(100)
    print(f"[SEARCH] Mencari ID 100...", end=" ")
    if hasil:
        print(f"Ditemukan! Judul: {hasil.judul}")
    else:
        print("Data tidak ditemukan.")
    print()
    
    min_node = bst.get_min()
    max_node = bst.get_max()
    print(f"[STATISTIK] ID Terkecil: {min_node.id_buku}")
    print(f"[STATISTIK] ID Terbesar: {max_node.id_buku}")
    print()
    
    print(f"[INFO] Tinggi (Height) Tree: {bst.height()}")
    print("\nSimulasi Selesai!")

if __name__ == "__main__":
    main()