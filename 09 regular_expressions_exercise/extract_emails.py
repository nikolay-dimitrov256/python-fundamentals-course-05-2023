import re

text = input()
pattern = r'\s(([a-z\d][a-z\d\.\-_]*)@([a-z][a-z\-]*)(\.[a-z]+)+)\b'
# pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

matches = re.findall(pattern, text)

for match in matches:
    print(match[0])
