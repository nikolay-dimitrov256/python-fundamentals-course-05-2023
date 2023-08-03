stock_list = input().split()

stock = {}

for i in range(0, len(stock_list), 2):
    product = stock_list[i]
    quantity = int(stock_list[i + 1])
    stock[product] = quantity

print(stock)
