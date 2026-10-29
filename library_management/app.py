from book import Book, BookManager
from member import Member, MemberManager
from issue import IssueManager
from reports import ReportManager
from exceptions import LibraryError


def main() -> None:
    """Run the Library Management System."""
    book_manager = BookManager()
    member_manager = MemberManager()

    issue_manager = IssueManager(book_manager, member_manager)
    report_manager = ReportManager(book_manager, issue_manager)

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Register Member")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Reports")
        print("7. Update Book")
        print("8. Delete Book")
        print("9. Update Member")
        print("10. Delete Member")
        print("11. Fine Report")
        print("12. Search Book")
        print("13. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                book_id = input("Book ID: ")
                title = input("Book title: ")
                author = input("Author: ")

                book = Book(book_id, title, author)
                book_manager.add_book(book)
                print("Book added successfully!")

            elif choice == "2":
                books = book_manager.list_books()

                if not books:
                    print("No books found.")
                else:
                    for book in books:
                        status = (
                            "Available"
                            if book["available"]
                            else "Borrowed"
                        )
                        print(
                            f'{book["book_id"]}: {book["title"]} '
                            f'by {book["author"]} - {status}'
                        )

            elif choice == "3":
                member_id = input("Member ID: ")
                name = input("Member name: ")

                member = Member(member_id, name)
                member_manager.register_member(member)
                print("Member registered successfully!")

            elif choice == "4":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")

                issue_manager.issue_book(book_id, member_id)
                print("Book issued successfully!")

            elif choice == "5":
                book_id = input("Book ID: ")

                record = issue_manager.return_book(book_id)
                print("Book returned successfully!")
                print(f'Fine: Rs. {record["fine"]:.2f}')

            elif choice == "6":
                print("\nAvailable books:")
                available = report_manager.available_books()

                if not available:
                    print("No available books.")

                for book in available:
                    print(f'{book["book_id"]}: {book["title"]}')

                print("\nBorrowed books:")
                borrowed = report_manager.borrowed_books()

                if not borrowed:
                    print("No borrowed books.")

                for book in borrowed:
                    print(f'{book["book_id"]}: {book["title"]}')

                print("\nTop borrowers:")
                for member in report_manager.top_borrowers():
                    print(
                        f'Member {member["member_id"]}: '
                        f'{member["books_borrowed"]} borrowings'
                    )

                print(
                    f'\nTotal recorded fines: '
                    f'Rs. {report_manager.total_fines():.2f}'
                )

            elif choice == "7":
                book_id = input("Book ID to update: ")
                title = input("New title: ")
                author = input("New author: ")

                book_manager.update_book(book_id, title, author)
                print("Book updated successfully!")

            elif choice == "8":
                book_id = input("Book ID to delete: ")

                book_manager.delete_book(book_id)
                print("Book deleted successfully!")

            elif choice == "9":
                member_id = input("Member ID to update: ")
                name = input("New member name: ")

                member_manager.update_member(member_id, name)
                print("Member updated successfully!")

            elif choice == "10":
                member_id = input("Member ID to delete: ")

                member_manager.delete_member(member_id)
                print("Member deleted successfully!")

            elif choice == "11":
                fine_records = report_manager.fine_report()

                if not fine_records:
                    print("No fines recorded.")
                else:
                    print("\nFine Report:")
                    for record in fine_records:
                        print(
                            f'Book: {record["book_id"]}, '
                            f'Member: {record["member_id"]}, '
                            f'Fine: Rs. {record["fine"]:.2f}'
                        )

                print(
                    f'Total fines: Rs. '
                    f'{report_manager.total_fines():.2f}'
                )

            elif choice == "12":
                book_id = input("Enter Book ID to search: ")
                book = book_manager.search_book(book_id)

                status = (
                    "Available"
                    if book["available"]
                    else "Borrowed"
                )

                print(f'Book ID: {book["book_id"]}')
                print(f'Title: {book["title"]}')
                print(f'Author: {book["author"]}')
                print(f'Status: {status}')

            elif choice == "13":
                print("Thank you for using the Library Management System!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 13.")

        except LibraryError as error:
            print(f"Library error: {error}")

        except (ValueError, KeyError, TypeError) as error:
            print(f"Input or data error: {error}")

        except OSError as error:
            print(f"File operation error: {error}")


if __name__ == "__main__":
    main()