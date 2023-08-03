contests_passwords = {}

while True:    # Stuff the contests dict
    contest_data = input()
    if contest_data == 'end of contests':
        break

    current_contest, correct_password = contest_data.split(':')
    contests_passwords[current_contest] = correct_password

participants = {}

while True:   # Stuff the participants dict
    submission_line = input()
    if submission_line == 'end of submissions':
        break

    contest, password, username, points = submission_line.split('=>')
    points = int(points)
    if contest in contests_passwords and contests_passwords[contest] == password:
        if username not in participants.keys():
            participants[username] = {}
        if contest not in participants[username].keys():
            participants[username][contest] = 0
        if points > participants[username][contest]:
            participants[username][contest] = points

most_points = 0   # Find the highest ranking participant
best_participant = None
for key, value in participants.items():
    total_points = sum(value.values())
    if total_points > most_points:
        most_points = total_points
        best_participant = key

print(f'Best candidate is {best_participant} with total {most_points} points.')

participants = dict(sorted(participants.items()))
for k, v in participants.items():
    participants[k] = dict(sorted(v.items(), key=lambda item: item[1], reverse=True))

print('Ranking:')
for user, results in participants.items():
    print(user)
    for language, result in results.items():
        print(f'#  {language} -> {result}')
