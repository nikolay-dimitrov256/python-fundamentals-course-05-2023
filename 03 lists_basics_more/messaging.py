numbers_sequence = input().split(" ")
symbols_sequence = input()

list_symbols = []
secret_word = ""

for ch in symbols_sequence:
    list_symbols.append(ch)

for item in numbers_sequence:
    index_value = 0

    for dig in item:
        index_value += int(dig)

    while index_value >= 0:
        for i in range(len(list_symbols)):
            if index_value == 0:
                secret_word += list_symbols[i]
                list_symbols.pop(i)
                index_value -= 1
                break
            else:
                index_value -= 1

print(secret_word)
