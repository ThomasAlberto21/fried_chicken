print("GEROBAK FRIED CHICKEN")
print("--------------------------------------------------")
print("Kode     Jenis       harga")
print("D        Dada        Rp.2500")
print("P        Paha        Rp.2000")
print("S        Sayap       Rp.1500")
print("--------------------------------------------------")

# ? inputan admin
banyak_jenis = int(input("Masukkan Banyak Jenis         : "))
kode_potong = []
jenis_potong = []
banyak_beli = []
harga = []
total = []


# ! logika
i = 0
while (i < banyak_jenis):  # ! perulangan banyak jenis
    print("Jenis Ke : ", i + 1)

    # ? Masukkan Kode Potong
    kode_potong.append(input("Masukkan Kode Potong (D / P / S) : "))

    # ? masukkan banyak beli
    banyak_beli.append(int(input("Beli Sebanyak : ")))

    # ! if elif else
    # * jika memilih kode (D / d)
    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("Dada")  # * tentukan Jenis potong
        harga.append("2500")  # * tentukan Harga
        total.append(banyak_beli[i] * int("2500"))  # ! totalkan

    # * jika memilih kode (P / p)
    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("Paha")  # * tentukan Jenis potong
        harga.append("2000")  # * tentukan Harga
        total.append(banyak_beli[i] * int("2000"))  # ! totalkan

    # * jika memilih kode (S / s)
    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Sayap")  # * tentukan Jenis potong
        harga.append("1500")  # * tentukan Harga
        total.append(banyak_beli[i] * int("1500"))  # ! totalkan

    # * Lainnya
    else:
        jenis_potong.append("Jenis Tidak Ada")
        harga.append("0")
        total.append(banyak_jenis[i] * int("0"))
    i += 1

# * print hasilnya
print("----------------------HASIL---------------------")
print("              GEROBAK FRIED CHICKEN             ")
print("------------------------------------------------")
print("No   Jenis   Harga   Banyak  Jumlah")
print("     Potong  Satuan  Beli    Harga")
print("------------------------------------------------")


# * lakukan perulangan cetak hasillnya
hasil = 0
while hasil < banyak_jenis:
    print("%i.    %s    %s     %i      %i" % (
        hasil+1, jenis_potong[hasil], harga[hasil], banyak_beli[hasil], total[hasil]))
    hasil += 1


print("------------------------------------------------")
# ! setiap pembeli dikenakan pajak 10%
jumlah_bayar = int(input("Jumlah Bayar Rp. "))
pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("Pajak 10 % Rp. ", pajak)
print("Total Bayar Rp. ", total_bayar)
