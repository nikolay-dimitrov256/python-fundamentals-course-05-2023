characters_count = int(input())

sum_characters = 0

for character in range(characters_count):
    current_character = input()
    sum_characters += ord(current_character)

print(f"The sum equals: {sum_characters}")
