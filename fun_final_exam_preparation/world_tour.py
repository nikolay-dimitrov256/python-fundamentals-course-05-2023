def switch_chars(line: str, params: list) -> str:
    old_string, new_string = params

    if old_string in line:
        line = line.replace(old_string, new_string)

    print(line)

    return line


def remove_stop(line: str, params: list) -> str:
    start_index = int(params[0])
    end_index = int(params[1])

    if start_index in range(len(line)) and end_index in range(len(line)):
        line = line[:start_index] + line[end_index+1:]

    print(line)

    return line


def add_stop(line: str, params: list) -> str:
    index = int(params[0])
    string = params[1]

    if index in range(len(line)):
        line = line[:index] + string + line[index:]

    print(line)

    return line


def modify_data(line: str) -> str:
    while True:
        command, *params = input().split(':')
        if command == 'Travel':
            return line

        if command == 'Add Stop':
            line = add_stop(line, params)

        elif command == 'Remove Stop':
            line = remove_stop(line, params)

        elif command == 'Switch':
            line = switch_chars(line, params)


data = input()

data = modify_data(data)

print(f'Ready for world tour! Planned stops: {data}')
