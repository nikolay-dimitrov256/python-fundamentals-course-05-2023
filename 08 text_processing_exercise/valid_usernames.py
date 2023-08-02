def valid_length(name: str) -> bool:
    if len(name) in range(3, 17):
        return True
    return False


def valid_characters(name: str) -> bool:
    for ch in name:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            return False
    return True


def no_redundant_symbols(name: str) -> bool:
    if ' ' in name:
        return False
    return True


def valid_username(name: str) -> bool:
    if valid_length(name) and valid_characters(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if valid_username(username):
        print(username)
