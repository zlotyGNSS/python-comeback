# dzien2_wektor.py - Twój pierwszy kalkulator geodezyjny
print("=== GNSS Vector Calculator ===")
print("by zlotyGNSS\n")

dx = float(input("Podaj dx [m]: "))
dy = float(input("Podaj dy [m]: "))
dz = float(input("Podaj dz [m]: "))

# Długość przestrzenna 3D - to liczymy w GNSS
d3d = (dx**2 + dy**2 + dz**2)**0.5

# Długość pozioma 2D - do mapy
d2d = (dx**2 + dy**2)**0.5

# Azymut w gradach, bo geodezja
import math
if dx == 0 and dy == 0:
    azymut = 0
else:
    azymut_rad = math.atan2(dy, dx)
    azymut = math.degrees(azymut_rad) * 10/9 # rad -> grady
    if azymut < 0: azymut += 400

print(f"\n--- WYNIKI ---")
print(f"Długość 3D: {d3d:.3f} m")
print(f"Długość 2D: {d2d:.3f} m")
print(f"Przewyższenie: {dz:.3f} m")
print(f"Azymut: {azymut:.4f}g")