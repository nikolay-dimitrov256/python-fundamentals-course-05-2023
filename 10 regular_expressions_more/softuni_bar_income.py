import re

pattern = r'%([A-Z][a-z]+)%[^\|\$%\.]*<(\w+)>[^\|\$%\.]*\|(\d+)\|[^\|\$%\.]*([1-9][0-9]*\.?\d+)\$'
total_income = 0

while True:
    line = input()
    if line == 'end of shift':
        break

    matches = re.search(pattern, line)
    if matches:
        customer = matches.group(1)
        product = matches.group(2)
        count = int(matches.group(3))
        price = float(matches.group(4))
        total_price = count * price
        total_income += total_price
        print(f'{customer}: {product} - {total_price:.2f}')

print(f"Total income: {total_income:.2f}")
