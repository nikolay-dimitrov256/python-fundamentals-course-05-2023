students = []
course_name = ''

while True:
    line = input()
    if ':' not in line:
        line = line.split('_')
        course_name = ' '.join(line)
        break

    line = line.split(":")
    current_name = line[0]
    student_id = line[1]
    course = line[2]
    students.append({'name': current_name, 'student_id': student_id, 'course': course})

for student in students:
    if student['course'] == course_name:
        print(f"{student['name']} - {student['student_id']}")
