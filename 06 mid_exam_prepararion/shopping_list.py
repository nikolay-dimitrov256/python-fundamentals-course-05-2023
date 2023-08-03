def urgent(groceries_list: list, item: str) -> list:
    if item not in groceries_list:
        groceries_list.insert(0, item)

    return groceries_list


def unnecessary(groceries_list: list, item: str) -> list:
    if item in groceries_list:
        groceries_list.remove(item)

    return groceries_list


def correct(groceries_list: list, old_item: str, new_item: str) -> list:
    if old_item in groceries_list:
        item_index = groceries_list.index(old_item)
        groceries_list[item_index] = new_item

    return groceries_list


def rearrange(groceries_list: list, item: str) -> list:
    if item in groceries_list:
        groceries_list.remove(item)
        groceries_list.append(item)

    return groceries_list


groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    command = command.split()

    if command[0] == "Urgent":
        needed_item = command[1]
        groceries = urgent(groceries, needed_item)

    elif command[0] == "Unnecessary":
        unnecessary_item = command[1]
        groceries = unnecessary(groceries, unnecessary_item)

    elif command[0] == "Correct":
        removed_item = command[1]
        inserted_item = command[2]
        groceries = correct(groceries, removed_item, inserted_item)

    elif command[0] == "Rearrange":
        moved_item = command[1]
        groceries = rearrange(groceries, moved_item)

print(", ".join(groceries))
