def insert_space(message: str, index: int) -> str:
    message = message[:index] + ' ' + message[index:]
    print(message)

    return message


def reverse_message(message: str, substring: str) -> str:
    if substring in message:
        message = message.replace(substring, '', 1)
        message += substring[::-1]
        print(message)
    else:
        print('error')

    return message


def change_all(message: str, substring: str, replacement: str) -> str:
    message = message.replace(substring, replacement)
    print(message)

    return message


def modify_message(message: str) -> str:
    while True:
        command, *params = input().split(':|:')
        if command == 'Reveal':
            return message

        if command == 'InsertSpace':
            index = int(params[0])
            message = insert_space(message, index)

        elif command == 'Reverse':
            substring = params[0]
            message = reverse_message(message, substring)

        elif command == 'ChangeAll':
            substring, replacement = params[0], params[1]
            message = change_all(message, substring, replacement)


data = input()

print(f'You have a new text message: {modify_message(data)}')
