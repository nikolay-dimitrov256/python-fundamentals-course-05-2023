items = input().split()

stock = {}

for i in range(0, len(items), 2):
    product = items[i]
    quantity = int(items[i + 1])
    stock[product] = quantity

search_items = input().split()

for item in search_items:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
