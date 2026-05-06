class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Gudang:
    def __init__(self, root_data):
        self.root = Node(root_data)

    # 1. Pre Order
    def traversePreOrder(self, node, hasil):
        if node:
            hasil.append(node.data)
            self.traversePreOrder(node.left, hasil)
            self.traversePreOrder(node.right, hasil)
        return hasil

    # 2. In Order
    def traverseInOrder(self, node, hasil):
        if node:
            self.traverseInOrder(node.left, hasil)
            hasil.append(node.data)
            self.traverseInOrder(node.right, hasil)
        return hasil

    # 3. Post Order
    def traversePostOrder(self, node, hasil):
        if node:
            self.traversePostOrder(node.left, hasil)
            self.traversePostOrder(node.right, hasil)
            hasil.append(node.data)
        return hasil

    # 4. Leaf Node
    def getLeafNodes(self, node, hasil):
        if node:
            if not node.left and not node.right:
                hasil.append(node.data)
            self.getLeafNodes(node.left, hasil)
            self.getLeafNodes(node.right, hasil)
        return hasil

# Main
print()
print("SISTEM AUDIT DISTRIBUSI CEPAT SAMPAI")
print("=====================================")
print("[INFO] Membangun Struktur Gudang...")

audit = Gudang("A")
audit.root.left = Node("B")
audit.root.right = Node("C")
audit.root.left.left = Node("D")
audit.root.left.right = Node("E")
audit.root.right.right = Node("F")

print("[INFO] Struktur berhasil dibuat.")
print()
print("HASIL AUDIT:")
print("1. Pre-Order   :", " - ".join(audit.traversePreOrder(audit.root, [])))
print("2. In-Order    :", " - ".join(audit.traverseInOrder(audit.root, [])))
print("3. Post-Order  :", " - ".join(audit.traversePostOrder(audit.root, [])))
print("[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(audit.getLeafNodes(audit.root, [])))
print("=====================================")
print("Audit selesai")