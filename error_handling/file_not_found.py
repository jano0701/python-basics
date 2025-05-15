try:
    with open("daten.txt", "r") as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Fehler: Die Datei wurde nicht gefunden.")