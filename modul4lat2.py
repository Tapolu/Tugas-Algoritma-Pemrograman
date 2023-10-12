bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))
jumlah_hari = 0
while True:
  if bulan == 2:
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
      jumlah_hari = 29
    else:
      jumlah_hari = 28
  elif bulan in [4, 6, 9, 11]:
    jumlah_hari = 30
  else:
    jumlah_hari = 31
  print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")
  bulan = int(input("Masukkan bulan (1-12) atau (-1 untuk keluar): "))
  if bulan == -1:
    break
  tahun = int(input("Masukkan tahun: "))
print("Done. Arigatou Gozaimuch >_<")