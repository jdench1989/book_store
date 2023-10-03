from lib.book import Book

"""
Book class constructs correctly with attributes for
each item on books table
"""
def test_constructs_correctly():
    book = Book(1, "Test title", "Test author")
    assert book.id == 1
    assert book.title == "Test title"
    assert book.author_name == "Test author"

"""
We can compare two identical book instances
and have them be equal for testing purposes
"""
def test_identical_equality():
    book1 = Book(1, "Test title", "Test author")
    book2 = Book(1, "Test title", "Test author")
    assert book1 == book2

"""
We can format book object attributes into a string for printing
"""
def test_string_formatting():
    book1 = Book(1, "Test title", "Test author")
    assert str(book1) == "Book(1, Test title, Test author)"