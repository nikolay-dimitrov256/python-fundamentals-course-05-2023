train = [0] * int(input())

while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    if command[0] == 'add':
        people = int(command[1])
        train[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people

    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)
