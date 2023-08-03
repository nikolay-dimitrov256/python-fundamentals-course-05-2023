def swap_elements(some_list: list, index_one: int, index_two: int) -> list:
    some_list[index_one], some_list[index_two] = some_list[index_two], some_list[index_one]

    return some_list


def multiply_elements(some_list: list, index_one: int, index_two: int) -> list:
    some_list[index_one] *= some_list[index_two]

    return some_list


def decrease_elements(some_list: list) -> list:
    for i in range(len(some_list)):
        some_list[i] -= 1

    return some_list


list_numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break

    command = command.split()

    if command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        list_numbers = swap_elements(list_numbers, first_index, second_index)

    elif command[0] == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        list_numbers = multiply_elements(list_numbers, first_index, second_index)

    elif command[0] == "decrease":
        list_numbers = decrease_elements(list_numbers)

list_numbers = [str(num) for num in list_numbers]

print(", ".join(list_numbers))
