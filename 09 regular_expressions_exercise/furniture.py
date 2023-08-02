import re

pattern = r'>>([a-z]+)<<(\d+\.?\d*)!(\d+)'
total_cost = 0
bought_furniture = []

while True:
    command = input()
    if command == 'Purchase':
        break

    matched = re.search(pattern, command, re.I)
    if matched:
        furniture, price, count = matched.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(count)

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_cost:.2f}')
