def todo_list():
    tasks_list = []
    while True:
        current_task = input()
        if current_task == "End":
            break
        tasks_list.append(current_task)

    tasks_list = sorted(tasks_list, key=lambda x: int(x.split("-")[0]))
    sorted_list = []
    for task in tasks_list:
        sorted_list.append(task.split('-')[1])

    return sorted_list


result = todo_list()
print(result)
