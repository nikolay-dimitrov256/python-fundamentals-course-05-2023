players = {}

while True:
    line = input()
    if line == 'Season end':
        break

    if '->' in line:
        line = line.split(' -> ')
        player, position, skill = line[0], line[1], int(line[2])

        if player not in players:
            players[player] = {}
        if position not in players[player]:
            players[player][position] = 0
        if skill > players[player][position]:
            players[player][position] = skill

    elif ' vs ' in line:
        line = line.split(' vs ')
        player1, player2 = line[0], line[1]
        if player1 not in players or player2 not in players:
            continue

        player1_points = 0
        player2_points = 0
        for current_position in players[player1].keys():
            if current_position in players[player2]:
                player1_points += players[player1][current_position]
                player2_points += players[player2][current_position]

        if player1_points > player2_points:
            del players[player2]
        elif player2_points > player1_points:
            del players[player1]

# Sort skill of a player by points in descending order, then by name in ascending order
for current_player, current_skills in players.items():
    players[current_player] = dict(sorted(players[current_player].items(), key=lambda x: (-x[1], x[0])))

sorted_players = dict(sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for key, value in sorted_players.items():
    print(f"{key}: {sum(value.values())} skill")
    for k, v in value.items():
        print(f'- {k} <::> {v}')
