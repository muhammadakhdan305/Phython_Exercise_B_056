# List Nama Pizza
Pizza = ["Pepperoni", "Margherita", "Cheese"]

# Copy List Pizza
Friend_Pizza = Pizza[:]

# Menambahkan item baru ke list Pizza
Pizza.append("Hawaiian")

# Menambahkan item baru ke list Friend_Pizza
Friend_Pizza.append("Veggie")

# Mencetak list Pizza
print("Pizza Kesukaanku adalah :")
for pizza in Pizza:
    print(pizza)

print()

# Mencetak list Friend_Pizza
print("Pizza Kesukaan Temanku adalah :")
for pizza in Friend_Pizza:
    print(pizza)