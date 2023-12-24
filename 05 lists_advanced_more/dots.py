def walk_path(matrix: list, row_, col_, path: list):
    path.append((row_, col_))

    for direction in directions.values():
        next_row = row_ + direction[0]
        next_col = col_ + direction[1]

        if next_row not in range(number_of_rows) or next_col not in range(len(matrix[0])):
            continue
        elif matrix[next_row][next_col] != '.':
            continue
        elif (next_row, next_col) in path:
            continue
        else:
            walk_path(matrix, next_row, next_col, path)

    return path


number_of_rows = int(input())

rectangle = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(number_of_rows):
    rectangle.append(input().split())

longest_path = []
current_path = []

for row in range(number_of_rows):
    for col in range(len(rectangle[row])):
        if rectangle[row][col] == '.':
            current_path = []
            current_path = walk_path(rectangle, row, col, current_path)
            if len(current_path) > len(longest_path):
                longest_path = current_path

print(len(longest_path))
