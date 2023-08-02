def check_palindrome():
    palindrome_words = [word for word in input().split() if word == word[::-1]]
    key_word = input()
    palindrome_counter = 0

    for item in palindrome_words:
        if key_word in item:
            palindrome_counter += 1

    return f"{palindrome_words}\nFound palindrome {palindrome_counter} times"


print(check_palindrome())
