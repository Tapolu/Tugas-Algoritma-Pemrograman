print ("Program menghitung dan konversi luas ruangan")

#Fungsi convert satuan dari inch ke meter
def inch_ke_meter(inch):
  return inch * 0.0254

#Fungsi menghitung luas ruangan
def luas_ruangan(panjang, lebar, satuan):
  if satuan == "m":
    return panjang * lebar
  else:
    return inch_ke_meter(panjang) * inch_ke_meter(lebar)

#Input data
panjang = float(input("Input panjang ruangan (m): "))
lebar = float(input("Input lebar ruangan (m): "))
satuan = input("pilih satuan yang digunakan (m/inch): ")

#Menghitung luas
luas = luas_ruangan(panjang, lebar, satuan)

# Output
print("Luas ruangannya adalah", luas, "meter persegi.")

