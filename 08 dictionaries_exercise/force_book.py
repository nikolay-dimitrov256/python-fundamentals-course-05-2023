def add_user(sides_dict: dict, side: str, user: str) -> dict:
    for key, value in sides_dict.items():
        if user in value:
            break
    else:
        if side not in sides_dict:
            sides_dict[side] = []
        sides_dict[side].append(user)

    return sides_dict


def change_sides(sides_dict: dict, user: str, side: str) -> dict:
    if side not in sides_dict:
        sides_dict[side] = []

    for key, value in sides_dict.items():
        if user in value:
            sides_dict[key].remove(user)
            sides_dict[side].append(user)
            break

    else:
        sides_dict[side].append(user)

    print(f'{user} joins the {side} side!')

    return sides_dict


force_sides = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if '|' in line:
        force_side, force_user = line.split(' | ')
        force_sides = add_user(force_sides, force_side, force_user)

    elif '->' in line:
        force_user, force_side = line.split(' -> ')
        force_sides = change_sides(force_sides, force_user, force_side)

for f_side, f_users in force_sides.items():
    if force_sides[f_side]:
        print(f'Side: {f_side}, Members: {len(f_users)}')
        for f_user in f_users:
            print(f'! {f_user}')
