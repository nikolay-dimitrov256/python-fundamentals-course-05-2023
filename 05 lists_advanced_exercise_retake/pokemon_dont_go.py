def modify_data(pokemons: list) -> int:
    sum_pokemons = 0
    while pokemons:
        index = int(input())
        value = 0

        if index < 0:
            index = 0
            value = pokemons[index]
            pokemons[index] = pokemons[-1]

        elif index >= len(pokemons):
            index = -1
            value = pokemons[index]
            pokemons[index] = pokemons[0]

        elif index in range(len(pokemons)):
            value = pokemons.pop(index)

        sum_pokemons += value

        for i in range(len(pokemons)):
            if pokemons[i] <= value:
                pokemons[i] += value
            else:
                pokemons[i] -= value

    return sum_pokemons


numbers = [int(num) for num in input().split()]

print(modify_data(numbers))
