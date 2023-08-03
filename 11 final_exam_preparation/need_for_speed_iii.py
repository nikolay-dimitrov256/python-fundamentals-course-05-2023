def drive(cars: dict, parameters: list) -> dict:
    car, distance, fuel = parameters
    fuel = int(fuel)
    distance = int(distance)

    if cars[car]['fuel'] >= fuel:
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]['mileage'] >= 100_000:
            print(f"Time to sell the {car}!")
            del cars[car]

    else:
        print('Not enough fuel to make that ride')

    return cars


def refuel(cars: dict, params: list) -> dict:
    car, fuel = params
    fuel = int(fuel)
    tank_capacity = 75

    if cars[car]['fuel'] + fuel > tank_capacity:
        fuel = tank_capacity - cars[car]['fuel']

    cars[car]['fuel'] += fuel
    print(f"{car} refueled with {fuel} liters")

    return cars


def revert(cars: dict, params: list) -> dict:
    car, kilometers = params
    kilometers = int(kilometers)
    cars[car]['mileage'] -= kilometers

    if cars[car]['mileage'] >= 10_000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        cars[car]['mileage'] = 10_000

    return cars


def modify_data(cars: dict) -> dict:
    while True:
        command, *params = input().split(' : ')
        if command == 'Stop':
            return cars

        if command == 'Drive':
            cars = drive(cars, params)

        elif command == 'Refuel':
            cars = refuel(cars, params)

        elif command == 'Revert':
            cars = revert(cars, params)


def base_function(number: int):
    cars = {}
    for _ in range(number):
        car, mileage, fuel = input().split('|')
        cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

    cars = modify_data(cars)

    for vehicle, data in cars.items():
        kms = data['mileage']
        gas = data['fuel']
        print(f"{vehicle} -> Mileage: {kms} kms, Fuel in the tank: {gas} lt.")


n = int(input())

base_function(n)
