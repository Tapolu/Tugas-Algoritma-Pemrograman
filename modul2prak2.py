import math

lat1 = float(input("Nilai lattitude 1 titik A = "))
lat2 = float(input("Nilai lattitude 2 titik A = "))
long1 = float(input("Nilai longitude 1 titik B = "))
long2 = float(input("Nilai longitude 2 titik B = "))

L_1 = lat1 * math.pi/180
B_1 = long1 * math.pi/180
L_2 = lat2 * math.pi/180
B_2 = long2 * math.pi/180

lat = L_2 - L_1
long = B_2 - B_1

a = (math.sin(lat/2)**2 + math.cos(L_1) * math.cos(L_2) * math.sin(long/2)**2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = 6371*c

print (L_1)
print (B_1)
print (L_2)
print (B_2)
print (lat)
print (long)
print (a)
print (c)
print ("Hasil jarak antara titik A dan B adalah = ",d, "km") 