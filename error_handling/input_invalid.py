def alter_pruefen():
    try:
        alter = int(input("Wie alt bist du? "))
        if alter < 0:
            raise ValueError("Alter kann nicht negativ sein.")
        print("Du bist", alter, "Jahre alt.")
    except ValueError as fehler:
        print("Ungültige Eingabe:", fehler)

alter_pruefen()