list_numbers = [int(num) for num in input().split()]

average_number = sum(list_numbers) / len(list_numbers)
bigger_numbers = [num for num in list_numbers if num > average_number]
bigger_numbers.sort(reverse=True)

if len(bigger_numbers) > 5:
    bigger_numbers = bigger_numbers[:5]

if bigger_numbers:
    print(*bigger_numbers)
else:
    print("No")
