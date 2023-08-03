import re


def decrypt_message(encrypted_message: str) -> str:
    decrypted_message = ''
    key_letters_count = 0

    for ch in encrypted_message:
        if ch.lower() in ['s', 't', 'a', 'r']:
            key_letters_count += 1

    for ch in encrypted_message:
        decrypted_message += chr(ord(ch) - key_letters_count)

    return decrypted_message


number_of_messages = int(input())

attacked_planets = []
destroyed_planets = []

for _ in range(number_of_messages):
    message = input()

    message = decrypt_message(message)
    pattern = r'@([a-zA-Z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)'
    matches = re.search(pattern, message)
    if matches:
        planet = matches.group(1)
        population = int(matches.group(2))
        attack_type = matches.group(3)
        soldiers = int(matches.group(4))
        if attack_type == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()

print(f'Attacked planets: {len(attacked_planets)}')
for attacked_planet in attacked_planets:
    print(f'-> {attacked_planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for destroyed_planet in destroyed_planets:
    print(f'-> {destroyed_planet}')
