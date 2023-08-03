string = input()

final_string = ''
explosion_force = 0

for i in range(len(string)):
    if string[i] == '>':
        explosion_force += int(string[i+1])

    if explosion_force > 0:
        if string[i] == '>':
            final_string += string[i]
        else:
            explosion_force -= 1
    else:
        final_string += string[i]

print(final_string)
