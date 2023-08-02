coffees_needed = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffees_needed += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffees_needed += 2

if coffees_needed <= 5:
    print(coffees_needed)
else:
    print("You need extra sleep")
