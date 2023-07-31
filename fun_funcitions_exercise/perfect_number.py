def perfection_check(some_number: int) -> str:
    sum_divisors = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            sum_divisors += num
    if sum_divisors == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfection_check(number))
