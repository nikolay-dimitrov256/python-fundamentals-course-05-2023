import re


def decipher_message(message: list):
    decoded_message = []
    for word in message:
        pattern = r'(?P<first>\d+)(?P<rest>[A-Za-z]+)'
        match = re.fullmatch(pattern, word)
        match = match.groupdict()
        first_char = chr(int(match['first']))
        remaining_word = [ch for ch in match['rest']]
        remaining_word[0], remaining_word[-1] = remaining_word[-1], remaining_word[0]
        decoded_word = first_char + ''.join(remaining_word)
        decoded_message.append(decoded_word)

    decoded_message = ' '.join(decoded_message)

    return decoded_message


data = input().split()

print(decipher_message(data))
