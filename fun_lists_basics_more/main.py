# list_numbers = [1, 10, 100, 1000]
# some_index = 10
#
# if some_index not in range(len(list_numbers)):
#     print("Invalid index")
# right_part = list_numbers[some_index + 1:]
# for _ in range(len(right_part)):
#     list_numbers.insert(0, list_numbers.pop(-1))
# print(list_numbers)

some_list = [1, 2]
some_list.insert(0, some_list.pop(-1))
some_list.insert(0, some_list.pop(-1))
print(some_list)