pet_1 = {'animal': 'kucing', 'owner': 'RIzky'}
pet_2 = {'animal': 'anjing', 'owner': 'Suki'}
pet_3 = {'animal': 'kelinci', 'owner': 'Agus'}
pet_4 = {'animal': 'burung', 'owner': 'Renai'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Hewan: {pet['animal'].title()}")
    print(f"Pemilik: {pet['owner']}\n")