def modify_data(heroes: dict):
    while True:
        command, *parameters = input().split(' - ')

        if command == 'End':
            return heroes

        if command == 'CastSpell':
            heroes = cast_spell(heroes, parameters)

        elif command == 'TakeDamage':
            heroes = take_damage(heroes, parameters)

        elif command == 'Recharge':
            heroes = recharge(heroes, parameters)

        elif command == 'Heal':
            heroes = heal(heroes, parameters)


def heal(heroes: dict, params: list) -> dict:
    hero, amount = params
    amount = int(amount)

    if heroes[hero]['HP'] + amount > 100:
        amount = 100 - heroes[hero]['HP']

    heroes[hero]['HP'] += amount
    print(f"{hero} healed for {amount} HP!")

    return heroes


def recharge(heroes: dict, params: list) -> dict:
    hero, amount = params
    amount = int(amount)

    if heroes[hero]['MP'] + amount > 200:
        amount = 200 - heroes[hero]['MP']

    heroes[hero]['MP'] += amount
    print(f"{hero} recharged for {amount} MP!")

    return heroes


def take_damage(heroes: dict, params: list) -> dict:
    hero, damage, attacker = params
    damage = int(damage)
    heroes[hero]['HP'] -= damage

    if heroes[hero]['HP'] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]

    return heroes


def cast_spell(heroes: dict, params: list) -> dict:
    hero, mp_needed, spell_name = params
    mp_needed = int(mp_needed)

    if heroes[hero]['MP'] >= mp_needed:
        heroes[hero]['MP'] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")

    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")

    return heroes


def base_function(number: int):
    heroes = {}
    for _ in range(number):
        hero, hp, mp = input().split()
        heroes[hero] = {'HP': int(hp), 'MP': int(mp)}

    heroes = modify_data(heroes)

    for current_hero, stats in heroes.items():
        print(current_hero)
        print(f"  HP: {stats['HP']}\n  MP: {stats['MP']}")


n = int(input())

base_function(n)
