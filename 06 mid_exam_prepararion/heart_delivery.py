neighbourhood = [int(num) for num in input().split("@")]

index = 0
unserviced_houses = len(neighbourhood)
serviced_indexes = []

while True:
    command = input()
    if command == "Love!":
        break

    command = command.split()
    jump_length = int(command[1])
    index += jump_length

    if index >= len(neighbourhood):
        index = 0
    if index in serviced_indexes:
        print(f"Place {index} already had Valentine's day.")
        continue

    neighbourhood[index] -= 2

    if neighbourhood[index] == 0:
        unserviced_houses -= 1
        serviced_indexes.append(index)
        print(f"Place {index} has Valentine's day.")

all_done = unserviced_houses == 0

print(f"Cupid's last position was {index}.")
if all_done:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {unserviced_houses} places.")
