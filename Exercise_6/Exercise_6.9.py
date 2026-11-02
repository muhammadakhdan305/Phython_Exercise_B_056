favorite_places = {
    'basbas': ['Bali', 'Yogyakarta'],
    'Jend': ['Bandung', 'Lombok', 'Raja Ampat'],
    'Kaka': ['Malang'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")