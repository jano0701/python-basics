try:
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Ergebnis:", ergebnis)
except ZeroDivisionError:
    print("Fehler: Division durch 0 ist nicht erlaubt.")
except ValueError:
    print("Fehler: Bitte eine gültige Zahl eingeben.")