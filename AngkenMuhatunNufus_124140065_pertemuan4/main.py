
import math_operations

from math_operations import (
    keliling_persegi,
    keliling_persegi_panjang,
    keliling_lingkaran,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin
)


print("=== PROGRAM MODUL MATEMATIKA ===")

sisi = 5

print("\n1. PERSEGI")
print(f"Sisi     : {sisi}")
print(f"Luas     : {math_operations.luas_persegi(sisi):.2f}")
print(f"Keliling : {keliling_persegi(sisi):.2f}")


panjang = 8
lebar = 4

print("\n2. PERSEGI PANJANG")
print(f"Panjang  : {panjang}")
print(f"Lebar    : {lebar}")
print(
    f"Luas     : "
    f"{math_operations.luas_persegi_panjang(panjang, lebar):.2f}"
)
print(
    f"Keliling : "
    f"{keliling_persegi_panjang(panjang, lebar):.2f}"
)


jari_jari = 7

print("\n3. LINGKARAN")
print(f"Jari-jari : {jari_jari}")
print(f"Nilai PI  : {math_operations.PI}")
print(
    f"Luas      : "
    f"{math_operations.luas_lingkaran(jari_jari):.2f}"
)
print(f"Keliling  : {keliling_lingkaran(jari_jari):.2f}")


suhu = 30

print("\n4. KONVERSI TEMPERATUR")
print(f"Celsius    : {suhu}")
print(f"Fahrenheit : {celsius_ke_fahrenheit(suhu):.2f}")
print(f"Kelvin     : {celsius_ke_kelvin(suhu):.2f}")
