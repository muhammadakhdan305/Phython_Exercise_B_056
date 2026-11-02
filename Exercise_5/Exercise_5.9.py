usernames = ['admin', 'budi', 'agus', 'somad', 'suki']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah login kembali.")
else:
    print("Kita perlu menemukan beberapa pengguna!")

print("\n============================================================")

usernames.clear()
print("\nJika pengguna tidak ada :")
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah login kembali.")
else:
    print("Kita perlu menemukan beberapa pengguna!")