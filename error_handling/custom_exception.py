class RisikoZuHochError(Exception):
    pass

def risiko_pruefen(score):
    if score > 8:
        raise RisikoZuHochError("Risikowert zu hoch! Sofortiges Handeln nötig.")
    else:
        print("Risikowert akzeptabel:", score)

try:
    risiko_pruefen(9)
except RisikoZuHochError as e:
    print("Achtung:", e)
