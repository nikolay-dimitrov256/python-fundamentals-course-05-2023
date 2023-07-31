key_number = int(input())
number_of_lines = int(input())

secret_message = ""

for ch in range(number_of_lines):
    character = input()
    secret_message += chr(ord(character) + key_number)

print(secret_message)
