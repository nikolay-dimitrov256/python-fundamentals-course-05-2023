# version_number = [num for num in input().split(".")]
# new_version_int = int("".join(version_number)) + 1
# new_version_list = []
#
# for num in str(new_version_int):
#     new_version_list.append(str(num))
#
# final_string = ".".join(new_version_list)
#
# print(final_string)

version_number = [int(num) for num in input().split(".")]

version_number[-1] += 1

for i in range(len(version_number) - 1, - 1, - 1):
    if version_number[i] > 9 and i != 0:
        version_number[i] = 0
        if i - 1 >= 0:
            version_number[i-1] += 1

print(".".join(str(number) for number in version_number))
