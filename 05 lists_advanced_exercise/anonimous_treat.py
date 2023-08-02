list_strings = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    command = command.split()

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0:
            start_index = 0

        if end_index >= len(list_strings):
            end_index = len(list_strings) - 1

        if start_index not in range(len(list_strings)) or end_index not in range(len(list_strings)):
            continue

        new_string = []
        indexes_to_pop = []

        for i in range(end_index, start_index - 1, - 1):
            new_string.append(list_strings.pop(i))

        new_string.reverse()
        new_string = "".join(new_string)

        if len(new_string) > 0:
            list_strings.insert(start_index, new_string)

    elif command[0] == "divide":
        index = int(command[1])
        partitions_count = int(command[2])

        if partitions_count == 0:
            continue

        string_to_divide = list_strings.pop(index)

        if partitions_count > len(string_to_divide):
            partitions_count = len(string_to_divide)

        partitions_length = len(string_to_divide) // partitions_count
        number_of_remaining_characters = len(string_to_divide) % partitions_count

        string_divided = []
        for i in range(0, len(string_to_divide) - number_of_remaining_characters, partitions_length):
            partition = string_to_divide[i:i + partitions_length]
            string_divided.append(partition)

        if len(string_to_divide) % partitions_count != 0:
            remaining_characters = string_to_divide[(len(string_to_divide)-number_of_remaining_characters):]
            string_divided[-1] += remaining_characters

        for i in range(len(string_divided)):
            list_strings.insert(index + i, string_divided[i])

print(" ".join(list_strings))
