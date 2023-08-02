numbers = [int(num) for num in input().split(', ')]

group = 10

while numbers:
    group_list = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num not in group_list]

    print(f"Group of {group}'s: {group_list}")
    group += 10
