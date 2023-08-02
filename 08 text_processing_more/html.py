article_title = input()
article_content = input()

final_code = f'''
<h1>
    {article_title}
</h1>
<article>
    {article_content}
</article>'''


while True:
    comment = input()
    if comment == "end of comments":
        break

    final_code += f'''
<div>
    {comment}
</div>'''

print(final_code)
