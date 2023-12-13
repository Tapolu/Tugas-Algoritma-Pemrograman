class Mahasiswa:
    mhsCount=0
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.mhsCount +=1

    def tampilkan(self):
        print("Nama:", self.nama)
        print("Nim:", self.nim)
        print("Angkatan:", self.angkatan)

if __name__ == "__main__":
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan Tahun Angkatanmu: ")

    mahasiswa = Mahasiswa(nama, nim, angkatan)
    mahasiswa.tampilkan()

print ("\n")
print("Total Mahasiswa %d" %Mahasiswa.mhsCount)
