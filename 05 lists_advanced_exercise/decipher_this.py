message = input().split()

secret_message = []

for word in message:
    break_index = None

    for i in range(len(word)):
        if word[i].isalpha():
            break_index = i
            break

    first_letter = chr(int(word[:break_index]))
    remaining_word = word[break_index:]
    secret_word = first_letter + remaining_word
    secret_word = [ch for ch in secret_word]
    secret_word[1], secret_word[-1] = secret_word[-1], secret_word[1]
    secret_word = "".join(secret_word)
    secret_message.append(secret_word)

print(" ".join(secret_message))
