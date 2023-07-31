available_products = input().split("|")
budget = int(input())

train_ticket_price = 150
sold_products_prices = []
total_spent = 0

for item in available_products:
    product = item.split("->")
    type_of_product = product[0]
    price_of_product = float(product[1])
    valid_price = False

    if type_of_product == "Clothes" and price_of_product <= 50:
        valid_price = True
    elif type_of_product == "Shoes" and price_of_product <= 35:
        valid_price = True
    elif type_of_product == "Accessories" and price_of_product <= 20.50:
        valid_price = True

    if valid_price and price_of_product <= budget:
        total_spent += price_of_product
        budget -= price_of_product
        price_of_product *= 1.4
        sold_products_prices.append(price_of_product)

total_revenue = sum(sold_products_prices)
profit = total_revenue - total_spent

for price in sold_products_prices:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + total_revenue >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
