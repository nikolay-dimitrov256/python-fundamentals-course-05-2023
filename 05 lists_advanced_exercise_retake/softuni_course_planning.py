def add_lesson(courses: list, params: list) -> list:
    lesson = params[0]
    if lesson not in courses:
        courses.append(lesson)

    return courses


def insert_lesson(courses: list, params: list) -> list:
    lesson = params[0]
    index = int(params[1])

    if lesson not in courses and index in range(len(courses)):
        courses.insert(index, lesson)

    return courses


def remove_lesson(courses: list, params: list) -> list:
    lesson = params[0]

    if lesson in courses:
        lesson_index = courses.index(lesson)
        if lesson_index + 1 in range(len(courses)) and 'Exercise' in courses[lesson_index+1]:
            courses.pop(lesson_index+1)
        courses.remove(lesson)

    return courses


def swap_lessons(courses: list, params: list) -> list:
    first_lesson = params[0]
    second_lesson = params[1]

    if first_lesson in courses and second_lesson in courses:
        first_index = courses.index(first_lesson)
        second_index = courses.index(second_lesson)

        courses[first_index], courses[second_index] = courses[second_index], courses[first_index]

        if (first_index + 1 in range(len(courses)) and second_index + 1 in range(len(courses))
                and 'Exercise' in courses[first_index+1] and 'Exercise' in courses[second_index+1]):
            courses[first_index+1], courses[second_index+1] = courses[second_index+1], courses[first_index+1]

        elif first_index + 1 in range(len(courses)) and 'Exercise' in courses[first_index+1]:
            courses.insert(second_index+1, courses.pop(first_index+1))

        elif second_index + 1 in range(len(courses)) and 'Exercise' in courses[second_index+1]:
            courses.insert(first_index+1, courses.pop(second_index+1))

    return courses


def add_exercise(courses: list, params: list) -> list:
    lesson = params[0]

    if lesson in courses:
        lesson_index = courses.index(lesson)
        if lesson_index + 1 in range(len(courses)):
            if 'Exercise' not in courses[lesson_index+1]:
                courses.insert(lesson_index+1, f'{lesson}-Exercise')
        else:
            courses.append(f'{lesson}-Exercise')
    else:
        courses.append(lesson)
        courses.append(f'{lesson}-Exercise')

    return courses


def modify_data(courses: list) -> list:
    while True:
        command, *params = input().split(':')
        if command == 'course start':
            return courses

        if command == 'Add':
            courses = add_lesson(courses, params)

        elif command == 'Insert':
            courses = insert_lesson(courses, params)

        elif command == 'Remove':
            courses = remove_lesson(courses, params)

        elif command == 'Swap':
            courses = swap_lessons(courses, params)

        elif command == 'Exercise':
            courses = add_exercise(courses, params)


def base_function(courses: list):
    courses = modify_data(courses)

    for i in range(len(courses)):
        print(f'{i + 1}.{courses[i]}')


data = input().split(', ')

base_function(data)
