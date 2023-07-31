number_of_strings = int(input())

for _ in range(number_of_strings):
    input_string = input()
    pure = False
    for ch in input_string:
        if ch == ",":
            break
        elif ch == ".":
            break
        elif ch == "_":
            break
    else:
        pure = True

    if pure:
        print(f"{input_string} is pure.")
    else:
        print(f"{input_string} is not pure!")
