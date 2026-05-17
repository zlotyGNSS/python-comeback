import math
import csv
import sys
from datetime import datetime

if len(sys.argv)!= 3:
    print("UŻYCIE: python dzien6_pary.py plik_wejsciowy.txt plik_wyjsciowy.csv")
    sys.exit(1)

plik_wejscie = sys.argv[1]
plik_wyjscie = sys.argv[2]

punkty = []
try:
    with open(plik_wejscie, "r") as f:
        for nr_linii, linia in enumerate(f, 1):
            if linia.strip() == "": continue
            try:
                dane = linia.strip().split(",")
                punkt = {"nazwa": dane[0].strip(), "x": float(dane[1]), "y": float(dane[2]), "z": float(dane[3])}
                punkty.append(punkt)
            except (ValueError, IndexError):
                print(f"BŁĄD w linii {nr_linii} - pomijam")
                continue
except FileNotFoundError:
    print(f"BŁĄD: Nie ma pliku {plik_wejscie}")
    sys.exit(1)

# SPRAWDZAMY CZY LICZBA PUNKTÓW JEST PARZYSTA
if len(punkty) % 2!= 0:
    print(f"UWAGA: Masz {len(punkty)} punktów. Ostatni {punkty[-1]['nazwa']} zostanie pominięty bo nie ma pary.")

with open(plik_wyjscie, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Data','Od','Do','dx[m]','dy[m]','dz[m]','D2D[m]','D3D[m]','Azymut[g]','dh[m]'])

    suma_d3d = 0
    data = f"{datetime.now():%Y-%m-%d}"

    # TUTAJ MAGIA: range(0, len-1, 2) = 0,2,4,6...
    for i in range(0, len(punkty) - 1, 2):
        p1, p2 = punkty[i], punkty[i+1]
        dx, dy, dz = p2['x']-p1['x'], p2['y']-p1['y'], p2['z']-p1['z']
        d2d = math.sqrt(dx**2 + dy**2)
        d3d = math.sqrt(dx**2 + dy**2 + dz**2)
        az_rad = math.atan2(dx, dy)
        az_grad = az_rad * 200 / math.pi
        if az_grad < 0: az_grad += 400
        suma_d3d += d3d

        writer.writerow([
            data, p1['nazwa'], p2['nazwa'],
            round(dx,3), round(dy,3), round(dz,3),
            round(d2d,3), round(d3d,3), round(az_grad,4), round(dz,3)
        ])

    writer.writerow([])
    writer.writerow(['', '', 'SUMA D3D:', '', '', '', '', round(suma_d3d, 3)])

print(f"Gotowe! Policzyłem {len(punkty)//2} wektorów parami z {plik_wejscie}")
