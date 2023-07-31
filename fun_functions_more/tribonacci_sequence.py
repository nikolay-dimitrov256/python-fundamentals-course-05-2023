def tribonacci_sequece(counter: int) -> str:
    list_sequence = [1, 1, 2]
    a = 1
    b = 1
    c = 2

    for _ in range(counter - 3):
        a, b, c = b, c, a + b + c
        list_sequence.append(c)

    list_sequence = list(map(str, list_sequence))
    required_list = []
    for i in range(counter):
        required_list.append(list_sequence[i])

    return " ".join(required_list)


some_counter = int(input())
print(tribonacci_sequece(some_counter))
