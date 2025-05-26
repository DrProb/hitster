import os
import shlex

min = 1958
max = 2025

if open("liste.txt").read() == "":
    with open("liste.txt", "w") as datei:
        for i in range(min, max + 1):
            datei.write(f"{i}: \n")
            for j in range(3):
                datei.write("- \n")
    print("Liste erstellt.")


def add(jahreszahl, songname):
    geschrieben = False
    jahreszahl = str(jahreszahl)
    with open("liste.txt", "r") as datei:
        zeilen = datei.readlines()
    zielzeile = None
    for idx, zeile in enumerate(zeilen):
        if zeile.strip().startswith(f"{jahreszahl}:"):
            zielzeile = idx + 1
            break
    if zielzeile is None:
        print(f"Jahr {jahreszahl} nicht gefunden.")
        return
    for i in range(zielzeile, zielzeile + 3):
        if zeilen[i] == "- \n" and not geschrieben:
            zeilen[i] = f"- {songname}\n"
            geschrieben = True
            break
    if not geschrieben:
        zeilen.insert(zielzeile + 3, f"- {songname}\n")

    with open("liste.txt", "w") as datei:
        datei.writelines(zeilen)

while True:
    befehl = input(">>> ")
    if befehl.lower() == "exit":
        break
    try:
        teile = shlex.split(befehl)
        if teile[0] == "add":
            jahr = int(teile[1])
            song = " ".join(teile[2:])
            add(jahr, song)
        else:
            print("Ungültiger Befehl.")
    except Exception as e:
        print("Fehler:", e)
