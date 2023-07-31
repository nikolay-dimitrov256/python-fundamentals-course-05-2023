from math import floor, sqrt


def closer_point(x1: float, y1: float, x2: float, y2: float) -> str:
    distance_point1 = sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    distance_point2 = sqrt(abs(x2) ** 2 + abs(y2) ** 2)
    if distance_point2 < distance_point1:
    # if abs(x2) + abs(y2) < abs(x1) + abs(y1):
        return f"({floor(x2)}, {floor(y2)})"
    return f"({floor(x1)}, {floor(y1)})"


point1_x, point1_y = float(input()), float(input())
point2_x, point2_y = float(input()), float(input())

print(closer_point(point1_x, point1_y, point2_x, point2_y))
