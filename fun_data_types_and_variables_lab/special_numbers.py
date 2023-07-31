n = int(input())

for num in range(1, n + 1):
    num = str(num)
    sum_nums = 0
    special = False

    for i in num[::]:
        sum_nums += int(i)

    if sum_nums == 5 or sum_nums == 7 or sum_nums == 11:
        special = True

    print(f'{num} -> {special}')
