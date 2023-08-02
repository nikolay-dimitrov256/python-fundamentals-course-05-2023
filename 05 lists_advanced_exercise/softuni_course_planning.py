def add_lesson(lesson_title: str, lessons_list: list) -> list:
    if lesson_title not in lessons_list:
        lessons_list.append(lesson_title)
    return lessons_list


def insert_lesson(lesson_title: str, index: int, lessons_list: list) -> list:
    if lesson_title not in lessons_list:
        lessons_list.insert(index, lesson_title)
    return lessons_list


def remove_lesson(lesson_title: str, lessons_list: list) -> list:
    if lesson_title in lessons_list:
        next_index = lessons_list.index(lesson_title) + 1
        if next_index in range(len(lessons_list)):
            if "Exercise" in lessons_list[next_index]:
                lessons_list.pop(next_index)

        lessons_list.remove(lesson_title)

    return lessons_list


def swap_lessons(lesson_title_1: str, lesson_title_2: str, lessons_list: list) -> list:
    if lesson_title_1 in lessons_list and lesson_title_2 in lessons_list:
        lesson_one_index = lessons_list.index(lesson_title_1)
        lesson_two_index = lessons_list.index(lesson_title_2)
        first_has_exercise = False
        second_has_exercise = False

        if lesson_one_index + 1 in range(len(lessons_list)):
            first_has_exercise = "Exercise" in lessons_list[lesson_one_index + 1]
        if lesson_two_index + 1 in range(len(lessons_list)):
            second_has_exercise = "Exercise" in lessons_list[lesson_two_index + 1]

        if first_has_exercise and second_has_exercise:
            lessons_list[lesson_one_index], lessons_list[lesson_one_index + 1], \
                lessons_list[lesson_two_index], lessons_list[lesson_two_index + 1] = \
                lessons_list[lesson_two_index], lessons_list[lesson_two_index + 1], \
                lessons_list[lesson_one_index], lessons_list[lesson_one_index + 1]

        elif first_has_exercise:
            lessons_list[lesson_one_index], lessons_list[lesson_two_index] = \
                lessons_list[lesson_two_index], lessons_list[lesson_one_index]
            lessons_list.insert(lesson_two_index + 1, lessons_list.pop(lesson_one_index + 1))

        elif second_has_exercise:
            lessons_list[lesson_one_index], lessons_list[lesson_two_index] = \
                lessons_list[lesson_two_index], lessons_list[lesson_one_index]
            lessons_list.insert(lesson_one_index + 1, lessons_list.pop(lesson_two_index + 1))

        else:
            lessons_list[lesson_one_index], lessons_list[lesson_two_index] = \
                lessons_list[lesson_two_index], lessons_list[lesson_one_index]

    return lessons_list


def add_exercise(lesson_title: str, lessons_list: list) -> list:
    if lesson_title in lessons_list:
        index_lesson = lessons_list.index(lesson_title)
        if index_lesson + 1 in range(len(lessons_list)) and "Exercise" not in lessons_list[index_lesson + 1]:
            lessons_list.insert(index_lesson + 1, f"{lesson_title}-Exercise")
        elif index_lesson == len(lessons_list) - 1:
            lessons_list.append(f"{lesson_title}-Exercise")

    else:
        lessons_list.append(lesson_title)
        lessons_list.append(f"{lesson_title}-Exercise")

    return lessons_list


lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command = command.split(":")

    if command[0] == 'Add':
        lesson = command[1]
        lessons = add_lesson(lesson, lessons)

    elif command[0] == 'Insert':
        title = command[1]
        lesson_index = int(command[2])
        lessons = insert_lesson(title, lesson_index, lessons)

    elif command[0] == 'Remove':
        title = command[1]
        lessons = remove_lesson(title, lessons)

    elif command[0] == 'Swap':
        first_lesson = command[1]
        second_lesson = command[2]
        lessons = swap_lessons(first_lesson, second_lesson, lessons)

    elif command[0] == 'Exercise':
        lesson = command[1]
        lessons = add_exercise(lesson, lessons)

for i in range(len(lessons)):
    print(f"{i + 1}.{lessons[i]}")
