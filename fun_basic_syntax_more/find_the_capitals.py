input_string = input()

list_capitals = []

for index, character in enumerate(input_string):
    if "A" <= character <= "Z":
        list_capitals.append(index)

print(list_capitals)
