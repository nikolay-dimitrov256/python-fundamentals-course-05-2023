people = int(input())
wagons = [int(wagon) for wagon in input().split()]

MAX_CAPACITY = 4

for i in range(len(wagons)):
    free_places = MAX_CAPACITY - wagons[i]

    if people >= free_places:
        people -= free_places
        wagons[i] += free_places
    else:
        wagons[i] += people
        people = 0
        break

lift_full = sum(wagons) / len(wagons) == MAX_CAPACITY

if lift_full:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")
else:
    print("The lift has empty spots!")

print(*wagons)
