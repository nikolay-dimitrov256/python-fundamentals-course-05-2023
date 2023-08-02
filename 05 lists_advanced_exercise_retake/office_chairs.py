n = int(input())

free_chairs = 0
enough_chairs = True

for room in range(1, n + 1):
    line = input().split()
    chairs = len(line[0])
    guests = int(line[1])

    if chairs >= guests:
        free_chairs += chairs - guests
    else:
        enough_chairs = False
        needed_chairs = guests - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
