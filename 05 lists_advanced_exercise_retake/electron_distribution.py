electrons = int(input())

shells = []
current_shell = 1

while electrons > 0:
    shell_capacity = 2 * current_shell ** 2
    shell_filled = shell_capacity if shell_capacity <= electrons else electrons
    shells.append(shell_filled)
    electrons -= shell_filled
    current_shell += 1

print(shells)
