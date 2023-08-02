words = input().split()

word_occurrences = {}

for word in words:
    word = word.lower()
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1

for word, count in word_occurrences.items():
    if count % 2 != 0:
        print(word, end=' ')
