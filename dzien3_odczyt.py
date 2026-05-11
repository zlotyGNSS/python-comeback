# dzien3_odczyt.py - czytamy punkty z pliku
import math

print("=== GNSS Vector z pliku ===")

# Otwieramy plik
punkty = []
with open("punkty.txt", "r") as f:
    for linia in f:
        # Rozbijamy "P1, 100.000, 200.000, 150.000"
        dane = linia.strip().split(",")
        nazwa = dane[0].strip()
        x = float(dane[1])
        y = float(dane[2])
        z = float(dane[3])
        punkty.append({"nazwa": nazwa, "x": x, "y": y, "z": z})

# Liczymy wektory między punktami
for i in range(len(punkty)-1):
    p1 = punkty[i]
    p2 = punkty[i+1]

    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    dz = p2["z"] - p1["z"]

    d3d = math.sqrt(dx**2 + dy**2 + dz**2)

    print(f"\nWektor {p1['nazwa']} -> {p2['nazwa']}")
    print(f"dx={dx:.3f} dy={dy:.3f} dz={dz:.3f}")
    print(f"Długość 3D: {d3d:.3f} m")
print("\n--- TEST ---")
print(f"Mam {len(punkty)} punkty w plecaku:")
print(punkty)
