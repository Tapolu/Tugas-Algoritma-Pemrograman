def cek_tahun_bulan():
    while True:
        print("Ketik 0 untuk berhenti dari program")
        tahun = int(input("Masukkan tahun: "))
        if tahun == 0:
            break
        bulan = int(input("Masukkan bulan (1-12): "))
        if bulan == 0:
            break
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            print("ada 31 hari dalam sebulan")
        elif bulan == 2:
            if tahun % 4 == 0:
                if tahun % 100 != 0 or (tahun % 100 == 0 and tahun % 400 == 0):
                    print("ada 29 hari dalam sebulan")
                else:
                    print("ada 28 hari dalam sebulan")
            else:
                print("ada 28 hari dalam sebulan")
        elif bulan in [4, 6, 9, 11]:
            print("ada 30 hari dalam sebulan")
        else:
            print("Invalid input!")

cek_tahun_bulan()
print("Terima kasih telah mencoba~")
