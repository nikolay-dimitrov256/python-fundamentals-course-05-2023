n = int(input())

list_numbers = []
filtered_list = []

for _ in range(n):
    current_number = int(input())
    list_numbers.append(current_number)

command = input()

for number in list_numbers:
    if command == 'even':
        if number % 2 == 0:
            filtered_list.append(number)
    elif command == 'odd':
        if number % 2 != 0:
            filtered_list.append(number)
    elif command == 'negative':
        if number < 0:
            filtered_list.append(number)
    elif command == 'positive':
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)
