#List nama buah dengan array 1 dimensi pada python
buah = ['apel', 'jeruk', 'semangka', 'khuldi']
#menampilkan index ke 3 yaitu buah khuldi
print(buah[3])

#List nama berhala dengan array 2 dimensi pada python
berhala = [['Isaf', 'Nailah'], ['Latta', 'Uzza'], ['Manat', 'Uqaisir']]
# Mengakses elemen-elemen array
print(berhala[0][0])  # Mencetak index ke 1
print(berhala[0][1])  # Mencetak index ke 2
print(berhala[1][1])  # Mencetak index ke 4

# Menggunakan loop untuk mencetak semua elemen array
for baris in berhala:
    for elemen in baris:
        print(elemen)
