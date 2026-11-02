rivers = {'nile': 'mesir','amazon': 'brasil','yangtze': 'tiongkok',}

# Kalimat tentang setiap sungai
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

# Nama setiap sungai
print("\nSungai-sungai dalam dictionary:")
for river in rivers.keys():
    print(river.title())

# Nama setiap negara
print("\nNegara-negara dalam dictionary:")
for country in rivers.values():
    print(country.title())