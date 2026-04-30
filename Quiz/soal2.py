stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

def filter_harga(data, min_harga, max_harga):
    hasil = []
    for item in data:
        if min_harga <= item["harga"] <= max_harga:
            hasil.append(item)
        return hasil
        
min_harga = int(input("Masukkan Harga Minimum: "))
max_harga = int(input("Masukkan Harga Maximum: "))

Hasilnya = filter_harga(stok_gadget, min_harga, max_harga)

if Hasilnya:
    print("\n Gadget Dengan Rentang Harga Berikut: ")
    for item in Hasilnya:
        print (item)

else:
    print("Tidak ada gadget dalam rentang harga tersebut")
        


        
            
        

        

 


        