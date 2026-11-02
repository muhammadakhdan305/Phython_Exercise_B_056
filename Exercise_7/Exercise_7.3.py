
angka_input = input("Masukkan sebuah angka: ")
angka_input = int(angka_input)

if angka_input % 10 == 0:
    print(f"Angka {angka_input} adalah kelipatan 10.")
else:
    print(f"Angka {angka_input} bukan kelipatan 10.")