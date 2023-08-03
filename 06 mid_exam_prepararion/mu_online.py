def potion(current_health: int, healing: int) -> int:
    healed_for = 0
    if current_health + healing > 100:
        healed_for = 100 - current_health
    else:
        healed_for = healing
    current_health += healed_for
    print(f"You healed for {healed_for} hp.")
    print(f"Current health: {current_health} hp.")

    return current_health


def chest(current_bitcoins: int, found_coins: int) -> int:
    current_bitcoins += found_coins
    print(f"You found {found_coins} bitcoins.")

    return current_bitcoins


def monster_fight(current_health: int, current_monster: str, monster_attack: int) -> int:
    current_health -= monster_attack
    if current_health > 0:
        print(f"You slayed {current_monster}.")
    else:
        print(f"You died! Killed by {current_monster}.")

    return current_health


dungeon_rooms = input().split("|")

health = 100
bitcoins = 0

for i in range(len(dungeon_rooms)):
    current_room = dungeon_rooms[i].split()

    if current_room[0] == "potion":
        healed_amount = int(current_room[1])
        health = potion(health, healed_amount)

    elif current_room[0] == "chest":
        found_bitcoins = int(current_room[1])
        bitcoins = chest(bitcoins, found_bitcoins)

    else:
        monster = current_room[0]
        stats = int(current_room[1])
        health = monster_fight(health, monster, stats)
        if health <= 0:
            print(f"Best room: {i + 1}")
            break

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
