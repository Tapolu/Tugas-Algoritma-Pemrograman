print ("Program menghitung dan konversi luas ruangan")
def inch_ke_meter(inch):
  return inch * 0.0254

def luas_ruangan(panjang, lebar, satuan):
  if satuan == "m":
    return panjang * lebar
  else:
    return inch_ke_meter(panjang) * inch_ke_meter(lebar)

panjang = float(input("Input panjang ruangan (m): "))
lebar = float(input("Input lebar ruangan (m): "))
satuan = input("pilih satuan yang digunakan (m/inch): ")

luas = luas_ruangan(panjang, lebar, satuan)
print("Luas ruangannya adalah", luas, "meter persegi.")

