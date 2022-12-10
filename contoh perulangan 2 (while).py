print ("=======================================================")
print (" Program Harga Fotocopy Per Halaman ")
print ("=======================================================")

lembar = 0
rp = 0
harga = input (" Masukkan Harga Per Halaman = ")

print (" Daftar Harga Fotocopy %Rp ",Harga)
print ("")

print ("=======================================================")
print (" Lembar        Harga (Rp")
print ("=======================================================")
while lembar <5:
    lembar = lembar+1
    rp=rp+int(harga)
    print(lembar, '         ',rp)
