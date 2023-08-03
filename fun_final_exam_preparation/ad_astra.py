import re

food_items = input()

pattern = r'(#|\|)([a-zA-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.finditer(pattern, food_items)
food = []
total_calories = 0

for match in matches:
    food_type = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))
    food_item = {'name': food_type, 'expiration date': expiration_date, 'calories': calories}
    food.append(food_item)
    total_calories += calories

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for item in food:
    name = item['name']
    expiration_date = item['expiration date']
    calories = item['calories']
    print(f'Item: {name}, Best before: {expiration_date}, Nutrition: {calories}')
