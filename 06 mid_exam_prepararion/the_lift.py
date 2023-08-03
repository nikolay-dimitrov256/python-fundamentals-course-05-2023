passengers = int(input())
wagons = [int(num) for num in input().split()]

for i in range(len(wagons)):
    wagon_capacity = 4 - wagons[i]
    if passengers >= wagon_capacity:
        wagons[i] = 4
        passengers -= wagon_capacity
    else:
        wagons[i] += passengers
        passengers = 0

lift_full = sum(wagons) / len(wagons) == 4
wagons = [str(wagon) for wagon in wagons]

if passengers > 0:
    print(f"There isn't enough space! {passengers} people in a queue!")
    print(" ".join(wagons))
else:
    if lift_full:
        print(" ".join(wagons))
    else:
        print(f"The lift has empty spots!")
        print(" ".join(wagons))
