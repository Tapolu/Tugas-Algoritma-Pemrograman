def perpangkatan(x, pangkat):
    if pangkat == 0:
        return -1
    else:
        return x * perpangkatan(x, pangkat - 1) if pangkat > 0 else 1.0 / perpangkatan(x, -pangkat)

angka = float(input("Masukkan angka = "))
pangkat = int(input("Masukkan pangkat (positif atau negatif) = "))

hasil_perpangkatan = perpangkatan(angka, pangkat)
print(f"{angka} pangkat {pangkat} = {hasil_perpangkatan}")
