current_users = ['Admin', 'Budi', 'Agus', 'Somad', 'Suki']
new_users = ['BUDI', 'dewi', 'agus', 'Rina', 'Joko']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. "
              "Silakan masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")