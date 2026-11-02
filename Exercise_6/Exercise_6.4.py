glossary = {'variable': 'nama yang dipakai untuk menyimpan sebuah nilai.',
'string': 'rangkaian karakter yang ditulis di dalam tanda kutip.',
'list': 'kumpulan item berurutan yang bisa diubah isinya.',
'loop': 'blok kode yang dijalankan berulang kali.',
'dictionary': 'kumpulan pasangan key dan value.',
'tuple': 'kumpulan item berurutan yang isinya tidak bisa diubah.',
'index': 'nomor posisi sebuah item di dalam list, dimulai dari 0.'
,'slice': 'sebagian dari list yang diambil dengan format [awal:akhir].'
,'comment': 'catatan di dalam kode yang diawali # dan diabaikan Python.'
,'boolean': 'nilai yang hanya bisa True atau False.'}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")