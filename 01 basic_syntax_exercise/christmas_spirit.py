decorations_count = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

total_cost = 0
gained_spirit = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        decorations_count += 2

    if day % 2 == 0:
        total_cost += decorations_count * ornament_set_price
        gained_spirit += ornament_set_points
    if day % 3 == 0:
        total_cost += tree_skirt_price * decorations_count + tree_garland_price * decorations_count
        gained_spirit += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_cost += decorations_count * tree_lights_price
        gained_spirit += tree_lights_points
        if day % 3 == 0:
            gained_spirit += 30

    if day % 10 == 0:
        gained_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_until_christmas % 10 == 0:
    gained_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")
