events = input().split("|")

energy = 100
coins = 100

for element in events:
    event, value = element.split("-")
    value = int(value)
    gained_energy = value
    if event == "rest":
        if energy + gained_energy > 100:
            gained_energy = 100 - energy
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        earned_coins = value
        if energy >= 30:
            energy -= 30
            coins += earned_coins
            print(f"You earned {earned_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        ingredient = event
        ingredient_price = value
        if ingredient_price <= coins:
            coins -= ingredient_price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
