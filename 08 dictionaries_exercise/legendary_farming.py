materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}

legendary_item = ''

while True:
    line = input().split()

    for i in range(0, len(line), 2):
        quantity, material = int(line[i]), line[i + 1].lower()

        if material not in materials_dict:
            materials_dict[material] = 0
        materials_dict[material] += quantity

        if materials_dict['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            materials_dict['shards'] -= 250

        elif materials_dict['fragments'] >= 250:
            legendary_item = 'Valanyr'
            materials_dict['fragments'] -= 250

        elif materials_dict['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            materials_dict['motes'] -= 250

        if legendary_item:
            break

    if legendary_item:
        break

print(f'{legendary_item} obtained!')
for key, value in materials_dict.items():
    print(f'{key}: {value}')
