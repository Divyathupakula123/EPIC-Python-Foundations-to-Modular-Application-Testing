class LibraryError(Exception):
    """Base exception for library errors."""


class BookNotFoundError(LibraryError):
    """Raised when a book is not found."""


class MemberNotFoundError(LibraryError):
    """Raised when a member is not found."""


class BookNotAvailableError(LibraryError):
    """Raised when a book is unavailable."""


class InvalidInputError(LibraryError):
    """Raised when the input is invalid."""


class InvalidReturnError(LibraryError):
    """Raised when a book return is invalid."""