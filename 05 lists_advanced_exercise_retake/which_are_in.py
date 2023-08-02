searched_words = input().split(', ')
words = input().split(', ')

found_words = []

for string in searched_words:
    for word in words:
        if string in word:
            found_words.append(string)
            break

print(found_words)
