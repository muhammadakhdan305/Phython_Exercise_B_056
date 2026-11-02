# Menggunakan program Exercise 4.9 untuk membuat hasil penggunaan slice pada list Cubes
Cubes = [value ** 3 for value in range(1, 11)]
print("3 angka pertama dari list Cubes:")
for cube in Cubes[:3]:
    print(cube)
print()
print("3 angka tengah dari list Cubes:")
for cube in Cubes[3:6]:
    print(cube)
print()
print("3 angka terakhir dari list Cubes:")
for cube in Cubes[-3:]:
    print(cube)
    