number_of_orders = int(input())

total_price = 0

for _ in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= capsule_price <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsules_per_day <= 2000:
        continue

    coffee_price = capsule_price * days * capsules_per_day
    total_price += coffee_price

    print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
