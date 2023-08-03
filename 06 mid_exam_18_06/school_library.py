def add_book(books_list: list, title: str) -> list:
    if title not in books_list:
        books_list.insert(0, title)

    return books_list


def take_book(books_list: list, title: str) -> list:
    if title in books_list:
        books_list.remove(title)

    return books_list


def swap_books(books_list: list, first_title: str, second_title: str) -> list:
    if first_title in books_list and second_title in books_list:
        first_index = books_list.index(first_title)
        second_index = books_list.index(second_title)
        books_list[first_index], books_list[second_index] = books_list[second_index], books_list[first_index]

    return books_list


def insert_book(books_list: list, title: str) -> list:
    if title not in books_list:
        books_list.append(title)

    return books_list


def check_book(books_list: list, index: int):
    if index in range(len(books_list)):
        print(books_list[index])


book_shelf = input().split("&")

while True:
    command = input()
    if command == "Done":
        break

    command = command.split(" | ")

    if command[0] == "Add Book":
        book_title = command[1]
        book_shelf = add_book(book_shelf, book_title)

    elif command[0] == "Take Book":
        book_title = command[1]
        book_shelf = take_book(book_shelf, book_title)

    elif command[0] == "Swap Books":
        title_one = command[1]
        title_two = command[2]
        book_shelf = swap_books(book_shelf, title_one, title_two)

    elif command[0] == "Insert Book":
        book_title = command[1]
        book_shelf = insert_book(book_shelf, book_title)

    elif command[0] == "Check Book":
        book_index = int(command[1])
        check_book(book_shelf, book_index)

print(", ".join(book_shelf))

