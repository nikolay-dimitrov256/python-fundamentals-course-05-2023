def take_odd(message: str) -> str:
    new_message = ''
    for i in range(len(message)):
        if i % 2 != 0:
            new_message += message[i]
    print(new_message)

    return new_message


def cut_chars(message: str, params: list) -> str:
    index = int(params[0])
    length = int(params[1])
    chars_to_cut = message[index:index+length]
    message = message.replace(chars_to_cut, '', 1)
    print(message)

    return message


def substitute(message: str, params: list) -> str:
    substring, substitution = params
    if substring in message:
        message = message.replace(substring, substitution)
        print(message)
    else:
        print('Nothing to replace!')

    return message


def modify_data(message: str):
    while True:
        command, *params = input().split()

        if command == 'Done':
            return message

        if command == 'TakeOdd':
            message = take_odd(message)

        elif command == 'Cut':
            message = cut_chars(message, params)

        elif command == 'Substitute':
            message = substitute(message, params)


data = input()

print(f'Your password is: {modify_data(data)}')
