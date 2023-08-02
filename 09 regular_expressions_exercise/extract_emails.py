import re

text = input()
pattern = r'\s(([a-z\d][a-z\d\.\-_]*)@([a-z][a-z\-]*)(\.[a-z]+)+)\b'

matches = re.findall(pattern, text)

for match in matches:
    print(match[0])
