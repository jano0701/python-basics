class Fahrzeug:
    def __init__(self, marke):
        self.marke = marke

    def beschreiben(self):
        print(f"Dies ist ein Fahrzeug der Marke {self.marke}.")

class Lastwagen(Fahrzeug):
    def __init__(self, marke, ladungskapazitaet):
        super().__init__(marke)
        self.ladungskapazitaet = ladungskapazitaet

    def beschreiben(self):
        print(f"{self.marke}-Lastwagen mit {self.ladungskapazitaet} Tonnen Kapazität.")

mein_lastwagen = Lastwagen("Mercedes", 15)
mein_lastwagen.beschreiben()