def presenteer(mijn_dict, totaal):
    for sleutel, waarde in mijn_dict.items():
        print(f"{sleutel} : {waarde} euro")
    print("=====================")
    print(f"totaal : {totaal} euro")