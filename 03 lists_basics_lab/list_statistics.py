number_of_lines = int(input())

list_positives = []
list_negatives = list()

for _ in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        list_positives.append(current_number)
    else:
        list_negatives.append(current_number)

print(list_positives)
print(list_negatives)
print('Count of positives:', len(list_positives))
print('Sum of negatives:', sum(list_negatives))
