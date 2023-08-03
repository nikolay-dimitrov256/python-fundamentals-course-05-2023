resources_dict = {}

while True:
    current_resource = input()
    if current_resource == 'stop':
        break
    amount = int(input())

    if current_resource not in resources_dict:
        resources_dict[current_resource] = 0
    resources_dict[current_resource] += amount

for resource, quantity in resources_dict.items():
    print(f'{resource} -> {quantity}')
