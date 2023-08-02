def order(product, count):
    total_price = 0
    coffe_price = 1.50
    water_price = 1
    coke_price = 1.40
    snacks_price = 2
    if product == "coffee":
        total_price = count * coffe_price
    elif product == "water":
        total_price = count * water_price
    elif product == "coke":
        total_price = count * coke_price
    elif product == "snacks":
        total_price = count * snacks_price

    return f"{total_price:.2f}"


product_type = input()
product_count = int(input())

print(order(product_type, product_count))
