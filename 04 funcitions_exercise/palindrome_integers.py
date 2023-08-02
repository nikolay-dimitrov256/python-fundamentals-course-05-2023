def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False


list_numbers = input().split(", ")
for item in list_numbers:
    print(is_palindrome(item))
