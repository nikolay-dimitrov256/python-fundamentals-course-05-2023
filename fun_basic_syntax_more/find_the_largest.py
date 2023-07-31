# number = input()
#
# list_indexes = []
# largest_number = ''
# largest_digit = "0"
# index_largest_digit = None
#
# while True:
#     for index, digit in enumerate(number):
#         if str(index) in list_indexes:
#             continue
#
#         if digit >= largest_digit:
#             largest_digit = digit
#             index_largest_digit = index
#
#     list_indexes += str(index_largest_digit)
#     largest_number += largest_digit
#     largest_digit = "0"
#     index_largest_digit = None
#
#     if len(number) == len(list_indexes):
#         break
# print(largest_number)


number = input()

list_digits = []

for digit in number:
    list_digits.append(digit)

list_digits.sort(reverse=True)

print(''.join(list_digits))
