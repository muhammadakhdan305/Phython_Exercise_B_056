cities = {
    'tokyo': {
        'country': 'jepang',
        'language': 'jepang',
        'population': 14000000,
        'fact': 'dulunya kota ini bernama Edo.',
        'landmarks': ['Tokyo Tower', 'Kuil Senso-ji'],
    },
    'jakarta': {
        'country': 'indonesia',
        'language': 'indonesia',
        'population': 10600000,
        'fact': 'dulunya kota ini bernama Batavia.',
        'landmarks': ['Monumen Nasional', 'Kota Tua'],
    },
    'paris': {
        'country': 'prancis',
        'language': 'prancis',
        'population': 2100000,
        'fact': 'Menara Eiffel selesai dibangun pada tahun 1889.',
        'landmarks': ['Menara Eiffel', 'Museum Louvre'],
    },
}

print(" DAFTAR KOTA ".center(44, "="))

for kota, info_kota in cities.items():
    populasi = f"{info_kota['population']:,}".replace(',', '.')

    print(f"\n{kota.title()}")
    print(f"  Negara   : {info_kota['country'].title()}")
    print(f"  Bahasa   : {info_kota['language'].title()}")
    print(f"  Populasi : sekitar {populasi} jiwa")
    print(f"  Fakta    : {info_kota['fact']}")
    print("  Tempat terkenal:")
    for tempat in info_kota['landmarks']:
        print(f"    - {tempat}")