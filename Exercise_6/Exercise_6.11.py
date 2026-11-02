cities = {
    'tokyo': {
        'country': 'jepang',
        'population': 14000000,
        'fact': 'dulunya kota ini bernama Edo.',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'dulunya kota ini bernama Batavia.',
    },
    'paris': {
        'country': 'prancis',
        'population': 2100000,
        'fact': 'Menara Eiffel selesai dibangun pada tahun 1889.',
    },
}

for kota, info_kota in cities.items():
    print(f"\n{kota.title()}")
    print(f"  Negara: {info_kota['country'].title()}")
    print(f"  Populasi: sekitar {info_kota['population']}")
    print(f"  Fakta: {info_kota['fact']}")