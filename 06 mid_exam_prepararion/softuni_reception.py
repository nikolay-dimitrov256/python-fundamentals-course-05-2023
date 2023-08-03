students_per_hour = int(input()) + int(input()) + int(input())
total_students = int(input())

hours = 0

while total_students > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    total_students -= students_per_hour

print(f"Time needed: {hours}h.")
