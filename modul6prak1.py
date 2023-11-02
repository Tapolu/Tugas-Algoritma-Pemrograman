def hitung_rata_rata(A, C):
    total = A + C
    rata_rata = total / 2
    return rata_rata

A = float(input("Input nilai A: "))
C = float(input("Input nilai C: "))

rata_rata = hitung_rata_rata(A, C)

print(f"Rata-ratanya: {rata_rata}")
