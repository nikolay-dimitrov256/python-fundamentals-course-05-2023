rows = int(input())

field = []

for row in range(rows):
    current_row = [int(num) for num in input().split()]
    field.append(current_row)

attacks = input().split()
sunken_ships = 0

for attack in attacks:
    coordinates = attack.split("-")
    row = int(coordinates[0])
    col = int(coordinates[1])

    if field[row][col] > 0:
        field[row][col] -= 1

        if field[row][col] <= 0:
            sunken_ships += 1

print(sunken_ships)
