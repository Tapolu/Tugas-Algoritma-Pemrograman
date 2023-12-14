import pandas as pd

# Membaca file CSV
df = pd.read_csv('Negara.csv')

# Menghitung mean dan standard deviation
mean = df.groupby("Benua").mean()[["Luas", "Populasi"]]
std = df.groupby("Benua").std()[["Luas", "Populasi"]]

# Menyimpan data ke file CSV
mean.to_csv("mean.csv")
std.to_csv("std.csv")

# Menampilkan hasil output
print("Berikut Data Mean:")
print(mean)
print("Berikut Data Standard Deviation:")
print(std)
print("File Berhasil Dibuat")