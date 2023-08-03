energy = int(input())

battles_won = 0
success = False

while True:
    command = input()
    if command == "End of battle":
        success = True
        break

    distance = int(command)

    if distance > energy:
        break

    energy -= distance
    battles_won += 1

    if battles_won % 3 == 0:
        energy += battles_won

if success:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
