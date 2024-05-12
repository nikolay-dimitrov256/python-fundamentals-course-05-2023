dwarves = []

while True:
    line = input()
    if line == 'Once upon a time':
        break

    name, color, physics = line.split(' <:> ')
    physics = int(physics)

    found_dwarf = next((d for d in dwarves if d['name'] == name and d['color'] == color), None)

    if found_dwarf:
        found_dwarf['physics'] = physics if physics > found_dwarf['physics'] else found_dwarf['physics']
    else:
        dwarf = {'name': name, 'color': color, 'physics': physics}
        dwarves.append(dwarf)

for dwarf in dwarves:
    same_color_count = len([d for d in dwarves if d['color'] == dwarf['color']])
    dwarf['same color count'] = same_color_count

dwarves.sort(key=lambda x: (-x['physics'], -x['same color count']))

for dwarf in dwarves:
    print(f'({dwarf["color"]}) {dwarf["name"]} <-> {dwarf["physics"]}')
