def process_data(users_dict: dict, lang_dict: dict, data_line: list):
    user, language, points = data_line[0], data_line[1], int(data_line[2])
    if user not in users_dict:
        users_dict[user] = 0
    if language not in lang_dict:
        lang_dict[language] = 0
    if points > users_dict[user]:
        users_dict[user] = points
    lang_dict[language] += 1

    return users_dict, lang_dict


def ban_user(users_dict: dict, user: str):
    del users_dict[user]

    return users_dict


users_data = {}
languages = {}

while True:
    line = input()
    if line == 'exam finished':
        break

    line = line.split('-')

    if 'banned' in line:
        username = line[0]
        users_data = ban_user(users_data, username)
    else:
        users_data, languages = process_data(users_data, languages, line)

print(f'Results:')
for user, points in users_data.items():
    print(f'{user} | {points}')
print(f'Submissions:')
for language, submissions in languages.items():
    print(f'{language} - {submissions}')
