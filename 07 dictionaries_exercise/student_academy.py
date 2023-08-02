grades_count = int(input())

students = {}

for _ in range(grades_count):
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = []
    students[student].append(grade)

students_average = {student: sum(grades) / len(grades) for student, grades in students.items()}

for student, average_grade in students_average.items():
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')
