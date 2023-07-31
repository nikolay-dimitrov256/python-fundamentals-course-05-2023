n = int(input())
secret_word = input()

list_of_strings = []
filtered_list = []

for _ in range(n):
    current_word = input()
    list_of_strings.append(current_word)

print(list_of_strings)

for item in list_of_strings:
    if secret_word in item:
        filtered_list.append(item)

print(filtered_list)
