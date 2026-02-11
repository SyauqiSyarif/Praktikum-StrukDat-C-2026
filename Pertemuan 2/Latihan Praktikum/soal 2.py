barang = ("B001", "Laptop Gaming", 15000000)

# barang[2] = 14000000
# hal ini error karena tuple ialah type data yang static dan tidak bisa dimanipulasi

kode, nama_barang, harga = barang

print(f"""
    kode : {kode}
    nama barang : {nama_barang}
    harga : {harga}
      """)