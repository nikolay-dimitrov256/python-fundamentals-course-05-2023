string_input = input().lower()

list_words = []
temporary_word = ""

for ch in string_input:
    temporary_word += ch
    if "sand" in temporary_word or "water" in temporary_word or "fish" in temporary_word or "sun" in temporary_word:
        list_words.append(temporary_word)
        temporary_word = ""

print(len(list_words))