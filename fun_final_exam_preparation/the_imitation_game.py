def move_letters(some_message: str, number: int) -> str:
    some_message = some_message[number:] + some_message[:number]

    return some_message


def insert_letter(some_message: str, some_index: int, letters: str) -> str:
    some_message = some_message[:some_index] + letters + some_message[some_index:]

    return some_message


def change_all(some_message: str, replaced_chars: str, new_chars: str) -> str:
    some_message = some_message.replace(replaced_chars, new_chars)

    return some_message


message = input()

while True:
    command = input()
    if command == 'Decode':
        break

    command = command.split('|')

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        message = move_letters(message, number_of_letters)

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = insert_letter(message, index, value)

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

print(f'The decrypted message is: {message}')
