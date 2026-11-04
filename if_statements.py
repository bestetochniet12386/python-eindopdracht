# Cijfers
nederlands = float(input("Voer je cijfer Nederlands in: "))
rekenen = float(input("Voer je cijfer voor Rekenen in: "))
engels = float(input("Voer je cijfer voor Engels in: ")) 

# Controleren of de cijfers geldig zijn
if nederlands > 10 or rekenen > 10 or engels > 10:
    print("Fout! Een cijfer mag niet hoger zijn dan 10.")
elif nederlands < 0 or rekenen < 0 or engels < 0:
    print("Fout! Een cijfer mag niet lager zijn dan 0.")
else:
    # Gemiddelde berekenen
    gemiddelde = (nederlands + rekenen + engels) / 3
    print("Gemiddelde:", gemiddelde)

# Controleren of de student geslaagd is of niet
if nederlands < 4 or rekenen < 4 or engels < 4:
    print("Gezakt!")
elif gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")