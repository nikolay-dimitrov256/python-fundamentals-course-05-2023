number_of_lines = int(input())

tank_capacity = 255

for liters in range(number_of_lines):
    liters_added = int(input())

    if liters_added > tank_capacity:
        print("Insufficient capacity!")
        continue

    tank_capacity -= liters_added

water_poured = 255 - tank_capacity

print(water_poured)
