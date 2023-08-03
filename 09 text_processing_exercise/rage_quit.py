line = input()

unique_characters = []
rage_message = ''
current_word = ''
factor = ''

for i in range(len(line)):
    if line[i].isdigit():
        factor += line[i]
        if i + 1 >= len(line) or not line[i+1].isdigit():
            factor = int(factor)
            rage_message += current_word * factor
            current_word = ''
            factor = ''

    else:
        current_word += line[i].upper()
        if line[i].upper() not in unique_characters:
            unique_characters.append(line[i].upper())

print(f'Unique symbols used: {len(unique_characters)}')
print(rage_message)
