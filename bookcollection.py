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
        with open(file_name, "r", encoding="utf-8-sig") as in_file:
            data = in_file.readlines()
            for line in data:
                items = line.strip().split(",")
                self.books.append(Book(items[0], items[1], items[2], items[3]))
            return self.books

    def save_file(self, file, book_list):
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(book_list)
        print("Your file has been updated and saved!")

    def add_book(self, book):
        self.books.append(book)

    def get_required_pages(self, book_list):
        for book in book_list:
            if book.is_required == "r":
                self.required_pages += int(book.page_number)
        return self.required_pages

    def sort(self, keyword):
        return self.books.sort(key=attrgetter(keyword))



