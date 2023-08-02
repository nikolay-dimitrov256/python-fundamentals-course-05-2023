list_numbers = input().split(", ")

positives = ", ".join([num for num in list_numbers if int(num) >= 0])
negatives = ", ".join([num for num in list_numbers if int(num) < 0])
evens = ", ".join([num for num in list_numbers if int(num) % 2 == 0])
odds = ", ".join([num for num in list_numbers if int(num) % 2 != 0])

print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {evens}")
print(f"Odd: {odds}")
