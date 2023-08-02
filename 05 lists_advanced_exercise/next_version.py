version_number = [int(num) for num in input().split(".")]

version_number[-1] += 1

for i in range(len(version_number) - 1, - 1, - 1):
    if version_number[i] > 9 and i != 0:
        version_number[i] = 0
        if i - 1 >= 0:
            version_number[i-1] += 1

print(".".join(str(number) for number in version_number))
