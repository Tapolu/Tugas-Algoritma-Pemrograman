def writeFile(data, file):
    fileWrite = open(file, "w")
    fileWrite.write(data)
    fileWrite.close()

def readFile(file):
    fileRead = open(file, "r")
    text = fileRead.read()
    print(text)
    fileRead.close()

def addText(data, file):
    file = open(file, "a")
    file.write(data)
    file.close()

while True:
    print("=== Program File Handling ===")
    print("1. Membuat File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")
    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")
    
    if pilihan == "1":
        File = input("Masukkan Nama File Kamu: ")
        NIM = input("Masukkan Nama Kamu: ")
        Nama = input("Masukkan NIM Kamu: ")
        Tahun = input("Masukkan Tahun Angkatanmu: ")
        data = "\nFile: " + File + "\nNama: " + Nama + "\nNIM: " + NIM + "\nTahun Angkatan: " + Tahun 
        writeFile(data, "data.txt")
    elif pilihan == "2":
        readFile("data.txt")
    elif pilihan == "3":
        sahabat = input("Masukkan nama sahabatmu:")
        data = "\nSahabatmu: " + sahabat
        addText(data, "data.txt")
    elif pilihan == "4":
        print("Terima Kasih")
        break
    else:
        print("\nPilihan tidak valid. Silahkan masukkan angka 1, 2, 3 atau 4.")
