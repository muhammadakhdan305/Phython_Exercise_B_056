list_tempat = ["Indonesia", "Australia","Jepang", "Kazakhstan", "Belanda"]

# Original Order
print("Urutan Asli :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Alphabetical Order
print("Urutan Abjad :")
print("list_tempat =", sorted(list_tempat))

print("===========================================================")
# List tidak Berubah
print("Urutan Asli (tidak berubah) :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Reverse Alphabetical Order
print("Urutan Abjad Terbalik :")
print("list_tempat =", sorted(list_tempat, reverse=True))

print("===========================================================")
# List tidak Berubah
print("Urutan Asli (tidak berubah) :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Reverse Original Order
list_tempat.reverse()
print("Setelah Reverse :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Reserve lagi
list_tempat.reverse()
print("Setelah Reverse lagi :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Sort List
list_tempat.sort()
print("Setelah Sort :")
print("list_tempat =", list_tempat)

print("===========================================================")
# Sort List Reverse
list_tempat.sort(reverse=True)
print("Setelah Sort Terbalik :")
print("list_tempat =", list_tempat)

print("===========================================================")