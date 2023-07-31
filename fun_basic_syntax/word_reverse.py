input_word = input()

# input_word = input_word[::-1]
#
# print(input_word)

for ch in range(len(input_word) - 1, -1, -1):
    print(input_word[ch], end="")
