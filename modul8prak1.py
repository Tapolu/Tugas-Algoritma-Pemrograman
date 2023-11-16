def penjumlahan_rekursif(jumlah):
    if jumlah == 0:
        return 0
    elif jumlah < 0:
        print("Angka harus positif")
        return 0
    else:
        angka = float(input("Masukkan angka ke-{}: ".format(jumlah)))
        return angka + penjumlahan_rekursif(jumlah - 1)

jumlah_angka = int(input("Masukkan Jumlah: "))

if jumlah_angka == 0:
    print("0 invalid.")
elif jumlah_angka <0:
    print("Angka harus positif!")
else:
    hasil = penjumlahan_rekursif(jumlah_angka)
    print("Hasil dari penjumlahan {} adalah: {}".format(jumlah_angka, hasil))
