from typing import Any


class ReportManager:
    """Generate reports for the library."""

    def __init__(self, book_manager: Any, issue_manager: Any) -> None:
        """Initialize the report manager."""
        self.book_manager = book_manager
        self.issue_manager = issue_manager

    def available_books(self) -> list[dict[str, Any]]:
        """Return all available books."""
        return [
            book
            for book in self.book_manager.list_books()
            if book["available"]
        ]

    def borrowed_books(self) -> list[dict[str, Any]]:
        """Return all currently borrowed books."""
        return [
            book
            for book in self.book_manager.list_books()
            if not book["available"]
        ]

    def top_borrowers(self, limit: int = 3) -> list[dict[str, Any]]:
        """Return members ranked by the number of books borrowed."""
        if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
            raise ValueError("Limit must be a positive integer.")

        counts: dict[str, int] = {}

        for issue in self.issue_manager.list_issues():
            member_id = issue["member_id"]
            counts[member_id] = counts.get(member_id, 0) + 1

        ranked = [
            {"member_id": member_id, "books_borrowed": count}
            for member_id, count in counts.items()
        ]

        return sorted(
            ranked,
            key=lambda item: (-item["books_borrowed"], item["member_id"]),
        )[:limit]

    def fine_report(self) -> list[dict[str, Any]]:
        """Return issue records with fines greater than zero."""
        return [
            issue
            for issue in self.issue_manager.list_issues()
            if issue["fine"] > 0
        ]

    def total_fines(self) -> float:
        """Calculate the total fines recorded by the library."""
        return sum(
            issue["fine"]
            for issue in self.issue_manager.list_issues()
        )