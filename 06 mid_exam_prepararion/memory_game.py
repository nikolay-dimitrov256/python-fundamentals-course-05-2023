elements = input().split()

counter = 0
success = False

while True:
    counter += 1
    command = input()
    if command == "end":
        break

    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])

    if first_index == second_index or first_index not in range(len(elements)) \
            or second_index not in range(len(elements)):
        middle_index = len(elements) // 2
        new_string = f"-{counter}a"
        elements.insert(middle_index, new_string)
        elements.insert(middle_index, new_string)
        print("Invalid input! Adding additional elements to the board")
        continue

    if elements[first_index] == elements[second_index]:
        matching_element = elements[first_index]
        if first_index > second_index:
            elements.pop(first_index)
            elements.pop(second_index)
        else:
            elements.pop(second_index)
            elements.pop(first_index)
        print(f"Congrats! You have found matching elements - {matching_element}!")

    else:
        print("Try again!")

    if len(elements) == 0:
        success = True
        break

if success:
    print(f"You have won in {counter} turns!")
else:
    print(f"Sorry you lose :(")
    print(" ".join(elements))
