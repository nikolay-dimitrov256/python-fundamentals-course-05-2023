counter = int(input())

synonym_dict = {}

for _ in range(counter):
    word, synonym = input(), input()

    if word not in synonym_dict:
        synonym_dict[word] = [synonym]
    else:
        synonym_dict[word].append(synonym)

for words, synonyms in synonym_dict.items():
    print(f"{words} - {', '.join(synonyms)}")
