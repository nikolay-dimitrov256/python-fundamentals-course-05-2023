import re

pattern = r'\b_([a-zA-Z\d]+)\b'

line = input()

matches = re.findall(pattern, line)

print(','.join(matches))
