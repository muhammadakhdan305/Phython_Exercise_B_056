person_1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 25,
    'city': 'Bandung',
}

person_2 = {
    'first_name': 'Tristan',
    'last_name': 'Naya',
    'age': 19,
    'city': 'Depok',
}

person_3 = {
    'first_name': 'Agus',
    'last_name': 'Wijaya',
    'age': 22,
    'city': 'Medan',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {full_name}")
    print(f"Usia: {person['age']}")
    print(f"Kota: {person['city']}\n")