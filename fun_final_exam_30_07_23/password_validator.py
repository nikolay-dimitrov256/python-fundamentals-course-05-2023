from string import ascii_lowercase, ascii_uppercase


def make_upper(password: str, command: str) -> str:
    command = command.split()
    index = int(command[2])

    if index in range(len(password)):
        ch = password[index]
        password = password.replace(ch, ch.upper(), 1)

    print(password)

    return password


def make_lower(password: str, command: str) -> str:
    command = command.split()
    index = int(command[2])

    if index in range(len(password)):
        ch = password[index]
        password = password.replace(ch, ch.lower(), 1)

    print(password)

    return password


def insert_char(password: str, command: str) -> str:
    command = command.split()
    index = int(command[1])
    char = command[2]

    if index in range(len(password)):
        password = password[:index] + char + password[index:]

    print(password)

    return password


def replace_char(password: str, command: str) -> str:
    command = command.split()
    char = command[1]
    value = int(command[2])

    if char in password:
        new_char = chr(ord(char) + value)
        password = password.replace(char, new_char)

    print(password)

    return password


def validation(password: str) -> str:
    if len(password) < 8:
        print("Password must be at least 8 characters long!")

    invalid_chars = False
    uppercase_letter = False
    lowercase_letter = False
    digit_present = False

    for ch in password:
        if not ch.isalnum() and ch != '_':
            invalid_chars = True
        elif ch in ascii_uppercase:
            uppercase_letter = True
        elif ch in ascii_lowercase:
            lowercase_letter = True
        elif ch.isdigit():
            digit_present = True

    if invalid_chars:
        print('Password must consist only of letters, digits and _!')
    if not uppercase_letter:
        print('Password must consist at least one uppercase letter!')
    if not lowercase_letter:
        print('Password must consist at least one lowercase letter!')
    if not digit_present:
        print('Password must consist at least one digit!')

    return password


def modify_data(password: str):
    while True:
        command = input()

        if command == 'Complete':
            break

        if command.startswith('Make Upper'):
            password = make_upper(password, command)

        elif command.startswith('Make Lower'):
            password = make_lower(password, command)

        elif command.startswith('Insert'):
            password = insert_char(password, command)

        elif command.startswith('Replace'):
            password = replace_char(password, command)

        elif command == 'Validation':
            password = validation(password)


text = input()

modify_data(text)
