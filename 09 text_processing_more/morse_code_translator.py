def decode_word(morse_word: str):
    encoded_word = morse_word.split()
    decoded_word = ''

    for ch in encoded_word:
        for letter, code in morse_dictionary.items():
            if ch == code:
                decoded_word += letter

    return decoded_word


morse_code = input().split(' | ')

message = []
morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

for word in morse_code:
    word = decode_word(word)
    message.append(word)

print(' '.join(message))
