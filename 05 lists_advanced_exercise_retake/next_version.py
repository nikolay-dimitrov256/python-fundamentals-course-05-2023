def version_change(current_version: list):
    current_version[-1] += 1

    for i in range(len(current_version) - 1, -1, -1):
        if current_version[i] > 9 and i != 0:
            current_version[i] = 0
            current_version[i - 1] += 1
        else:
            break

    print(*current_version, sep='.')


version = [int(num) for num in input().split('.')]

version_change(version)
