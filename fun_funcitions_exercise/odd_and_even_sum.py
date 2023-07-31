is_even = lambda x: x % 2 == 0


def odd_even_sum(some_number: str):
    even_sum = 0
    odd_sum = 0
    for i in range(len(some_number)):
        if is_even(int(some_number[i])):
            even_sum += int(some_number[i])
        else:
            odd_sum += int(some_number[i])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sum(number))
