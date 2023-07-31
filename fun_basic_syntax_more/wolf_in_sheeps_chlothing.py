list_animals = input().split(", ")

for i in range(-1, -len(list_animals) -1, -1):
    if list_animals[i] == "wolf":
        if i == -1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {abs(i + 1)}! You are about to be eaten by a wolf!")
        break
