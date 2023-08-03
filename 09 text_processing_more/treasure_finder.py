def decrypt_string(encrypted_string: str, key: list) -> str:
    index = 0
    new_string = ''
    for i in range(len(encrypted_string)):
        new_char = chr(ord(encrypted_string[i]) - key[index])
        new_string += new_char
        index += 1
        if index >= len(key):
            index = 0

    return new_string


def extract_data(some_message: str):
    treasure = ''
    coordinates = ''
    treasure_flag = False
    coordinates_flag = False

    for ch in message:
        if ch == '&':
            if treasure_flag:
                treasure_flag = False
            else:
                treasure_flag = True
                continue
        elif ch == '<':
            coordinates_flag = True
            continue
        elif ch == '>':
            coordinates_flag = False

        if treasure_flag:
            treasure += ch
        elif coordinates_flag:
            coordinates += ch

    return treasure, coordinates



key_numbers = [int(num) for num in input().split()]

while True:
    line = input()
    if line == 'find':
        break

    message = decrypt_string(line, key_numbers)
    treasure, coordinates = extract_data(message)

    print(f'Found {treasure} at {coordinates}')
