fires_list = input().split("#")
available_water = int(input())

total_effort = 0
total_fire = 0
high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)
cells_put_out = []

for item in fires_list:
    fire_cell = item.split(" = ")
    type_of_fire = fire_cell[0]
    value_of_cell = int(fire_cell[1])
    valid = False

    if type_of_fire == "High" and value_of_cell in high:
        valid = True
    elif type_of_fire == "Medium" and value_of_cell in medium:
        valid = True
    elif type_of_fire == "Low" and value_of_cell in low:
        valid = True

    if valid:
        if value_of_cell <= available_water:
            available_water -= value_of_cell
            cells_put_out.append(value_of_cell)
            total_fire += value_of_cell
            total_effort += value_of_cell * 0.25

print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
