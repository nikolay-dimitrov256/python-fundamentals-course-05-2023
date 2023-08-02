from string import ascii_lowercase

strings_list = input().split()

lowercase_letters = {}
uppercase_letters = {}
total_sum = 0

counter = 0
for let in ascii_lowercase:
    counter += 1
    lowercase_letters[let] = counter
    uppercase_letters[let.upper()] = counter

for current_string in strings_list:
    current_string = current_string.strip()
    left_letter = current_string[0]
    right_letter = current_string[-1]
    number = int(current_string[1:-1])

    if left_letter in uppercase_letters:
        number /= uppercase_letters[left_letter]
    elif left_letter in lowercase_letters:
        number *= lowercase_letters[left_letter]

    if right_letter in uppercase_letters.keys():
        number -= uppercase_letters[right_letter]
    elif right_letter in lowercase_letters.keys():
        number += lowercase_letters[right_letter]

    total_sum += number

print(f'{total_sum:.2f}')
