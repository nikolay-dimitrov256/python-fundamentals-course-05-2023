def modify_data(cities: dict) -> dict:
    while True:
        command, *params = input().split('=>')

        if command == 'End':
            return cities

        if command == 'Plunder':
            cities = plunder(cities, params)

        elif command == 'Prosper':
            cities = prosper(cities, params)


def prosper(cities: dict, params: list) -> dict:
    town = params[0]
    gold = int(params[1])

    if gold < 0:
        print('Gold added cannot be a negative number!')
    else:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    return cities


def plunder(cities: dict, params: list) -> dict:
    town, people, gold = params
    cities[town]['population'] -= int(people)
    cities[town]['gold'] -= int(gold)

    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
        print(f"{town} has been wiped off the map!")
        del cities[town]

    return cities


def main_function():
    cities = {}
    while True:
        data = input()
        if data == 'Sail':
            break

        city, population, gold = data.split('||')
        if city not in cities:
            cities[city] = {'population': 0, 'gold': 0}
        cities[city]['population'] += int(population)
        cities[city]['gold'] += int(gold)

    cities = modify_data(cities)

    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for town, stats in cities.items():
            print(f"{town} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg")

    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


main_function()
