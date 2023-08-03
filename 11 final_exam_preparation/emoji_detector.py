import re


def find_threshold(text: str) -> int:
    numbers = re.findall('\\d', text)
    threshold = int(numbers[0])
    for i in range(1, len(numbers)):
        threshold *= int(numbers[i])

    return threshold


def find_emojis(text: str) -> list:
    pattern = r'(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1'
    matches = re.findall(pattern, text)
    emojis = []
    for match in matches:
        symbols = match[0]
        emoji = match[1]
        emojis.append({'emoji': emoji, 'symbols': symbols})

    return emojis


def find_cool_emojis(emojis: list, cool_threshold: int) -> list:
    cool_emojis = []
    for emoji in emojis:
        coolness = 0
        for letter in emoji['emoji']:
            coolness += ord(letter)

        if coolness > cool_threshold:
            cool_emojis.append(emoji)

    return cool_emojis


def base_function(text: str):
    cool_threshold = find_threshold(text)
    all_emojis = find_emojis(text)
    cool_emojis = find_cool_emojis(all_emojis, cool_threshold)

    print(f"Cool threshold: {cool_threshold}")
    print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
    for current_emoji in cool_emojis:
        emoji = current_emoji['emoji']
        symbols = current_emoji['symbols']
        print(symbols + emoji + symbols)


data = input()

base_function(data)
