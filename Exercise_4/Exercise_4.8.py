# Membuat list hasil pangkat 3 dari 1 sampai 10
Cubes = []
for value in range(1, 11):
    cube = value ** 3
    Cubes.append(cube)

for cube in Cubes:
    print(cube)
    