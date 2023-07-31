numbers_sequence = input().split(" ")

middle = len(numbers_sequence) // 2
left_part = numbers_sequence[:middle]
right_part = numbers_sequence[middle:]
left_car_time = 0
right_car_time = 0

for i_left in range(len(left_part)):
    left_time = int(left_part[i_left])
    left_car_time += left_time

    if left_time == 0:
        left_car_time *= 0.80

for i_right in range(len(right_part) - 1, 0, -1):
    right_time = int(right_part[i_right])
    right_car_time += right_time

    if right_time == 0:
        right_car_time *= 0.80

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
