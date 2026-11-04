monster_health = 150
player_damage = 25
count = 0
while monster_health > 0:
    monster_health -= player_damage
    count += 1
    if monster_health <= 0:
        break
    print(monster_health)
print(f"De speler had {count} aanvallen nodig.")

print("-----------------------------")


enemies = [("Slime",50),("Goblin",130), ("Zombie",190)]

for name,health in enemies: 
    count = 0
    while health > 0:
        health -= player_damage
        count += 1
        if health <= 0:
            break
        print(health)
    print(f"{name} is verslagen in {count} aanvallen.")
