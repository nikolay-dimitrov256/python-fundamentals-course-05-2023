rooms = int(input())

free_chairs = 0
all_seated = True

for room in range(1, rooms + 1):
    command = input().split()
    chairs = len(command[0])
    guests = int(command[1])

    if chairs < guests:
        all_seated = False
        print(f"{guests - chairs} more chairs needed in room {room}")
    else:
        free_chairs += chairs - guests

if all_seated:
    print(f"Game On, {free_chairs} free chairs left")
