def chars_in_range(first_char, second_char):
    list_characters = []
    for current_character in range(ord(first_char) + 1, ord(second_char)):
        list_characters.append(chr(current_character))
    string_characters = " ".join(list_characters)
    return string_characters


first_character, second_character = input(), input()

print(chars_in_range(first_character, second_character))
