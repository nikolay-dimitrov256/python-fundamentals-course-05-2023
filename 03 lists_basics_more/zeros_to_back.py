list_strings = input().split(", ")
list_digits = []

for dig in list_strings:
    list_digits.append(int(dig))

for i in range(len(list_digits) - 1, -1, -1):
    if list_digits[i] == 0:
        list_digits.append(list_digits.pop(i))

print(list_digits)
