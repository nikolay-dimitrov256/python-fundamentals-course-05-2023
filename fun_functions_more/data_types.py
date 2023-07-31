def data_manipulator(some_command: str, some_value):
    result = None
    if some_command == "int":
        some_value = int(some_value)
        result = some_value * 2
    elif some_command == "real":
        some_value = float(some_value)
        result = f"{some_value * 1.5:.2f}"
    elif some_command == "string":
        result = f"${some_value}$"

    return result


command = input()
value = input()

print(data_manipulator(command, value))
