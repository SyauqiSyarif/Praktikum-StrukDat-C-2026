def dipisahkan(array):
    ganjil = []
    genap = []

    for plat in array:
        angka = plat.split()
        terakhir = angka[1]
        angkaterakhir = int(terakhir[-1])

        if angkaterakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap
    
data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
    
ganjil, genap = dipisahkan(data)

print("plat ganjil", ganjil)
print("plat genap", genap)


    

        


    
    






