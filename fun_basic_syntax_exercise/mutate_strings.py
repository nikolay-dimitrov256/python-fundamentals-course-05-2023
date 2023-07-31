first_string, second_string = input(), input()

mutated_string = first_string

for ch in range(len(first_string)):
    left_string = second_string[:ch + 1]
    right_string = first_string[ch + 1:]
    current_string = left_string + right_string

    if current_string != mutated_string:
        print(current_string)

    mutated_string = current_string
