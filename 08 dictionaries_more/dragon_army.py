def clean_stats(stats):
    damage, health, armor = stats

    if damage == 'null':
        damage = 45
    else:
        damage = int(damage)

    if health == 'null':
        health = 250
    else:
        health = int(health)

    if armor == 'null':
        armor = 10
    else:
        armor = int(armor)

    return [damage, health, armor]


n = int(input())

dragons = {}

for i in range(n):
    dragon_type, name, damage, health, armor = input().split()

    damage, health, armor = clean_stats([damage, health, armor])

    if dragon_type not in dragons:
        dragons[dragon_type] = []

    existing_dragon = next((d for d in dragons[dragon_type] if d['name'] == name), None)

    if existing_dragon:
        existing_dragon['damage'] = damage
        existing_dragon['health'] = health
        existing_dragon['armor'] = armor
    else:
        dragon = {'name': name, 'damage': damage, 'health': health, 'armor': armor}
        dragons[dragon_type].append(dragon)

for d_type, dragons_list in dragons.items():
    dragons_count = len(dragons_list)
    avg_damage = sum(d['damage'] for d in dragons_list) / dragons_count
    avg_health = sum(d['health'] for d in dragons_list) / dragons_count
    avg_armor = sum(d['armor'] for d in dragons_list) / dragons_count

    print(f'{d_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})')

    dragons_list = sorted(dragons_list, key=lambda x: x['name'])

    for d in dragons_list:
        print(f"-{d['name']} -> damage: {d['damage']}, health: {d['health']}, armor: {d['armor']}")
