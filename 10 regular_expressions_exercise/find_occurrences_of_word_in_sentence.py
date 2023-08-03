import re

line = input()
key_word = input()

pattern = fr'{key_word}\b'
matches = re.findall(pattern, line, re.IGNORECASE)

print(len(matches))
