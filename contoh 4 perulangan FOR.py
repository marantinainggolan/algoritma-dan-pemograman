print ("--------------------------------------------")
print (" Program Deret Aritmatika ")
print ("--------------------------------------------")

nilaiAwal= input (" masukkan nilai awal = ")
jeda= input (" masukkan jeda angka = ")
banyak= input (" masukkan banyak deret angka = ")

jumlahDeret = int (banyak )+1
suku = int (nilaiAwal)

for i in range (1,jumlahDeret,1):
    print("suku ke-",i, "=", suku)
    suku = suku+ int (jeda)

