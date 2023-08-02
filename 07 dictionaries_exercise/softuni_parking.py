def register(some_dict: dict, user: str, number: str) -> dict:
    if user in some_dict:
        print(f'ERROR: already registered with plate number {number}')
    else:
        some_dict[user] = number
        print(f'{user} registered {number} successfully')

    return some_dict


def unregister(some_dict: dict, user: str) -> dict:
    if user in some_dict:
        del some_dict[user]
        print(f'{user} unregistered successfully')
    else:
        print(f'ERROR: user {user} not found')

    return some_dict


users_dict = {}

n_lines = int(input())

for _ in range(n_lines):
    line = input().split()

    command, name = line[0], line[1]

    if command == 'register':
        plate_number = line[2]
        users_dict = register(users_dict, name, plate_number)

    elif command == 'unregister':
        users_dict = unregister(users_dict, name)

for name, plate_number in users_dict.items():
    print(f'{name} => {plate_number}')
