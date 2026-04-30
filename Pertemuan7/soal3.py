class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def tampilkan_antrean(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")


def sisipkan_vip(head, nodeBaru, position):
  currentNode = head

  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  if currentNode:
    nodeBaru.next = currentNode.next
    currentNode.next = nodeBaru

  return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("F 0477 MM")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4


print("Antrean kendaraan:")
tampilkan_antrean(node1)


nodeVIP = Node("VIP 1123 FOG")
node1 = sisipkan_vip(node1, nodeVIP, 3)


print("\nSetelah VIP disisipkan:")
tampilkan_antrean(node1)