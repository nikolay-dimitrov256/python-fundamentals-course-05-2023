current_year = int(input())

while True:
    current_year += 1
    string_year = str(current_year)
    if len(set(string_year)) == len(str(current_year)):
        print(current_year)
        break
