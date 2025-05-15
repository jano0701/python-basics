# Funktion, die Risiken mit Score > Schwelle filtert

risks = [
    {"name": "Cyber-Angriff", "score": 9},
    {"name": "Lieferkettenausfall", "score": 6},
    {"name": "Reputationsverlust", "score": 8}
]

def filter_high_risks(risiko_liste, schwelle):
    gefiltert = []
    for risiko in risiko_liste:
        if risiko["score"] > schwelle:
            gefiltert.append(risiko)
    return gefiltert

kritische_risiken = filter_high_risks(risks, 7)
print("Kritische Risiken:")
for r in kritische_risiken:
    print(f"- {r['name']} (Score: {r['score']})")