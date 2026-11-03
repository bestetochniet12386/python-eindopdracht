# Boodschappenlijst met 5 producten
boodschappenlijst = ["brood", "melk", "eieren", "kaas", "appels"]

# Twee nieuwe producten invoeren
product1 = input("Welk eerste product wil je toevoegen? ")
boodschappenlijst.append(product1)

product2 = input("Welke tweede product wil je toevoegen? ")
boodschappenlijst.append(product2)

# 1 product verwijderen
verwijderen = input("Welke product wil je verwijderen? ")
boodschappenlijst.remove(verwijderen)

# Aantal producten printen
print("Aantal producten:", len(boodschappenlijst))

# Volledige boodschappenlijst printen
print ("Boodschappenlijst:", len(boodschappenlijst))

# Controleren of een product in de lijst staat
controle = input("Welke producten wil je controleren? ")

if controle in boodschappenlijst:
    print(controle, "staat in de boodschappenlijst!")
else:
    print(controle, "staat niet in de boodschappenlijst.")