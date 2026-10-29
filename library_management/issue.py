from datetime import date, timedelta
from typing import Any

from exceptions import (
    BookNotAvailableError,
    BookNotFoundError,
    InvalidInputError,
    InvalidReturnError,
    MemberNotFoundError,
)
from storage import load_data, save_data
from validator import validate_text


class IssueManager:
    """Manage book issues, returns, and fines."""

    FILE_NAME = "issues.json"
    FINE_PER_DAY = 5.0
    LOAN_DAYS = 14

    def __init__(self, book_manager: Any, member_manager: Any) -> None:
        """Initialize the issue manager."""
        self.book_manager = book_manager
        self.member_manager = member_manager
        self.issues = load_data(self.FILE_NAME)

    def issue_book(self, book_id: str, member_id: str) -> dict:
        """Issue an available book to an active member."""
        book_id = validate_text(book_id, "Book ID")
        member_id = validate_text(member_id, "Member ID")

        book = self.book_manager.search_book(book_id)

        if not book["available"]:
            raise BookNotAvailableError("Book is already borrowed.")

        if not self.member_manager.validate_membership(member_id):
            raise InvalidInputError("Member membership is inactive.")

        issue_date = date.today()
        due_date = issue_date + timedelta(days=self.LOAN_DAYS)

        record = {
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": issue_date.isoformat(),
            "due_date": due_date.isoformat(),
            "return_date": None,
            "fine": 0.0,
        }

        book["available"] = False
        self.book_manager.books  # Book records are saved below.
        save_data(self.book_manager.FILE_NAME, self.book_manager.books)

        self.issues.append(record)
        save_data(self.FILE_NAME, self.issues)

        return record

    def return_book(self, book_id: str) -> dict:
        """Return a borrowed book and calculate any late fine."""
        book_id = validate_text(book_id, "Book ID")

        active_issue = next(
            (
                issue
                for issue in reversed(self.issues)
                if issue["book_id"] == book_id
                and issue["return_date"] is None
            ),
            None,
        )

        if active_issue is None:
            raise InvalidReturnError("No active issue found for this book.")

        book = self.book_manager.search_book(book_id)
        return_date = date.today()
        due_date = date.fromisoformat(active_issue["due_date"])
        late_days = max((return_date - due_date).days, 0)
        fine = late_days * self.FINE_PER_DAY

        active_issue["return_date"] = return_date.isoformat()
        active_issue["fine"] = fine
        book["available"] = True

        save_data(self.book_manager.FILE_NAME, self.book_manager.books)
        save_data(self.FILE_NAME, self.issues)

        return active_issue

    def list_issues(self) -> list[dict[str, Any]]:
        """Return all issue records."""
        return self.issues