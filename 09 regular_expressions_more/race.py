competitors = {name: 0 for name in input().split(', ')}

while True:
    command = input()
    if command == 'end of race':
        break

    competitor = ''
    distance = 0

    for ch in command:
        if ch.isalpha():
            competitor += ch
        elif ch.isdigit():
            distance += int(ch)

    if competitor in competitors:
        competitors[competitor] += int(distance)

competitors = dict(sorted(competitors.items(), key=lambda x: x[1], reverse=True))
winners = [name for name in competitors.keys()]

print(f'1st place: {winners[0]}')
print(f'2nd place: {winners[1]}')
print(f'3rd place: {winners[2]}')
