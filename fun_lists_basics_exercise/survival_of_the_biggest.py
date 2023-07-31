numbers_as_string = input().split(" ")
count_of_numbers_to_remove = int(input())

numbers_as_digits = []

for num in numbers_as_string:
    numbers_as_digits.append(int(num))

sorted_numbers = sorted(numbers_as_digits)
numbers_to_remove = sorted_numbers[:count_of_numbers_to_remove]

for item in numbers_to_remove:
    numbers_as_digits.remove(item)

final_sequence = []

for element in numbers_as_digits:
    final_sequence.append(str(element))

final_sequence = ", ".join(final_sequence)

print(final_sequence)
