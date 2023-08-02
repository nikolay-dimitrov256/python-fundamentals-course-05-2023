def validate_password(some_password: str) -> bool:
    valid = True
    if len(some_password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False
    digits_counter = 0
    for ch in some_password:
        if ch.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        valid = False
    return valid


password = input()
valid_password = validate_password(password)
if valid_password:
    print("Password is valid")
