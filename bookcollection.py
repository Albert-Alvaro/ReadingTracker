"""..."""
from book import Book


# Create your BookCollection class in this file


class BookCollection:
    """..."""
    books = []
    required_pages = 0

    def load_books(self, file_name):
        with open(file_name, "r", encoding="utf-8-sig") as in_file:
            data = in_file.readlines()
            for line in data:
                items = line.strip().split(",")
                self.books.append(Book(items[0], items[1], items[2], items[3]))
        return self.books

    def save_books(self, file_name):
        output_file = open(file_name, "w")
        for book in self.books:
            print(f"{book.title},{book.author},{book.page_number},{book.is_required}", file=output_file)
        output_file.close()

    def add_book(self):
        book_name = input("Title: ")
        book_author = input("Author: ")
        book_pages = int(input("Pages: "))
        return Book(book_name, book_author, book_pages, "r")

    def get_required_pages(self, book_list):
        for book in book_list:
            if book.is_required == "r":
                self.required_pages += int(book.page_number)
        return self.required_pages

    def sort(self, other):



