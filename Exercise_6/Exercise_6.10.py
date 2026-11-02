favorite_numbers = {
    'budi': [7, 21],
    'siti': [12, 3, 45],
    'agus': [3],
    'rina': [21, 8],
    'andi': [9, 14, 100],
}

for orang, daftar_angka in favorite_numbers.items():
    print(f"\nAngka favorit {orang.title()}:")
    for angka in daftar_angka:
        print(f"- {angka}")