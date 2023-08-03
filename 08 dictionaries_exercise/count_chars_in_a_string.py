characters = [ch for ch in input() if ch != ' ']

chars_dict = {}

for ch in characters:
    if ch not in chars_dict:
        chars_dict[ch] = 0
    chars_dict[ch] += 1

for char, counter in chars_dict.items():
    print(f"{char} -> {counter}")
