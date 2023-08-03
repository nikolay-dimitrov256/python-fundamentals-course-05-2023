import re

text = input()

pattern = r'<title>(.*)</title>.*<body>(.*)</body>'

matches = re.search(pattern, text)
title = matches.group(1)
content = ''
flag = False

for ch in matches.group(2):
    if ch == '<':
        flag = True
    elif ch == '>':
        flag = False
        continue

    if not flag:
        content += ch

while '\\n' in content:
    content = content.replace('\\n', '')

print(f'Title: {title}')
print(f'Content: {content}')
