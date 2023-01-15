"""(Incomplete) Tests for Book class."""
from book import Book


def run_tests():
    """Test Book class."""

    # Test empty book (defaults)
    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.page_number == 0
    assert default_book.is_required == ""

    # Test initial-value book
    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, "r")
    print(new_book)
    # TODO: Write tests to show this initialisation works

    # Test mark_required()
    print(new_book.mark_required())
    # TODO: Write tests to show the mark_required() method works

    # Test is_long()
    print(new_book.is_long())

    # TODO: Write tests to show the is_long() method works

    # TODO: Add more tests, as appropriate


run_tests()
