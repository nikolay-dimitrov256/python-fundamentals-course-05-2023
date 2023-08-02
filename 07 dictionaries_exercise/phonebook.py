phonebook = {}

while True:
    line = input()
    if '-' not in line:
        break

    name, phone_number = line.split('-')

    phonebook[name] = phone_number

for _ in range(int(line)):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
