def shoot_target(targets_list: list, index: int, power: int) -> list:
    if index in range(len(targets_list)):
        if power >= targets_list[index]:
            targets_list.pop(index)
        else:
            targets_list[index] -= power

    return targets_list


def add_target(targets_list: list, index: int, value: int) -> list:
    if index in range(len(targets_list)):
        targets_list.insert(index, value)
    else:
        print("Invalid placement!")

    return targets_list


def strike_targets(targets_list: list, index: int, radius: int) -> list:
    if index - radius in range(len(targets_list)) and index + radius in range(len(targets_list)):
        start_index = index - radius
        end_index = index + radius

        for removed_index in range(end_index, start_index - 1, - 1):
            targets_list.pop(removed_index)

    else:
        print("Strike missed!")

    return targets_list


targets = [int(num) for num in input().split()]

while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    if command[0] == "Shoot":
        shoot_index = int(command[1])
        shot_power = int(command[2])
        targets = shoot_target(targets, shoot_index, shot_power)

    elif command[0] == "Add":
        target_index = int(command[1])
        target_value = int(command[2])
        targets = add_target(targets, target_index, target_value
                             )
    elif command[0] == "Strike":
        target_index = int(command[1])
        index_radius = int(command[2])
        targets = strike_targets(targets, target_index, index_radius)

print(*targets, sep="|")
