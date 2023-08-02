number_of_lines = int(input())

balanced = False
opened = False

for ch in range(number_of_lines):
    input_string = input()

    if input_string == "(":
        if not opened:
            opened = True
        else:
            balanced = False
            break
    elif input_string == ")":
        if opened:
            balanced = True
            opened = False
        else:
            balanced = False
            break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
