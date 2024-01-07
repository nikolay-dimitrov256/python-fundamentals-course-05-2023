def walk_path(matrix: list, row: int, col: int, path: list, moves: int) -> int:
    global found_exit
    path.append((row, col))
    moves += 1

    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]

        if next_row not in range(rows) or next_col not in range(len(matrix[0])):
            found_exit = True
        elif matrix[next_row][next_col] == '#':
            continue
        elif (next_row, next_col) in path:
            continue
        elif matrix[next_row][next_col] == ' ':
            return walk_path(matrix, next_row, next_col, path, moves)

    return moves


rows = int(input())

maze = []
kate = []
exit_position = []
longest_path = []
current_path = []
number_of_moves = 0
found_exit = False
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for row_i in range(rows):
    maze.append(list(input()))
    for col_i in range(len(maze[0])):
        if maze[row_i][col_i] == 'k':
            kate = [row_i, col_i]

start_row, start_col = kate

number_of_moves = walk_path(maze, start_row, start_col, current_path, number_of_moves)

if found_exit:
    print(f'Kate got out in {number_of_moves} moves')
else:
    print('Kate cannot get out')
