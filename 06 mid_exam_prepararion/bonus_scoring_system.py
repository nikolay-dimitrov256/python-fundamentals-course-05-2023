from math import ceil

students = int(input())
total_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
lectures_attended = 0

for _ in range(students):
    current_student_attendances = int(input())
    bonus = current_student_attendances / total_lectures * (5 + additional_bonus)

    if bonus > max_bonus:
        max_bonus = bonus
        lectures_attended = current_student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lectures_attended} lectures.")
