"""..."""


# Create your Book class in this file


class Book:
    """..."""
    def __init__(self, title="", author="", page_number=0, is_required=""):
        self.title = title.title()
        self.author = author.title()
        self.page_number = int(page_number)
        self.is_required = str(is_required)

    def __str__(self):
        return f"{self.title} by {self.author} {self.page_number} pages"

    def mark_required(self):
        if self.is_required == "r":
            return True

    def mark_complete(self):
        if self.is_required == "c":
            return False

    def is_long(self):
        if int(self.page_number) >= 500:
            return True
        else:
            return False
