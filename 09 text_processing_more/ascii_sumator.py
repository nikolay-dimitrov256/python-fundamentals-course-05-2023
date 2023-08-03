first_ch, second_ch = input(), input()
string_to_pick = input()

total_sum = 0

for ch in string_to_pick:
#    if ord(ch) in range(ord(first_ch) + 1, ord(second_ch)):
    if first_ch < ch < second_ch:
        total_sum += ord(ch)

print(total_sum)
