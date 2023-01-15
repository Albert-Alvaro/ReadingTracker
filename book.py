"""..."""


# Create your Book class in this file


class Book:
    """..."""
    def __init__(self, title="", author="", page_number=0, is_required=""):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.is_required = is_required

    def __str__(self):
        return f"{self.title} by {self.author} {self.page_number} pages"

    def mark_required(self):
        if self.is_required == "r":
            return True

    def mark_complete(self):
        if self.is_required == "c":
            return False

    def is_long(self):
        if self.page_number >= 500:
            return "Long"
