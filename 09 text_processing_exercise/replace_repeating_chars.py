string = input()

final_string = ''
previous_char = ''

for ch in string:
    if ch != previous_char:
        final_string += ch
        previous_char = ch

print(final_string)
