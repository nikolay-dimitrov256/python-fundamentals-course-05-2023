def contains(key: str, params: list) -> None:
    substring = params[0]
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")


def flip_chars(key: str, params: list) -> str:
    upper_lower = params[0]
    start_index = int(params[1])
    end_index = int(params[2])
    substring = key[start_index:end_index]
    substring = substring.upper() if upper_lower == 'Upper' else substring.lower()
    key = key[:start_index] + substring + key[end_index:]

    print(key)

    return key


def slice_key(key: str, params: list) -> str:
    start_index = int(params[0])
    end_index = int(params[1])
    key = key.replace(key[start_index:end_index], '', 1)

    print(key)

    return key


def modify_data(key: str) -> str:
    while True:
        command, *params = input().split('>>>')

        if command == 'Generate':
            return key

        if command == 'Contains':
            contains(key, params)

        elif command == 'Flip':
            key = flip_chars(key, params)

        elif command == 'Slice':
            key = slice_key(key, params)


activation_key = input()

print(f'Your activation key is: {modify_data(activation_key)}')
