factor = int(input())
count = int(input())

list_numbers = []

for multiple in range(1, count + 1):
    list_numbers.append(factor * multiple)

print(list_numbers)
