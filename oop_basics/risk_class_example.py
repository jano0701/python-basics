class Risiko:
    def __init__(self, name, schweregrad):
        self.name = name
        self.schweregrad = schweregrad

    def ist_kritisch(self):
        return self.schweregrad >= 8

    def __str__(self):
        return f"Risiko: {self.name}, Schweregrad: {self.schweregrad}"

risiko1 = Risiko("Datenleck", 9)
risiko2 = Risiko("Verspätete Rechnung", 4)

print(risiko1, "→ Kritisch?", risiko1.ist_kritisch())
print(risiko2, "→ Kritisch?", risiko2.ist_kritisch())
