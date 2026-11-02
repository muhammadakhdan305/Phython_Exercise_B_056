prompt = "\nMasukkan usia (ketik 'quit' untuk selesai): "

while True:
    usia_teks = input(prompt)

    if usia_teks == 'quit':
        break

    usia = int(usia_teks)

    if usia < 3:
        print("Tiket gratis.")
    elif usia <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")

print("===============================================================")
prompt = "\nMasukkan usia (ketik 'quit' untuk selesai): "

usia_teks = input(prompt)

while usia_teks != 'quit':
    usia = int(usia_teks)

    if usia < 3:
        print("Tiket gratis.")
    elif usia <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")

    usia_teks = input(prompt)

print("===================================================================")
prompt = "\nMasukkan usia (ketik 'quit' untuk selesai): "

aktif = True

while aktif:
    usia_teks = input(prompt)

    if usia_teks == 'quit':
        aktif = False
    else:
        usia = int(usia_teks)

        if usia < 3:
            print("Tiket gratis.")
        elif usia <= 12:
            print("Harga tiket $10.")
        else:
            print("Harga tiket $15.")

