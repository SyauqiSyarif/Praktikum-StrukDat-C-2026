stok =[15, 50, 30, 25, 40]

stok.append(100)
stok.insert(2, 75)
stok.sort(reverse=True)

jumlah = sum(stok)
rata=jumlah/len(stok)

print("Rata - Rata :", rata)
print(stok)