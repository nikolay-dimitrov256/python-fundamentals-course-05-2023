gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break

    command = command.split(" ")
    if command[0] == "OutOfStock":
        for index, value in enumerate(gifts):
            if value == command[1]:
                gifts.pop(index)
                gifts.insert(index, "None")
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts):
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        gifts.pop(-1)
        gifts.append(command[1])

for item in gifts:
    if item != "None":
        print(item, end=" ")
