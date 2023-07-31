a = 0
b = 1
list_numbers = []

for _ in range(10):
    list_numbers.append(a)
    a, b = b, a + b

print(list_numbers)
