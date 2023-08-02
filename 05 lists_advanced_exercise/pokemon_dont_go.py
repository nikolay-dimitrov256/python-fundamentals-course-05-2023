pokemon_list = [int(num) for num in input().split()]

sum_removed_values = 0

while len(pokemon_list) > 0:
    index = int(input())
    popped_value = 0

    if index < 0:
        popped_value = pokemon_list.pop(0)
        pokemon_list.insert(0, pokemon_list[-1])
    elif index >= len(pokemon_list):
        popped_value = pokemon_list.pop(-1)
        pokemon_list.append(pokemon_list[0])
    else:
        popped_value = pokemon_list.pop(index)

    sum_removed_values += popped_value

    for i in range(len(pokemon_list)):
        if pokemon_list[i] <= popped_value:
            pokemon_list[i] += popped_value
        else:
            pokemon_list[i] -= popped_value
    # pokemon_list = [poke + popped_value if poke <= popped_value else poke - popped_value for poke in pokemon_list]

print(sum_removed_values)
