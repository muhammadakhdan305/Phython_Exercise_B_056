mobil = ["Toyota", "Honda", "Suzuki", "Mazda"]
print(f"List awal: {mobil}")
print("===========================================================")
# Mengakses elemen berdasarkan indeks
print(f"Elemen pertama: {mobil[0]}")
print(f"Elemen terakhir: {mobil[-1]}")
print("===========================================================")
# Mengubah elemen
mobil[1] = "BMW"
print(f"Setelah diubah: {mobil}")
print("===========================================================")
# append(): menambah di akhir
mobil.append("Honda")
print(f"Setelah append: {mobil}")
print("===========================================================")
# insert(): menyisipkan di posisi tertentu
mobil.insert(0, "Ferrari")
print(f"Setelah insert: {mobil}")
print("===========================================================")

# len(): jumlah elemen
print(f"Jumlah mobil: {len(mobil)}")
print("===========================================================")

# del: menghapus berdasarkan indeks
del mobil[1]
print(f"Setelah del: {mobil}")
print("===========================================================")
# pop(): menghapus elemen terakhir dan menyimpan nilainya
popped_car = mobil.pop()
print(f"Hasil pop: {popped_car}")
print(f"Setelah pop: {mobil}")
print("===========================================================")

# remove(): menghapus berdasarkan nilai
mobil.remove("Mazda")
print(f"Setelah remove: {mobil}")
print("===========================================================")

# Tambah dua mobil lagi supaya pengurutan lebih jelas
mobil.append("Audi")
mobil.append("Tesla")
print(f"Urutan asli: {mobil}")
print("===========================================================")
# sorted(): urutan sementara, list asli tidak berubah
print(f"sorted() alfabet: {sorted(mobil)}")
print(f"sorted() kebalikan: {sorted(mobil, reverse=True)}")
print(f"List asli masih sama: {mobil}")
print("===========================================================")
# reverse(): membalik urutan list secara permanen
mobil.reverse()
print(f"Setelah reverse(): {mobil}")
print("===========================================================")

# sort(): mengurutkan list secara permanen
mobil.sort()
print(f"Setelah sort(): {mobil}")
mobil.sort(reverse=True)
print(f"Setelah sort(reverse=True): {mobil}")

print(f"Jumlah mobil sekarang: {len(mobil)}")