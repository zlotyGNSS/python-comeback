# dzien4_raport.py - geodezyjny raport z wektorów
import math
from datetime import datetime

def azymut(dx, dy):
    """Liczymy azymut z przyrostów. Zwraca w gradach."""
    az_rad = math.atan2(dy, dx) # atan2 sam ogarnia ćwiartki
    az_grad = math.degrees(az_rad) * 200 / 180 # rad -> grad
    if az_grad < 0:
        az_grad += 400
    return az_grad

# Wczytujemy punkty
punkty = []
with open("punkty.txt", "r") as f:
    for linia in f:
        if linia.strip() == "":
            continue
        dane = linia.strip().split(",")
        nazwa = dane[0].strip()
        x = float(dane[1])
        y = float(dane[2])
        z = float(dane[3])
        punkty.append({"nazwa": nazwa, "x": x, "y": y, "z": z})

# Otwieramy plik do ZAPISU
with open("raport.txt", "w") as raport:
    raport.write("RAPORT Z OBLICZENIA WEKTORÓW GNSS\n")
    raport.write("====================================\n\n")
    raport.write(f"Data: {datetime.now():%Y-%m-%d}\n\n")
    # Liczymy wektory
    for i in range(len(punkty)-1):
        p1 = punkty[i]
        p2 = punkty[i+1]

        dx = p2["x"] - p1["x"]
        dy = p2["y"] - p1["y"]
        dz = p2["z"] - p1["z"]

        d2d = math.sqrt(dx**2 + dy**2)
        d3d = math.sqrt(dx**2 + dy**2 + dz**2)
        az = azymut(dx, dy)

        # Piszemy do pliku
        raport.write(f"Wektor: {p1['nazwa']} -> {p2['nazwa']}\n")
        raport.write(f"dx = {dx:9.3f} m\n")
        raport.write(f"dy = {dy:9.3f} m\n")
        raport.write(f"dz = {dz:9.3f} m\n")
        raport.write(f"Długość 2D = {d2d:7.3f} m\n")
        raport.write(f"Długość 3D = {d3d:7.3f} m\n")
        raport.write(f"Azymut = {az:7.4f} g\n")
        raport.write(f"Przewyższenie = {dz:7.3f} m\n")
        raport.write("-" * 35 + "\n\n")

print("Gotowe! Sprawdź plik raport.txt")
