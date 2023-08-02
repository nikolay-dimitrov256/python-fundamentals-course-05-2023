import re

demons = [name.strip() for name in input().split(',')]
demons_stats = {}
pattern = r'([+-]?[0-9]+\.?[0-9]*)'

for demon in demons:
    demon_health = 0
    demon_damage = 0
    math_symbols = ''

    matches = re.findall(pattern, demon)

    for match in matches:
        demon_damage += float(match)

    for ch in demon:
        if not ch.isdigit() and ch not in ['+', '-', '*', '/', '.']:
            demon_health += ord(ch)
        elif ch in ['*', '/']:
            math_symbols += ch

    for symbol in math_symbols:
        if symbol == '*':
            demon_damage *= 2
        else:
            demon_damage /= 2

    demons_stats[demon] = {'health': demon_health, 'damage': demon_damage}

demons_stats = dict(sorted(demons_stats.items(), key=lambda x: x[0]))

for name, stats in demons_stats.items():
    print(f"{name} - {stats['health']} health, {stats['damage']:.2f} damage")
