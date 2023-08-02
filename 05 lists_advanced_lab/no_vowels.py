filtered_list = [ch for ch in input() if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(filtered_list))
