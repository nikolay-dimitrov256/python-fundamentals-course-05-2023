companies = {}

while True:
    line = input()
    if line == 'End':
        break

    company, employee_id = line.split(' -> ')

    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f'-- {employee}')
