# import re
#
# number_of_lines = int(input())
#
# pattern = r'@([A-Za-z]+)\|.*#(\d+)\*'
#
# for _ in range(number_of_lines):
#     line = input()
#
#     matches = re.search(pattern, line)
#
#     if matches:
#         name = matches.group(1)
#         age = matches.group(2)
#         print(f'{name} is {age} years old.')

number_of_lines = int(input())
for _ in range(number_of_lines):
    line = input()

    name = ''
    age = ''
    flag_name = False
    flag_age = False
    for ch in line:
        if ch == '@':
            flag_name = True
            continue
        elif ch == '|':
            flag_name = False
        elif ch == '#':
            flag_age = True
            continue
        elif ch == '*':
            flag_age = False

        if flag_name:
            name += ch
        elif flag_age:
            age += ch

    print(f'{name} is {age} years old.')
