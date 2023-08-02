first_sequence = input().split(", ")
second_sequence = input().split(", ")

matched_words = []

for word_first in first_sequence:
    for word_second in second_sequence:

        if word_first in word_second:
            matched_words.append(word_first)
            break

print(matched_words)
