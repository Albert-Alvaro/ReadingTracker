"""..."""
from operator import attrgetter

from book import Book
import csv
import operator

# Create your BookCollection class in this file


class BookCollection:
    """..."""
    def __init__(self, books=[], required_pages=0):
        self.books = books
        self.required_pages = required_pages

    def load_books(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8-sig") as in_file:
                data = in_file.readlines()
                for line in data:
                    items = line.strip().split(",")
                    self.books.append(Book(items[0], items[1], items[2], items[3]))
                return self.books
        except FileNotFoundError:
            self.books = []
            return self.books

    def save_file(self, file, book_list):
        output_file = open(file, "w")
        for book in book_list:
            print(f"{book.title},{book.author},{book.page_number},{book.is_required}", file=output_file)
        output_file.close()

    def add_book(self, book):
        self.books.append(book)

    def get_required_pages(self, book_list):
        for book in book_list:
            if book.is_required == "r":
                self.required_pages += int(book.page_number)
        return self.required_pages

    def sort(self, keyword):
        return self.books.sort(key=attrgetter(keyword))



