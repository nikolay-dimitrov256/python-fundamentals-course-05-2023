def length_validation(some_password: str) -> bool:
    if len(some_password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        return False
    return True


def symbol_validation(some_password: str) -> bool:
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def digits_validation(some_password: str) -> bool:
    digits_counter = 0
    for ch in some_password:
        if ch.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input()

# triggers the three functions and puts their boolean results in a list
valid_password = [length_validation(password), symbol_validation(password), digits_validation(password)]
if all(valid_password):
    print("Password is valid")
