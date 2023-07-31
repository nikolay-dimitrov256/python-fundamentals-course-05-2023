money_as_string = input().split(', ')
beggars = int(input())

money_as_digits = []

for item in money_as_string:
    money_as_digits.append(int(item))

start_index = 0
beggars_revenue_list = []

while start_index < beggars:
    current_beggar_revenue = 0
    for number in range(start_index, len(money_as_digits), beggars):
        current_beggar_revenue += money_as_digits[number]

    beggars_revenue_list.append(current_beggar_revenue)
    start_index += 1

print(beggars_revenue_list)
