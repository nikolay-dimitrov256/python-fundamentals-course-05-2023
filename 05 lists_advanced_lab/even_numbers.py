list_numbers = list(map(int, input().split(", ")))

even_numbers_indexes = [i for i in range(len(list_numbers)) if list_numbers[i] % 2 == 0]

print(even_numbers_indexes)
