lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_breaks = lost_fights_count // 2
sword_breaks = lost_fights_count // 3
shield_breaks = lost_fights_count // 6
armor_breaks = shield_breaks // 2

total_cost = helmet_breaks * helmet_price + sword_breaks * sword_price + \
             shield_breaks * shield_price + armor_breaks * armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")
