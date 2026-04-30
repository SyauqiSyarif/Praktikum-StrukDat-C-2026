def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("error : harga harus diatas 1.000.000")
        return None
    
    if len(sn) <5:
        print("error : sn (Serial Number) harus berisi minimal 5 karakter. ")
        return None
    
    return {
       "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "tersedia"
    }

inventaris = []

for i in range(3):
    print(f"\ninput Gadget ke-{i+1}")
    merk = input("Merk: ")
    tipe = input("Tipe: ")
    harga = int(input("Harga: "))
    sn = input("Serial Number: ")
    
    data = registrasi_gadget(merk, tipe, harga, sn)
    if data !=None :
        inventaris.append(data)

print()

for item in inventaris:
    print(item)






    

    

    


    

    

    





