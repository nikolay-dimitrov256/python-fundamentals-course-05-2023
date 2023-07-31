# def is_palindrome(some_list: list):
#     for number in some_list:
#         if number == number[::-1]:
#             print(True)
#         else:
#             print(False)
#
#
# list_numbers = input().split(", ")
# is_palindrome(list_numbers)

def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False


list_numbers = input().split(", ")
for item in list_numbers:
    print(is_palindrome(item))
