def multiplication_result(some_list: list) -> str:
    negatives = 0

    for item in some_list:
        if item < 0:
            negatives += 1
        elif item == 0:
            return "zero"

    if negatives % 2 == 0:
        return "positive"
    return "negative"


list_numbers = [int(input()), int(input()), int(input())]
print(multiplication_result(list_numbers))
