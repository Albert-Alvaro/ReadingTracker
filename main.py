"""
Name: Albert Alvaro
Date: 15 January 2023
Brief Project Description: A program that can be used to track the progress of someone's reading
GitHub URL: https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-2-Albert-Alvaro
"""
# Create your main program in this file, using the ReadingTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from book import Book
from operator import attrgetter
from bookcollection import BookCollection

COMPLETED = "c"
REQUIRED = "r"
MENU = """Menu:
L - List all books
A - Add new book
M - Mark a book as completed 
Q - Quit"""
book_dictionary = {}
SPINNER_OPTIONS_TO_KEYWORD = {'Title': 'title', 'Author': 'author', 'Pages': 'page_number', 'Required': 'is_required'}


class ReadingTrackerApp(App):
    status_text = StringProperty()
    by_sort = ListProperty()
    current_by_sort = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.books = BookCollection().load_books("books.csv")

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Book Tracker"
        self.by_sort = sorted(SPINNER_OPTIONS_TO_KEYWORD.keys())
        self.current_by_sort = self.by_sort[0]
        self.root = Builder.load_file('app.kv')
        self.books.sort(key=attrgetter('author'))
        self.create_widgets()
        return self.root

    def press_add(self, added_title, added_author, added_pages):
        try:
            if added_title == "" or added_author == "" or added_pages == "":
                self.status_text = f"All fields must be completed"
                self.clear_fields()
            elif int(added_pages) < 0:
                self.status_text = f"Pages must be > 0"
                self.clear_fields()
            elif not added_pages.isdigit():
                self.status_text = f"Please enter a valid number"
                self.clear_fields()
            else:
                new_book = Book(added_title, added_author, int(added_pages), REQUIRED)
                self.books.append(new_book)
                self.clear_fields()
                self.root.ids.entries_box.clear_widgets()
                self.status_text = f"{new_book.title} by {new_book.author} has been added"
                self.books.sort(key=attrgetter(SPINNER_OPTIONS_TO_KEYWORD[self.current_by_sort]))
                self.create_widgets()
        except ValueError:
            self.status_text = f"Please enter a valid number"
            self.clear_fields()

    def create_widgets(self):
        for book in self.books:
            temp_button = Button(text=str(book))
            temp_button.bind(on_release=self.press_book)
            temp_button.book = book
            if book.is_required == "r":
                temp_button.background_color = [0, 0.9, 1, 1]
            else:
                temp_button.background_color = [1, 1, 1, 1]
            self.root.ids.entries_box.add_widget(temp_button)

    def press_book(self, instance):
        book = instance.book
        additional_statuses = ['Good job!', 'Get started!']
        if book.is_required == "c":
            book.is_required = "r"
            if book.is_long():
                add = additional_statuses[1]
                status = f"You need to read {book.title}.{add}"
            else:
                status = f"You need to read {book.title}."
        else:
            book.is_required = "c"
            if book.is_long():
                add = additional_statuses[0]
                status = f"You completed {book.title}.{add}"
            else:
                status = f"You completed {book.title}."
        self.root.ids.entries_box.clear_widgets()
        self.status_text = f"{status}"
        self.create_widgets()

    def clear_fields(self):
        self.root.ids.added_title.text = ""
        self.root.ids.added_author.text = ""
        self.root.ids.added_pages.text = ""

    def change_spinner_selection(self, new_sort_selection):
        self.current_by_sort = new_sort_selection
        self.update_selection()

    def update_selection(self):
        self.books.sort(key=attrgetter(SPINNER_OPTIONS_TO_KEYWORD[self.current_by_sort]))
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()


if __name__ == '__main__':
    ReadingTrackerApp().run()
