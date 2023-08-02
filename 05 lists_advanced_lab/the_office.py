def happy_employees():
    employees_list = [int(num) for num in input().split()]
    factor = int(input())
    happier_employees = []

    for employee in employees_list:
        happier_employees.append(employee * factor)

    employees_happy = [employee for employee in happier_employees if \
                       employee >= sum(happier_employees) / len(happier_employees)]

    if len(employees_happy) >= len(happier_employees) / 2:
        return f"Score: {len(employees_happy)}/{len(happier_employees)}. Employees are happy!"
    return f"Score: {len(employees_happy)}/{len(happier_employees)}. Employees are not happy!"


print(happy_employees())
