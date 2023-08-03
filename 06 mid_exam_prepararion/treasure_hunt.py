def loot_found(initial_loot: list, some_loot: list) -> list:
    for item in some_loot:
        if item not in initial_loot:
            initial_loot.insert(0, item)

    return initial_loot


def drop_loot(initial_loot: list, drop_index: int) -> list:
    if drop_index in range(len(initial_loot)):
        initial_loot.append(initial_loot.pop(drop_index))

    return initial_loot


def steal_loot(initial_loot: list, count_stolen: int) -> list:
    stolen_items = []
    if count_stolen >= len(initial_loot):
        stolen_items, initial_loot = initial_loot, []
    else:
        steal_index = len(initial_loot) - count_stolen
        stolen_items = initial_loot[steal_index:]
        initial_loot = initial_loot[:steal_index]

    print(*stolen_items, sep=", ")
    return initial_loot


treasure_chest = input().split("|")

command = input()

while command != "Yohoho!":
    command = command.split()

    if command[0] == "Loot":
        loot = command[1:]
        treasure_chest = loot_found(treasure_chest, loot)

    elif command[0] == "Drop":
        index = int(command[1])
        treasure_chest = drop_loot(treasure_chest, index)

    elif command[0] == "Steal":
        stolen_count = int(command[1])
        treasure_chest = steal_loot(treasure_chest, stolen_count)

    command = input()

if treasure_chest:
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
