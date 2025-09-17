import math


num = int(input("Butun son kiriting: "))
print(f"Kvadrati: {num ** 2}")
print(f"Kubi: {num ** 3}")


a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a} ning {b}-darajasi: {a ** b}")


print(f"Pi: {math.pi}")
print(f"E: {math.e}")
radius = float(input("Doira radiusini kiriting: "))
print(f"Doira yuzasi: {math.pi * radius ** 2}")


n = float(input("Ixtiyoriy son kiriting: "))
print(f"Yuqoriga yaxlitlash: {math.ceil(n)}")
print(f"Pastga yaxlitlash: {math.floor(n)}")


side = float(input("Kvadratning tomon uzunligini kiriting: "))
print(f"Yuzasi: {side ** 2}")
print(f"Perimetri: {4 * side}")