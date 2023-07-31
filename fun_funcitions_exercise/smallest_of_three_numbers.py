def smallest_number(first, second, third):
    list_numbers = [first, second, third]
    smallest = min(list_numbers)
    return smallest


first_num, second_num, third_num = int(input()), int(input()), int(input())

print(smallest_number(first_num, second_num, third_num))
