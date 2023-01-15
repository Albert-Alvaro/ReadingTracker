"""
Name: Albert Alvaro
Date started: 23 December 2022
GitHub URL: https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-1-Albert-Alvaro

Time estimate : 1 Hour
Time taken : 2 Hours
"""
from book import Book
from bookcollection import BookCollection
COMPLETED = "c"
REQUIRED = "r"
MENU = """Menu:
L - List all books
A - Add new book
M - Mark a book as completed 
Q - Quit"""
book_dictionary = {}


def main():
    books = BookCollection().load_books("books.csv")
    """..."""
    print("Reading Tracker 1.0 - by Albert Alvaro")
    print(f"{len(books)} books loaded")
    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            books_to_read = 0
            title_lengths = [book.title for book in books]
            author_lengths = [book.author for book in books]
            title_alignment = len(max(title_lengths, key=len))
            author_alignment = len(max(author_lengths, key=len))
            for i in range(0, len(books)):
                if books[i].is_required == REQUIRED:
                    books_to_read += 1
                    is_required = "*"
                    number_alignment = 0
                else:
                    is_required = ""
                    number_alignment = 2
                print(f"{is_required}{i + 1: >{number_alignment}}. {books[i].title: <{title_alignment+1}} by {books[i].author: <{author_alignment+1}} {books[i].page_number} pages")
            print(f"You need to read {BookCollection().get_required_pages(books)} pages in {books_to_read} books.")
        elif choice == "A":
            book_name = validate_string("Title: ")
            book_author = validate_string("Author: ")
            book_pages = validate_int("Pages: ")
            new_book = Book(book_name, book_author, book_pages, "r")
            BookCollection().add_book(new_book)

            print(f"{new_book.title} by {new_book.author}, ({new_book.page_number}) added to Reading Tracker")
        elif choice == "M":
            required_books = [book for book in books if book.is_required == REQUIRED]
            if not required_books:
                print("No required books")
            else:
                books_to_read = 0
                title_lengths = [book.title for book in books]
                author_lengths = [book.author for book in books]
                title_alignment = len(max(title_lengths, key=len))
                author_alignment = len(max(author_lengths, key=len))
                for i in range(0, len(books)):
                    book_dictionary[i + 1] = books[i]
                    if books[i].is_required == REQUIRED:
                        books_to_read += 1
                        is_required = "*"
                        number_alignment = 0
                    else:
                        is_required = ""
                        number_alignment = 2
                    print(
                        f"{is_required}{i + 1: >{number_alignment}}. {books[i].title: <{title_alignment + 1}} by {books[i].author: <{author_alignment + 1}} {books[i].page_number} pages")
                print(f"You need to read {BookCollection().get_required_pages(books)} pages in {books_to_read} books.")
                print("Enter the number of a book to mark as completed")
                book_choice = validate_book_number(">>>", books)
                books[book_choice-1].is_required = COMPLETED
                print(f"{book_dictionary[book_choice].title} by {book_dictionary[book_choice].author} completed!")
        else:
            print("Invalid Choice")
        choice = get_choice()
    autosave(books)
    print(f"{len(books)} books saved to books.csv")
    print("So many books, so little time. Frank Zappa")


def autosave(books):
    """This function will save the books added or modified to the pre-determined file"""
    output_file = open("books.csv", "w")
    for book in books:
        print(f"{book.title},{book.auhtor},{book.page_number},{book.is_required}", file=output_file)
    output_file.close()


def validate_int(prompt):
    """
    This function is to validate an integer that is inputted, such that the integer is not below zero and is an integer
    """
    try:
        page = int(input(prompt))
        while page < 0:
            print("Number must be > 0")
            page = int(input(prompt))
    except ValueError:
        print("Invalid input; enter a valid number")
        page = int(input(prompt))
    return page


def validate_book_number(prompt, books):
    """This function is for validating the book number that is inputted"""
    try:
        number = int(input(prompt))
        while number < 0:
            print("Number must be > 0")
            number = int(input(prompt))
        while number not in book_dictionary:
            print("Invalid book number")
            number = int(input(prompt))
        while books[number-1].is_required == COMPLETED:
            print("That book is already completed")
            number = int(input(prompt))
    except ValueError:
        print("Invalid input; enter a valid number")
        number = int(input(prompt))
    return number


def validate_string(prompt):
    """This function is for validating the string inputted"""
    name = input(prompt).title()
    while name == "":
        print("Input cannot be blank")
        name = input(prompt).title()
    return name


def extract_data(data, books):
    """This function is for extracting the data from the csv file"""
    for line in data:
        items = line.strip().split(",")
        books.append(items)


def get_choice():
    """This function is for getting the user's menu choice"""
    print(MENU, end="\n")
    choice = input(">>>").upper()
    return choice


main()


