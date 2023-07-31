first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

left_column = [first_row[0], second_row[0], third_row[0]]
middle_column = [first_row[1], second_row[1], third_row[1]]
right_column = [first_row[2], second_row[2], third_row[2]]
first_diagonal = [first_row[0], second_row[1], third_row[2]]
second_diagonal = [first_row[2], second_row[1], third_row[0]]
winner = 0

if first_row.count(1) == 3 or second_row.count(1) == 3 or third_row.count(1) == 3 \
        or left_column.count(1) == 3 or middle_column.count(1) == 3 or right_column.count(1) == 3 \
        or first_diagonal.count(1) == 3 or second_diagonal.count(1) == 3:
    winner = 1
elif first_row.count(2) == 3 or second_row.count(2) == 3 or third_row.count(2) == 3 \
        or left_column.count(2) == 3 or middle_column.count(2) == 3 or right_column.count(2) == 3 \
        or first_diagonal.count(2) == 3 or second_diagonal.count(2) == 3:
    winner = 2

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
