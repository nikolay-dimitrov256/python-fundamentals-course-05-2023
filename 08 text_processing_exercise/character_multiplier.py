first_string, second_string = input().split()

longer_string = first_string if len(first_string) > len(second_string) else second_string
shorter_string = first_string if longer_string == second_string else second_string
total_sum = 0

for i in range(len(shorter_string)):
    total_sum += ord(longer_string[i]) * ord(shorter_string[i])

for i in range(len(shorter_string), len(longer_string)):
    total_sum += ord(longer_string[i])

print(total_sum)
