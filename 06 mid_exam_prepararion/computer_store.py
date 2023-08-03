total_price_before_taxes = 0
total_taxes = 0
special = False

while True:
    command = input()
    if command == "special":
        special = True
        break
    elif command == "regular":
        break

    current_price = float(command)

    if current_price <= 0:
        print("Invalid price!")
        continue

    total_price_before_taxes += current_price
    total_taxes += current_price * 0.2

total_price_after_taxes = total_price_before_taxes + total_taxes
if special:
    total_price_after_taxes *= 0.9

if total_price_after_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_before_taxes:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_after_taxes:.2f}$")
