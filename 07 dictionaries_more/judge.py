contests_dict = {}
participants_dict = {}

while True:   # Stuff the contests dictionary
    input_line = input()
    if input_line == 'no more time':
        break

    input_line = input_line.split(' -> ')
    username, contest, points = input_line[0], input_line[1], int(input_line[2])
    if contest not in contests_dict:
        contests_dict[contest] = {}
    if username not in contests_dict[contest]:
        contests_dict[contest][username] = 0
    if points > contests_dict[contest][username]:
        contests_dict[contest][username] = points

for users in contests_dict.values():   # Stuff the participants dictionary from the contests dict
    for user, current_points in users.items():
        if user not in participants_dict:
            participants_dict[user] = 0
        participants_dict[user] += current_points

for key, value in contests_dict.items():
    contests_dict[key] = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))

participants_dict = dict(sorted(participants_dict.items(), key=lambda x: (-x[1], x[0])))

for subject, participants in contests_dict.items():
    print(f'{subject}: {len(participants)} participants')
    counter = 1
    for participant, current_score in participants.items():
        print(f'{counter}. {participant} <::> {current_score}')
        counter += 1

print('Individual standings:')
counter = 1
for student, total_points in participants_dict.items():
    print(f'{counter}. {student} -> {total_points}')
    counter += 1
