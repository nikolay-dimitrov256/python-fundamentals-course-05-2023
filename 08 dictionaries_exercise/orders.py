products = {}

while True:
    line = input().split()
    if line[0] == 'buy':
        break

    name, price, quantity = line[0], float(line[1]), int(line[2])

    if name not in products.keys():
        products[name] = {'price': 0.0, 'quantity': 0}
    products[name]['price'] = price
    products[name]['quantity'] += quantity

for name, value in products.items():
    total_price = value['price'] * value['quantity']
    print(f'{name} -> {total_price:.2f}')
