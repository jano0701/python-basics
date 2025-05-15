class Auto:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def fahren(self):
        print(f"{self.marke} aus dem Jahr {self.baujahr} fährt los.")

mein_auto = Auto("Toyota", 2020)
mein_auto.fahren()