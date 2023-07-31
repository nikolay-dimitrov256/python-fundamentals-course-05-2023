from math import sqrt

number = int(input())

prime = True

for num in range(2, int(sqrt(number)) + 1):
    if number % num == 0:
        prime = False
        break

print(prime)
