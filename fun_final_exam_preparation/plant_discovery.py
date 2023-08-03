def rate_plant(plants: dict, params: str) -> dict:
    plant, rating = params.split(' - ')
    rating = int(rating)

    if plant in plants.keys():
        plants[plant]['ratings'].append(rating)
    else:
        print('error')

    return plants


def update_rarity(plants: dict, params: str) -> dict:
    plant, new_rarity = params.split(' - ')

    if plant in plants.keys():
        plants[plant]['rarity'] = int(new_rarity)
    else:
        print('error')

    return plants


def reset_ratings(plants: dict, plant: str) -> dict:
    if plant in plants.keys():
        plants[plant]['ratings'].clear()
    else:
        print('error')

    return plants


def modify_data(plants: dict) -> dict:
    while True:
        command = input()

        if command == 'Exhibition':
            return plants

        command, params = command.split(': ')

        if command == 'Rate':
            plants = rate_plant(plants, params)

        elif command == 'Update':
            plants = update_rarity(plants, params)

        elif command == 'Reset':
            plants = reset_ratings(plants, params)


def main_function(number: int):
    plants = {}
    for _ in range(number):
        plant, rarity = input().split('<->')
        plants[plant] = {'rarity': int(rarity), 'ratings': []}

    plants = modify_data(plants)

    print("Plants for the exhibition:")
    for current_plant, data in plants.items():
        average_rating = sum(data['ratings']) / len(data['ratings']) if data['ratings'] else 0
        print(f"- {current_plant}; Rarity: {data['rarity']}; Rating: {average_rating:.2f}")


n = int(input())

main_function(n)
