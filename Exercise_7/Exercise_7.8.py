sandwich_orders = ['tuna', 'ayam', 'telur', 'keju']
finished_sandwiches = []

while sandwich_orders:
    pesanan = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {pesanan} milikmu.")
    finished_sandwiches.append(pesanan)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")