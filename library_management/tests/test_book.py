import pytest

from book import Book
from exceptions import InvalidInputError


def test_create_book():
    book = Book("B101", "Python Basics", "Guido")

    assert book.book_id == "B101"
    assert book.title == "Python Basics"
    assert book.author == "Guido"
    assert book.available is True


def test_book_to_dict():
    book = Book("B102", "Python OOP", "James")

    result = book.to_dict()

    assert result == {
        "book_id": "B102",
        "title": "Python OOP",
        "author": "James",
        "available": True,
    }


def test_book_rejects_empty_title():
    with pytest.raises(ValueError):
        Book("B103", "   ", "Guido")


def test_duplicate_book_id_is_rejected(tmp_path, monkeypatch):
    import book as book_module

    data_file = tmp_path / "books.json"

    def fake_load_data(filename):
        return []

    def fake_save_data(filename, records):
        pass

    monkeypatch.setattr(book_module, "load_data", fake_load_data)
    monkeypatch.setattr(book_module, "save_data", fake_save_data)

    manager = book_module.BookManager()
    manager.add_book(Book("B104", "Python", "Guido"))

    with pytest.raises(InvalidInputError):
        manager.add_book(Book("B104", "Python Advanced", "Guido"))