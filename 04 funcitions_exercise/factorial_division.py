def factorial_division(a: int, b: int) -> str:
    sum_numbers_a = 1
    sum_numbers_b = 1
    for num_a in range(1, a + 1):
        sum_numbers_a *= num_a
    for num_b in range(1, b + 1):
        sum_numbers_b *= num_b
    result = sum_numbers_a / sum_numbers_b
    return f"{result:.2f}"


first_num = int(input())
second_num = int(input())

print(factorial_division(first_num, second_num))
