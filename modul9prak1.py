def writeFile():
    nama= input ("Masukkan nama anda = ")
    umur= input ("Masukkan umur anda = ")
    alamat= input ("Masukkan alamat anda = ")
    email= input ("Masukkan email anda = ")
    dosen= input ("Masukkan nama dosen wali anda = ")


    fileWrite = open("Biodata.txt", "w")
    fileWrite.write("Nama = "+ nama + "\nUmur = "+umur + "\nalamat = " + alamat + "\nemail = " + email + "\ndosen = " + dosen)
    fileWrite.close()

def readFile():
    fileRead = open ("Biodata.txt", "r")
    text = fileRead.read()
    print("inilah biodata anda")
    print(text)
    fileRead.close()
writeFile()
print("\n")
readFile()
