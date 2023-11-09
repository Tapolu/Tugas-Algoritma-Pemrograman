def angka_prima(angka):

  if angka == 1:
    return False

  for i in range(2, int(angka**0.5) + 1):
    if angka % i == 0:
      return False

  return True

def main():

  angka = float(input("Masukkan angka = "))

  if angka_prima(angka):
    print(angka, "adalah bilangan prima")
  else:
    print(angka, "bukan bilangan prima")

main()
