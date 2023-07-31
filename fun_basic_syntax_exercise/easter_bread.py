budget = float(input())
flour_price_kg = float(input())

eggs_price = flour_price_kg * 0.75
lt_milk_price = flour_price_kg * 1.25 / 4
bread_cost = flour_price_kg + eggs_price + lt_milk_price

loaves_of_bread = 0
colored_eggs_received = 0

while True:
    if bread_cost < budget:
        budget -= bread_cost
        loaves_of_bread += 1
        colored_eggs_received += 3

        if loaves_of_bread % 3 == 0:
            colored_eggs_received -= loaves_of_bread - 2

    else:
        break

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs_received} eggs "
      f"and {budget:.2f}BGN left.")
