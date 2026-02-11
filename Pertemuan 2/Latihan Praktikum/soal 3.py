# Data Keahlian Masing Masing Tim
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# 1. Mencari keahlian yang dimiliki kedua tim (irisan)
irisan = tim_frontend.intersection(tim_backend)

# 2. Menentukan keahlian yang dimiliki oleh tim_backend
Khusus_Timbackend = tim_backend.difference(tim_frontend)

# 3. Gabungkan keahlian unik kedua tim
Total_Keahlian = tim_frontend.union(tim_backend)

print(f""" 
    Keahlian yang dimiliki oleh kedua tim : {irisan}
    Keahlian khusus yang dimiliki tim_backend : {Khusus_Timbackend}
    Keahlian Unik untuk kedua tim : {Total_Keahlian}
 """)

