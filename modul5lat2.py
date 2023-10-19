total_harga = 0

while True:
    umur = input("Masukkan umur (atau q untuk lanjut pembayaran): ")
    if umur == 'q':
        break
    umur = int(umur)
    if umur <= 2:
        harga = 0
    elif umur <= 12:
        harga = 14
    elif umur >= 65:
        harga = 18
    else:
        harga = 23
    total_harga += harga
    print("Harga untuk umur", umur, " tahun = ", harga, "dollars.")

print("Harga totalnya = ", total_harga, "dollars.")

while True:
    dibayar = input("Total uang anda = ")
    if dibayar == 'q':
        break
    dibayar = float(dibayar)
    if dibayar >= total_harga:
        kembalian = dibayar - total_harga
        print("Kembalian = ", kembalian, "dollars.")
        break
    else:
        print("Maaf, uang anda tidak cukup. Silakan isi ulang dompet anda!")
print("Terima kasih atas pembayarannya ^_^")