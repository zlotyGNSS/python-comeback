import math
import csv
from datetime import datetime

# To samo co w Dniu 3 - czytamy punkty
punkty = []
with open("punkty.txt", "r") as f:
    for linia in f:
        if linia.strip() == "":
            continue
        dane = linia.strip().split(",")
        punkt = {
            "nazwa": dane[0].strip(),
            "x": float(dane[1]),
            "y": float(dane[2]),
            "z": float(dane[3])
        }
        punkty.append(punkt)

# Otwieramy CSV do zapisu
with open("raport.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # 1. Nagłówek - to będą kolumny w Excelu
    writer.writerow([
        'Data', 'Od', 'Do', 'dx[m]', 'dy[m]', 'dz[m]',
        'D2D[m]', 'D3D[m]', 'Azymut[g]', 'dh[m]'
    ])

    suma_d3d = 0 # tu będziemy zbierać sumę
    data = f"{datetime.now():%Y-%m-%d}"

    # 2. Lecimy po wektorach
    for i in range(len(punkty) - 1):
        p1 = punkty[i]
        p2 = punkty[i+1]

        dx = p2['x'] - p1['x']
        dy = p2['y'] - p1['y']
        dz = p2['z'] - p1['z']
        d2d = math.sqrt(dx**2 + dy**2)
        d3d = math.sqrt(dx**2 + dy**2 + dz**2)
        az_rad = math.atan2(dx, dy)
        az_grad = az_rad * 200 / math.pi
        if az_grad < 0:
            az_grad += 400

        suma_d3d += d3d # dokładamy do sumy

        # 3. Zapisujemy wiersz do CSV
        writer.writerow([
            data,
            p1['nazwa'],
            p2['nazwa'],
            round(dx, 3),
            round(dy, 3),
            round(dz, 3),
            round(d2d, 3),
            round(d3d, 3),
            round(az_grad, 4),
            round(dz, 3)
        ])

    # 4. Pusty wiersz i podsumowanie
    writer.writerow([])
    writer.writerow(['', '', 'SUMA D3D:', '', '', '', '', round(suma_d3d, 3)])

print("Gotowe! Sprawdź raport.csv")
