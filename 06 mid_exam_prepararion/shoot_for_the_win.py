targets = [int(num) for num in input().split()]

shot_targets_count = 0
shot_indexes = []

while True:
    command = input()
    if command == "End":
        break

    index = int(command)

    if index not in shot_indexes and index in range(len(targets)):
        shot_indexes.append(index)
        shot_targets_count += 1

        for i in range(len(targets)):
            if i not in shot_indexes:
                if targets[i] > targets[index]:
                    targets[i] -= targets[index]
                else:
                    targets[i] += targets[index]

        targets[index] = -1

print(f"Shot targets: {shot_targets_count} ->", *targets)
