# Membuat list hasil pangkat 3 dari 1 sampai 10 menggunakan list comprehension
Cubes = [value ** 3 for value in range(1, 11)]
for cube in Cubes:
    print(cube)