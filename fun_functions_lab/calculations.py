def calculator(operator, a, b):
    result = 0

    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b

    print(result)


input_operator = input()
first_num = int(input())
second_num = int(input())

calculator(input_operator, first_num, second_num)
