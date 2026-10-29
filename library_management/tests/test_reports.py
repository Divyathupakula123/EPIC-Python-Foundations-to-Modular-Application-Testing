from reports import ReportManager


class FakeBookManager:
    def list_books(self):
        return [
            {
                "book_id": "B101",
                "title": "Python Basics",
                "available": True,
            },
            {
                "book_id": "B102",
                "title": "Python OOP",
                "available": False,
            },
        ]


class FakeIssueManager:
    def list_issues(self):
        return [
            {
                "book_id": "B102",
                "member_id": "M101",
                "fine": 10.0,
            },
            {
                "book_id": "B103",
                "member_id": "M101",
                "fine": 5.0,
            },
            {
                "book_id": "B104",
                "member_id": "M102",
                "fine": 0.0,
            },
        ]


def test_available_books():
    report = ReportManager(FakeBookManager(), FakeIssueManager())

    books = report.available_books()

    assert len(books) == 1
    assert books[0]["book_id"] == "B101"


def test_borrowed_books():
    report = ReportManager(FakeBookManager(), FakeIssueManager())

    books = report.borrowed_books()

    assert len(books) == 1
    assert books[0]["book_id"] == "B102"


def test_total_fines():
    report = ReportManager(FakeBookManager(), FakeIssueManager())

    assert report.total_fines() == 15.0


def test_fine_report():
    report = ReportManager(FakeBookManager(), FakeIssueManager())

    fines = report.fine_report()

    assert len(fines) == 2