products = {}

while True:
    line = input()
    line = line.split(': ')
    if len(line) == 1:
        break

    product = line[0]
    quantity = int(line[1])
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

total_products = len(products)
total_quantity = sum(products.values())

print('Products in stock:')
for k, v in products.items():
    print(f'- {k}: {v}')
print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')
