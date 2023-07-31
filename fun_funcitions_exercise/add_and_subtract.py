sum_numbers = lambda a, b: a + b


def subtract(some_sum, c):
    return some_sum - c


def add_and_subtract(first, second, third):
    sum_first_second = sum_numbers(first, second)
    result = subtract(sum_first_second, third)
    return result


first_num, second_num, third_num = int(input()), int(input()), int(input())

print(add_and_subtract(first_num, second_num, third_num))
