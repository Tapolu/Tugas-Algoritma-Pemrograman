def angka_ordinal(n):

  if n == 1:
    return "1st"
  elif n == 2:
    return "2nd"
  elif n == 3:
    return "3rd"
  elif n % 10 == 1:
    return f"{n}{'st'}"
  elif n % 10 == 2:
    return f"{n}{'nd'}"
  elif n % 10 == 3:
    return f"{n}{'rd'}"
  else:
    return f"{n}{'th'}"


def main():

  n = int(input("Masukkan angka: "))

  while n != 0:
    ordinal = angka_ordinal(n)
    print(ordinal)
    n = int(input("Masukkan angka: "))

main()
print("Program Berhenti!")
