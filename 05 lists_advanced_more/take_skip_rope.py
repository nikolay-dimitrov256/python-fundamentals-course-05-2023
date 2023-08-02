initial_string = input()

numbers_list = [int(ch) for ch in initial_string if ch.isdigit()]
non_numbers_list = [ch for ch in initial_string if not ch.isdigit()]

taken_string = ""
skipped_string = ""

for i in range(len(numbers_list)):
    if i % 2 == 0:
        for _ in range(numbers_list[i]):
            if non_numbers_list:
                taken_string += non_numbers_list.pop(0)
    else:
        for _ in range(numbers_list[i]):
            if non_numbers_list:
                skipped_string += non_numbers_list.pop(0)

print(taken_string)
