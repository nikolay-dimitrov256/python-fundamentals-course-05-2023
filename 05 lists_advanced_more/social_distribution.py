population = [int(num) for num in input().split(", ")]
min_wealth = int(input())

impossible = False

if sum(population) / len(population) < min_wealth:
    impossible = True
else:
    needed_money = 0
    for person in population:
        if person < min_wealth:
            needed_money += min_wealth - person

    while needed_money > 0:

        index_min = population.index(min(population))
        index_max = population.index(max(population))
        needed_money_for_person = min_wealth - population[index_min]
        distributed_money = needed_money_for_person \
            if population[index_max] - needed_money_for_person >= min_wealth else population[index_max] - min_wealth
        population[index_max] -= distributed_money
        population[index_min] += distributed_money
        needed_money -= distributed_money

if impossible:
    print("No equal distribution possible")
else:
    print(population)
