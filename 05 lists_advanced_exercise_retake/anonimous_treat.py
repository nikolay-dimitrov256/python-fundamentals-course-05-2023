def divide_string(words: list, params: list) -> list:
    index = int(params[0])
    partitions_count = int(params[1])
    if partitions_count == 0:
        return words

    word_to_partition = words.pop(index)

    if partitions_count > len(word_to_partition):
        partitions_count = len(word_to_partition)

    partitions_length = len(word_to_partition) // partitions_count
    last_chars = len(word_to_partition) % partitions_count
    partitions = []

    for i in range(0, len(word_to_partition) - last_chars, partitions_length):
        partition = word_to_partition[i:i+partitions_length]
        partitions.append(partition)

    if last_chars:
        partitions[-1] += word_to_partition[len(word_to_partition)-last_chars:]

    for i in range(len(partitions)):
        words.insert(index+i, partitions[i])

    return words


def merge_strings(words: list, params: list) -> list:
    start_index = int(params[0])
    end_index = int(params[1])

    if start_index < 0:
        start_index = 0
    if end_index >= len(words):
        end_index = len(words) - 1

    if start_index in range(len(words)) and end_index in range(len(words)):
        word = ''
        for i in range(start_index, end_index + 1):
            word += words[i]

        words = words[:start_index] + words[end_index+1:]
        words.insert(start_index, word)

    return words


def modify_data(words: list) -> list:
    while True:
        command, *params = input().split()
        if command == '3:1':
            return words

        if command == 'merge':
            words = merge_strings(words, params)

        elif command == 'divide':
            words = divide_string(words, params)


data = input().split()

print(' '.join(modify_data(data)))
