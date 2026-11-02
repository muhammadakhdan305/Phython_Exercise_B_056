# Variabel
fruit = 'mangga'
harga = 15000
umur = 20
daftar_buah = ['mangga', 'apel', 'pisang', 'anggur']
fruit_caps = 'MANGGA'

# Kesamaan dan ketidaksamaan string
print("Is fruit == 'mangga'? I predict True.")
print(fruit == 'mangga')

print("\nIs fruit == 'apel'? I predict False.")
print(fruit == 'apel')

print("\nIs fruit != 'apel'? I predict True.")
print(fruit != 'apel')

# Metode lower()
print("\nIs fruit_caps.lower() == 'mangga'? I predict True.")
print(fruit_caps.lower() == 'mangga')

print("\nIs fruit_caps.lower() == 'apel'? I predict False.")
print(fruit_caps.lower() == 'apel')

# Angka: sama dengan dan tidak sama dengan
print("\nIs harga == 15000? I predict True.")
print(harga == 15000)

print("\nIs harga == 12000? I predict False.")
print(harga == 12000)

print("\nIs harga != 12000? I predict True.")
print(harga != 12000)

# Angka: lebih besar dari dan lebih kecil dari
print("\nIs harga > 10000? I predict True.")
print(harga > 10000)

print("\nIs harga > 15000? I predict False.")
print(harga > 15000)

print("\nIs harga < 20000? I predict True.")
print(harga < 20000)

print("\nIs harga < 15000? I predict False.")
print(harga < 15000)

# Angka: lebih besar atau sama dengan, lebih kecil atau sama dengan
print("\nIs harga >= 15000? I predict True.")
print(harga >= 15000)

print("\nIs harga >= 16000? I predict False.")
print(harga >= 16000)

print("\nIs harga <= 15000? I predict True.")
print(harga <= 15000)

print("\nIs harga <= 14000? I predict False.")
print(harga <= 14000)

# Kata kunci and
print("\nIs harga > 10000 and umur >= 18? I predict True.")
print(harga > 10000 and umur >= 18)

print("\nIs harga > 10000 and umur < 18? I predict False.")
print(harga > 10000 and umur < 18)

# Kata kunci or
print("\nIs harga < 10000 or umur >= 18? I predict True.")
print(harga < 10000 or umur >= 18)

print("\nIs harga < 10000 or umur < 18? I predict False.")
print(harga < 10000 or umur < 18)

# Item ada di dalam list
print("\nIs 'jeruk' in daftar_buah? I predict False.")
print('jeruk' in daftar_buah)

# Item tidak ada di dalam list
print("\nIs 'jeruk' not in daftar_buah? I predict True.")
print('jeruk' not in daftar_buah)

print("\nIs 'apel' not in daftar_buah? I predict False.")
print('apel' not in daftar_buah)