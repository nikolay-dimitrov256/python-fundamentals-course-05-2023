def collect(items_list: list, item: str) -> list:
    if item not in items_list:
        items_list.append(item)

    return items_list


def drop(items_list: list, item: str) -> list:
    if item in items_list:
        items_list.remove(item)

    return items_list


def combine_items(items_list: list, old_item: str, new_item: str) -> list:
    if old_item in items_list:
        index_old_item = items_list.index(old_item)
        items_list.insert(index_old_item + 1, new_item)

    return items_list


def renew(items_list: list, item: str) -> list:
    if item in items_list:
        item_index = items_list.index(item)
        items_list.append(items_list.pop(item_index))

    return items_list


items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    command = command.split(" - ")

    if command[0] == 'Collect':
        current_item = command[1]
        items = collect(items, current_item)

    elif command[0] == "Drop":
        current_item = command[1]
        items = drop(items, current_item)

    elif command[0] == "Combine Items":
        two_items = command[1].split(":")
        the_old_item = two_items[0]
        the_new_item = two_items[1]
        items = combine_items(items, the_old_item, the_new_item)

    elif command[0] == "Renew":
        current_item = command[1]
        items = renew(items, current_item)

print(", ".join(items))
