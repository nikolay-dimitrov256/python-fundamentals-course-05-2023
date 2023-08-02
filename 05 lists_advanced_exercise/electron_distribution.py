electrons_count = int(input())

atom_shells = []
current_shell = 0

while electrons_count > 0:
    current_shell += 1
    shell_capacity = 2 * current_shell ** 2
    shell_filled = 0

    if shell_capacity <= electrons_count:
        shell_filled = shell_capacity
    else:
        shell_filled = electrons_count

    electrons_count -= shell_filled
    atom_shells.append(shell_filled)

print(atom_shells)
