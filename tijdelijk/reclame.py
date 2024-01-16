prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = prijzen ["aardbei"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: Aardbei, 1 Liter - slechts € {aanbieding}"
reclame_tekst3 = reclame_tekst.upper()
print(reclame_tekst3)