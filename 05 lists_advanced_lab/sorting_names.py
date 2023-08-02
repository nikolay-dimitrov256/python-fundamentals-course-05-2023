def sorted_names():
    list_names = input().split(", ")
    sorted_list = sorted(list_names, key=lambda x: (-len(x), x))

    return sorted_list


print(sorted_names())
