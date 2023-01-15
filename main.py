"""
Name: Albert Alvaro
Date: 15 January 2023
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the ReadingTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from book import Book
from operator import itemgetter, attrgetter
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
        self.create_widgets()
        return self.root

    def press_add(self, added_title, added_author, added_pages):
        try:
            if added_title == "" or added_author == "" or added_pages == "":
                self.root.ids.validation_popup2.open()
                self.clear_fields()
            if not added_pages.isdigit():
                self.root.ids.validation_popup2.open()
                self.clear_fields()
            else:
                new_book = Book(added_title, added_author, added_pages, REQUIRED)
                self.books.append(new_book)
                self.clear_fields()
                self.root.ids.entries_box.clear_widgets()
                self.status_text = f"{new_book.title} by {new_book.author} has been added"
                self.create_widgets()
        except ValueError:
            self.root.ids.validation_popup2.open()
            self.clear_fields()

    def create_widgets(self):
        for book in self.books:
            temp_button = Button(text=str(book))
            temp_button.bind(on_release=self.press_book)
            temp_button.book = book
            if book.is_required == "r":
                # if location is visited, button will now be different color
                temp_button.background_color = [0, 0.9, 1, 1]
            else:
                temp_button.background_color = [1, 1, 1, 1]
            self.root.ids.entries_box.add_widget(temp_button)

    def press_book(self, instance):
        book = instance.book
        if book.is_required == "c":
            book.is_required = "r"
            requirement = 'Required'
        else:
            book.is_required = "c"
            requirement = 'Completed'
        self.root.ids.entries_box.clear_widgets()
        self.status_text = f"{book.title} by {book.author} is now {requirement}"
        self.create_widgets()

    def clear_fields(self):
        self.root.ids.added_title.text = ""
        self.root.ids.added_author.text = ""
        self.root.ids.added_pages.text = ""

    def change_spinner_selection(self, new_sort_selection):
        self.current_by_sort = new_sort_selection
        self.update_selection()

    def update_selection(self):
        keyword = SPINNER_OPTIONS_TO_KEYWORD[self.current_by_sort]
        self.books.sort(key=attrgetter(keyword))
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()


if __name__ == '__main__':
    ReadingTrackerApp().run()
