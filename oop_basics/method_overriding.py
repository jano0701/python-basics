class Tier:
    def sprechen(self):
        print("Das Tier macht ein Geräusch.")

class Hund(Tier):
    def sprechen(self):
        print("Der Hund bellt.")

tier = Tier()
hund = Hund()
tier.sprechen() 
hund.sprechen()  