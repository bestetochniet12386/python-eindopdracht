# Producten en prijzen
product1 = "Apple iPhone 16"
prijs1 = 899.00

product2 = "Logitech MX Master 3S"
prijs2 = 109.00

product3 = "Logitech G Pro X TKL toetsenbord"
prijs3 = 149.99

# Aantal verkochte producten invullen
aantal1 = int(input("Hoeveel iPhones zijn verkocht? "))
aantal2 = int(input("Hoeveel muizen zijn verkocht? "))
aantal3 = int(input("Hoeveel toetsenborden zijn verkocht? "))

# Omzet per product berekenen
omzet1 = prijs1 * aantal1
omzet2 = prijs2 * aantal2
omzet3 = prijs3 * aantal3

# Totale omzet berekenen
totale_omzet = omzet1 + omzet2 + omzet3

# Product printen
print("\n---Productoverzicht---")
print("Product:", product1, "| Prijs: €", prijs1, "| Aantal:", aantal1)
print("Product:", product2, "| Prijs: €", prijs2, "| Aantal:", aantal2)
print("Product:", product3, "| Prijs: €", prijs3, "| Aantal:", aantal3)

# Totale omzet printen
print("--------------------------")
print("Totale omzet: €", round(totale_omzet, 2))