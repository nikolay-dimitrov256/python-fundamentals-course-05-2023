def like(followers: dict, params: list) -> dict:
    username = params[0]
    count = int(params[1])

    if username not in followers:
        followers[username] = {'likes': 0, 'comments': 0}
    followers[username]['likes'] += count

    return followers


def comment(followers: dict, params: list) -> dict:
    username = params[0]

    if username not in followers:
        followers[username] = {'likes': 0, 'comments': 0}
    followers[username]['comments'] += 1

    return followers


def blocked(followers: dict, params: list) -> dict:
    username = params[0]

    if username in followers:
        followers.pop(username)
    else:
        print(f"{username} doesn't exist.")

    return followers


def new_follower(followers: dict, params: list) -> dict:
    username = params[0]

    if username not in followers:
        followers[username] = {'likes': 0, 'comments': 0}

    return followers


def main_function():
    followers = {}
    while True:
        command, *params = input().split(': ')

        if command == 'Log out':
            break

        if command == 'New follower':
            followers = new_follower(followers, params)

        elif command == 'Like':
            followers = like(followers, params)

        elif command == 'Comment':
            followers = comment(followers, params)

        elif command == 'Blocked':
            followers = blocked(followers, params)

    print(f'{len(followers)} followers')
    for username, stats in followers.items():
        print(f'{username}: {sum(stats.values())}')


main_function()
