from math import ceil

budget = float(input())
students = int(input())
price_package_flour = float(input())
price_for_one_egg = float(input())
price_for_apron = float(input())

free_flour = students // 5
flour_costs = (students - free_flour) * price_package_flour
eggs_costs = students * 10 * price_for_one_egg
aprons_count = ceil(students * 1.2)
aprons_costs = aprons_count * price_for_apron

total_costs = flour_costs + eggs_costs + aprons_costs

if total_costs <= budget:
    print(f"Items purchased for {total_costs:.2f}$.")
else:
    diff = total_costs - budget
    print(f"{diff:.2f}$ more needed.")
