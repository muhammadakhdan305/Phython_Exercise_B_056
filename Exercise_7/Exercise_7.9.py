sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'ayam',
    'telur', 'pastrami', 'keju',
]
finished_sandwiches = []

print("Mohon maaf, pastrami sudah habis.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    pesanan = sandwich_orders.pop(0)
    print(f"Saya sudah membuat sandwich {pesanan} milikmu.")
    finished_sandwiches.append(pesanan)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")