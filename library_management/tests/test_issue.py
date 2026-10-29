from book import Book, BookManager
from member import Member, MemberManager
from issue import IssueManager
from storage import save_data


def test_issue_and_return_book(tmp_path, monkeypatch):
    import book as book_module
    import member as member_module
    import issue as issue_module

    def fake_load_data(filename):
        return []

    def fake_save_data(filename, records):
        pass

    monkeypatch.setattr(book_module, "load_data", fake_load_data)
    monkeypatch.setattr(book_module, "save_data", fake_save_data)
    monkeypatch.setattr(member_module, "load_data", fake_load_data)
    monkeypatch.setattr(member_module, "save_data", fake_save_data)
    monkeypatch.setattr(issue_module, "load_data", fake_load_data)
    monkeypatch.setattr(issue_module, "save_data", fake_save_data)

    books = BookManager()
    members = MemberManager()

    books.add_book(Book("B201", "Python Basics", "Guido"))
    members.register_member(Member("M201", "Divya"))

    issues = IssueManager(books, members)

    record = issues.issue_book("B201", "M201")

    assert record["book_id"] == "B201"
    assert record["member_id"] == "M201"
    assert books.search_book("B201")["available"] is False

    returned = issues.return_book("B201")

    assert returned["return_date"] is not None
    assert returned["fine"] == 0.0
    assert books.search_book("B201")["available"] is True