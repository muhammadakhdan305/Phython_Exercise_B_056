glossary = {
    'variable': 'nama yang dipakai untuk menyimpan sebuah nilai.','string': 'rangkaian karakter yang ditulis di dalam tanda kutip.','list': 'kumpulan item berurutan yang bisa diubah isinya.','loop': 'blok kode yang dijalankan berulang kali.','dictionary': 'kumpulan pasangan key dan value.',}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")