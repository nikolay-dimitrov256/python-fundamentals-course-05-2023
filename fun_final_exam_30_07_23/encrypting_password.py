import re


def encrypt_password(data: dict) -> str:
    encrypted_password = data['one'] + data['two'] + data['three'] + data['four']

    return encrypted_password


def validate_password(password: str):
    pattern = r'(.+)>(?P<one>\d{3})\|(?P<two>[a-z]{3})\|(?P<three>[A-Z]{3})\|(?P<four>[^<>]{3})<\1'
    match = re.fullmatch(pattern, password)

    if match:
        data = match.groupdict()
        return data


def main_function(n: int):
    for _ in range(n):
        password = input()
        data = validate_password(password)

        if data is None:
            print('Try another password!')
        else:
            print(f'Password: {encrypt_password(data)}')


number = int(input())

main_function(number)
