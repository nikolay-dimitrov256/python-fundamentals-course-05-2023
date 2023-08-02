import re

pattern = '(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)'
#pattern = "(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)"
valid_urls = []

while True:
    command = input()
    if command == '':
        break

    matches = re.search(pattern, command)
    if matches:
        valid_urls.append(matches.group(1))

for url in valid_urls:
    print(url)
