import math
a = float(input("Masukkan nilai A = "))
b = float(input("Masukkan nilai B = "))
c = float(input("Masukkan nilai C = "))

D = float(b*b)-(4*a*c)
print("Determinan = ", D)

if a==0:
    print("Bukan persamaan kuadrat karena nilai A = 0")
elif D == 0:
    print("Ini adalah akar sama")
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = x1
    print("x1 = ",x1)
    print("x2 = ",x2)
    print("Akar persamaannya adalah = ", a, "x² + ", b, "x + ", c, " = 0")
elif D>0:
    print("Ini adalah akar berbeda")
    x1 = (-b + math.sqrt(D))
    x1 = (-b + math.sqrt(D))
    print("x1 = ", x1)
    print("x2 = ", x2)
    print("Akar persamaannya adalah = ", a, "x² + ", b, "x + ", c, " = 0")
else:
    x1 = (-b + math.sqrt(-D)) / (2 * a)
    x2 = (-b - math.sqrt(-D)) / (2 * a)
    print("Ini adalah akar imajiner",x1,x2)
    print("Akar persamaannya adalah = ", a, "x² + ", b, "x + ", c, " = 0")