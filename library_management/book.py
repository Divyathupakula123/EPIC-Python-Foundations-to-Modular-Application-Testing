from typing import Any

from exceptions import BookNotFoundError, InvalidInputError
from storage import load_data, save_data
from validator import validate_text


class Book:
    """Represent a book in the library."""

    def __init__(
        self,
        book_id: str,
        title: str,
        author: str,
        available: bool = True,
    ) -> None:
        """Initialize a book."""
        self.book_id = validate_text(book_id, "Book ID")
        self.title = validate_text(title, "Title")
        self.author = validate_text(author, "Author")
        self.available = available

    def to_dict(self) -> dict[str, Any]:
        """Convert book details to a dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available,
        }


class BookManager:
    """Manage library book records."""

    FILE_NAME = "books.json"

    def __init__(self) -> None:
        """Load book records."""
        self.books = load_data(self.FILE_NAME)

    def add_book(self, book: Book) -> None:
        """Add a new book."""
        if any(item["book_id"] == book.book_id for item in self.books):
            raise InvalidInputError("Book ID already exists.")

        self.books.append(book.to_dict())
        save_data(self.FILE_NAME, self.books)

    def search_book(self, book_id: str) -> dict[str, Any]:
        """Search for a book using its ID."""
        book_id = validate_text(book_id, "Book ID")

        for book in self.books:
            if book["book_id"] == book_id:
                return book

        raise BookNotFoundError(f"Book {book_id} was not found.")

    def update_book(
        self, book_id: str, title: str, author: str
    ) -> None:
        """Update a book's title and author."""
        book = self.search_book(book_id)
        book["title"] = validate_text(title, "Title")
        book["author"] = validate_text(author, "Author")
        save_data(self.FILE_NAME, self.books)

    def delete_book(self, book_id: str) -> None:
        """Delete a book using its ID."""
        book = self.search_book(book_id)

        if not book["available"]:
            raise InvalidInputError("Cannot delete a borrowed book.")

        self.books.remove(book)
        save_data(self.FILE_NAME, self.books)

    def list_books(self) -> list[dict[str, Any]]:
        """Return all books."""
        return self.books