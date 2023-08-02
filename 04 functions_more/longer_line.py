from math import floor, sqrt


def line_comparison(some_list: list) -> str:
    # For the next four lines X values are on index[0], and Y values are on index[1]:
    first_line_point1 = [some_list[0], some_list[1]]
    first_line_point2 = [some_list[2], some_list[3]]
    second_line_point1 = [some_list[4], some_list[5]]
    second_line_point2 = [some_list[6], some_list[7]]
    first_rectangle_length = 0
    first_rectangle_height = 0
    second_rectangle_length = 0
    second_rectangle_height = 0
    if first_line_point1[0] >= 0 and first_line_point2[0] >= 0 \
            or first_line_point1[0] <= 0 and first_line_point2[0] <= 0:
        first_rectangle_length = abs(first_line_point1[0] - first_line_point2[0])
    else:
        first_rectangle_length = abs(first_line_point1[0]) + abs(first_line_point2[0])
    if first_line_point1[1] >= 0 and first_line_point2[1] >= 0 \
            or first_line_point1[1] <= 0 and first_line_point2[1] <= 0:
        first_rectangle_height = abs(first_line_point1[1] - first_line_point2[1])
    else:
        first_rectangle_height = abs(first_line_point1[1]) + abs(first_line_point2[1])

    if second_line_point1[0] >= 0 and second_line_point2[0] >= 0 \
            or second_line_point1[0] <= 0 and second_line_point2[0] <= 0:
        second_rectangle_length = abs(second_line_point1[0] - second_line_point2[0])
    else:
        second_rectangle_length = abs(second_line_point1[0]) + abs(second_line_point2[0])
    if second_line_point1[1] >= 0 and second_line_point2[1] >= 0 \
            or second_line_point1[1] <= 0 and second_line_point2[1] <= 0:
        second_rectangle_height = abs(second_line_point1[1] - second_line_point2[1])
    else:
        second_rectangle_height = abs(second_line_point1[1]) + abs(second_line_point2[1])

    length_fist_line = sqrt(first_rectangle_length ** 2 + first_rectangle_height ** 2)
    length_second_line = sqrt(second_rectangle_length ** 2 + second_rectangle_height ** 2)

    line_coordinates_to_return = None

    if length_second_line > length_fist_line:
        if sqrt(abs(second_line_point1[0]) ** 2 + abs(second_line_point1[1]) ** 2) \
                <= sqrt(abs(second_line_point2[0]) ** 2 + abs(second_line_point2[1]) ** 2):
            line_coordinates_to_return = f"({floor(second_line_point1[0])}, {floor(second_line_point1[1])})" \
                                         f"({floor(second_line_point2[0])}, {floor(second_line_point2[1])})"
        else:
            line_coordinates_to_return = f"({floor(second_line_point2[0])}, {floor(second_line_point2[1])})" \
                                         f"({floor(second_line_point1[0])}, {floor(second_line_point1[1])})"

    elif length_fist_line > length_second_line:
        if sqrt(abs(first_line_point1[0]) ** 2 + abs(first_line_point1[1]) ** 2) \
                <= sqrt(abs(first_line_point2[0]) ** 2 + abs(first_line_point2[1]) ** 2):
            line_coordinates_to_return = f"({floor(first_line_point1[0])}, {floor(first_line_point1[1])})" \
                                         f"({floor(first_line_point2[0])}, {floor(first_line_point2[1])})"
        else:
            line_coordinates_to_return = f"({floor(first_line_point2[0])}, {floor(first_line_point2[1])})" \
                                         f"({floor(first_line_point1[0])}, {floor(first_line_point1[1])})"
    else:
        if sqrt(abs(first_line_point1[0]) ** 2 + abs(first_line_point1[1]) ** 2) \
                <= sqrt(abs(first_line_point2[0]) ** 2 + abs(first_line_point2[1]) ** 2):
            line_coordinates_to_return = f"({floor(first_line_point1[0])}, {floor(first_line_point1[1])})" \
                                         f"({floor(first_line_point2[0])}, {floor(first_line_point2[1])})"
        else:
            line_coordinates_to_return = f"({floor(first_line_point2[0])}, {floor(first_line_point2[1])})" \
                                         f"({floor(first_line_point1[0])}, {floor(first_line_point1[1])})"

    return line_coordinates_to_return


list_coordinates = []
for _ in range(8):
    list_coordinates.append(float(input()))

print(line_comparison(list_coordinates))
