responses = {}

pertanyaan = ("Kalau kamu bisa mengunjungi satu tempat di dunia, "
              "ke mana kamu akan pergi? ")
tanya_lanjut = "Apakah ada orang lain yang ingin ikut polling? (ya/tidak) "

polling_aktif = True

while polling_aktif:
    orang = input("\nSiapa namamu? ")
    tujuan = input(pertanyaan)
    responses[orang] = tujuan

    lanjut = input(tanya_lanjut)
    if lanjut == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling ---")
for orang, tujuan in responses.items():
    print(f"{orang.title()} ingin mengunjungi {tujuan.title()}.")