# tail, body, head = input(), input(), input()
#
# body_parts = list()
#
# body_parts.append(head)
# body_parts.append(body)
# body_parts.append(tail)
#
# print(body_parts)

tail, body, head = input(), input(), input()

body_parts = [tail, body, head]
body_parts[0], body_parts[2] = body_parts[2], body_parts[0]

print(body_parts)
