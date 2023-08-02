list_numbers = [int(num) for num in input().split(", ")]

current_group_numbers = 10

while len(list_numbers) > 0:
    current_list = [num for num in list_numbers if num <= current_group_numbers]

    print(f"Group of {current_group_numbers}'s: {current_list}")

    list_numbers = [num for num in list_numbers if num not in current_list]
    current_group_numbers += 10
