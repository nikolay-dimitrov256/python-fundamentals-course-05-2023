pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health = int(input())
retire = False

while True:
    command = input()
    if command == "Retire":
        retire = True
        break

    command = command.split()

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif command[0] == "Status":
        sections_for_repair = 0
        for section in pirate_ship:
            if section < max_health * 0.2:
                sections_for_repair += 1
        print(f"{sections_for_repair} sections need repair.")

if retire:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
