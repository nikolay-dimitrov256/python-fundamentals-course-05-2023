def exchange(some_index: int, some_list: list) -> list:
    if some_index not in range(len(some_list)):
        print("Invalid index")
        return some_list
    right_part = some_list[some_index + 1:]
    for _ in range(len(right_part)):
        some_list.insert(0, some_list.pop(-1))
    return some_list


def max_even_odd(even_odd: str, some_list: list):
    biggest_even = -2
    index_biggest_even = None
    biggest_odd = -1
    index_biggest_odd = None
    if even_odd == "even":
        for index, digit in enumerate(some_list):
            if digit % 2 == 0 and digit >= biggest_even:
                biggest_even = digit
                index_biggest_even = index
        if index_biggest_even is None:
            return "No matches"
        return index_biggest_even
    elif even_odd == "odd":
        for index, digit in enumerate(some_list):
            if digit % 2 != 0 and digit >= biggest_odd:
                biggest_odd = digit
                index_biggest_odd = index
        if index_biggest_odd is None:
            return "No matches"
        return index_biggest_odd


def min_even_odd(even_odd: str, some_list: list):
    smallest_even = float("inf")
    index_smallest_even = None
    smallest_odd = float("inf")
    index_smallest_odd = None
    if even_odd == "even":
        for index, digit in enumerate(some_list):
            if digit % 2 == 0 and digit <= smallest_even:
                smallest_even = digit
                index_smallest_even = index
        if index_smallest_even is None:
            return "No matches"
        return index_smallest_even
    elif even_odd == "odd":
        for index, digit in enumerate(some_list):
            if digit % 2 != 0 and digit <= smallest_odd:
                smallest_odd = digit
                index_smallest_odd = index
        if index_smallest_odd is None:
            return "No matches"
        return index_smallest_odd


def first_count_even_odd(count: int, even_odd: str, some_list: list):
    if count > len(some_list):
        return "Invalid count"
    even_list = []
    odd_list = []
    if even_odd == "even":
        for i in range(len(some_list)):
            if some_list[i] % 2 == 0:
                even_list.append(some_list[i])
            if len(even_list) >= count:
                break
        return even_list
    elif even_odd == "odd":
        for i in range(len(some_list)):
            if some_list[i] % 2 != 0:
                odd_list.append(some_list[i])
            if len(odd_list) >= count:
                break
        return odd_list


def last_count_even_odd(count: int, even_odd: str, some_list: list):
    if count > len(some_list):
        return "Invalid count"
    even_list = []
    odd_list = []
    if even_odd == "even":
        for even_i in range(len(some_list) - 1, - 1, - 1):
            if some_list[even_i] % 2 == 0:
                even_list.insert(0, some_list[even_i])
            if len(even_list) >= count:
                break
        return even_list
    elif even_odd == "odd":
        for odd_i in range(len(some_list) - 1, - 1, - 1):
            if some_list[odd_i] % 2 != 0:
                odd_list.insert(0, some_list[odd_i])
            if len(odd_list) >= count:
                break
        return odd_list


list_numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    command = command.split()

    if command[0] == "exchange":
        exchange(int(command[1]), list_numbers)
    elif command[0] == "max":
        print(max_even_odd(command[1], list_numbers))
    elif command[0] == "min":
        print(min_even_odd(command[1], list_numbers))
    elif command[0] == "first":
        print(first_count_even_odd(int(command[1]), command[2], list_numbers))
    elif command[0] == "last":
        print(last_count_even_odd(int(command[1]), command[2], list_numbers))

print(list_numbers)
