list_guest = ['Ghiry', 'Dhino', 'Dito']

# Undangan Pertama
print(f"Halo {list_guest[0]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[1]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[2]}, Bisakah kamu datang ke acara makan malam bersama kami?")

# Salah satu tamu tidak bisa hadir
print(f"\nSayangnya {list_guest[0]} tidak bisa hadir ke acara makan malam kami.")

# Mengganti tamu dengan tamu baru
list_guest[0] = 'Rizky'

# Undangan Baru
print(f"Halo {list_guest[0]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[1]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[2]}, Bisakah kamu datang ke acara makan malam bersama kami?")

# Menemukan meja yang lebih besar
print("Aku menemukan meja yang lebih besar, jadi ayo undang lebih banyak teman")

# Menambahkan tamu baru
# Menambahkan tamu di awal list
list_guest.insert(0, "Tristan")

# Menambahkan tamu di tengah list
list_guest.insert(2, "Raka")

# Menambahkan tamu di akhir list
list_guest.append("Hylmi")

# Undangan Baru untuk semua tamu
print(f"\nHalo {list_guest[0]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[1]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[2]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[3]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[4]}, Bisakah kamu datang ke acara makan malam bersama kami?")
print(f"Halo {list_guest[5]}, Bisakah kamu datang ke acara makan malam bersama kami?")
