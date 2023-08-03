import re


def find_pairs(message: str) -> list:
    pattern = r'(@|#)(?P<one>[a-zA-Z]{3,})\1{2}(?P<two>[a-zA-Z]{3,})\1'
    matches = re.finditer(pattern, message)
    pairs = []

    for match in matches:
        match = match.groupdict()
        pairs.append(match)

    if pairs:
        print(f"{len(pairs)} word pairs found!")
    else:
        print("No word pairs found!")

    return pairs


def find_mirror_words(pairs: list):
    mirror_words = []

    for pair in pairs:
        if pair['one'] == pair['two'][::-1]:
            one, two = pair['one'], pair['two']
            mirror_words.append(f'{one} <=> {two}')

    if mirror_words:
        print('The mirror words are:')
        print(', '.join(mirror_words))

    else:
        print('No mirror words!')


def process_data(message: str):
    pairs = find_pairs(message)
    find_mirror_words(pairs)


data = input()

process_data(data)
