is_even = lambda x: x % 2 == 0

list_numbers = list(map(int, input().split()))
even_list = list(filter(is_even, list_numbers))

print(even_list)
