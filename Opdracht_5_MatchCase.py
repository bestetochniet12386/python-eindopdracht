player_class = "Archer"

match player_class:
  case "Warrior":
    chosen_class = "warrior"
    health = 150
    damage = 20
  case "Mage":
    chosen_class = "mage"
    health = 80
    damage = 35
  case "Archer":
    chosen_class = "Archer"
    health = 100
    damage = 25
  case "Rogue":
    chosen_class = "Rogue"
    health = 90
    damage = 30
  case "Bard":
    chosen_class = "Bard"
    health = 60
    damage = 10
  case "Paladin":
    chosen_class = "Paladin"
    health = 145
    damage = 24
print(f"{player_class} class chosen. Health: {health}. Damage: {damage}")