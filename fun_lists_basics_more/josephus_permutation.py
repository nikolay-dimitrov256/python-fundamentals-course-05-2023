circle_of_people = list(map(int, input().split()))
step = int(input())


executed_people = []
current_person = -1

while len(circle_of_people) > 0:
    current_person += step
    while current_person >= len(circle_of_people):
        current_person -= len(circle_of_people)

    executed_people.append(circle_of_people.pop(current_person))
    current_person -= 1

print("[", end="")
for item in range(len(executed_people) - 1):
    print(executed_people[item], end=",")
print(executed_people[-1], end="]")
