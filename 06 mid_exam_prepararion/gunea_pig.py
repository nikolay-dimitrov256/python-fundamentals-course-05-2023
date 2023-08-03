food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())

day = 0
enough = False

while day < 30:
    day += 1
    food_kg -= 0.300

    if day % 2 == 0:
        hay_kg -= food_kg * 0.05
    if day % 3 == 0:
        cover_kg -= weight_kg / 3

    if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
        break

else:
    enough = True

if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
