# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:32:25 2023

@author: Adkur
"""

print ("Program menghitung dan konversi luas ruangan")

#Fungsi convert satuan dari inci ke meter
def inch_ke_meter(inci):
  return inci * 0.0254

#Fungsi menghitung luas ruangan
def luas_ruangan(panjang, lebar, satuan):
  if satuan == "meter":
    return panjang * lebar
  else:
    return inch_ke_meter(panjang) * inch_ke_meter(lebar)

# Input data
panjang = float(input("Masukkan panjang ruangan (meter): "))
lebar = float(input("Masukkan lebar ruangan (meter): "))
satuan = input("Satuan yang digunakan (meter/inch): ")

# Menghitung luas
luas = luas_ruangan(panjang, lebar, satuan)

# Output
print("Luas ruangannya adalah", luas, "meter persegi.")

