# Library Management System

## Project Description
The Library Management System is a Python-based application developed using Object-Oriented Programming (OOP). It helps manage books, library members, book issues, returns, and fines.

## Features
- Add, search, update, and delete books.
- Register, search, update, and delete members.
- Validate member membership.
- Issue books to active members.
- Return books and calculate late return fines.
- Generate available books and borrowed books reports.
- Display top borrowers and fine reports.
- Store book, member, and issue records in JSON files.
- Handle errors using custom exceptions.
- Validate user inputs.

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON for data storage

## Project Structure
text
library_management/
├── app.py
├── book.py
├── member.py
├── issue.py
├── reports.py
├── storage.py
├── exceptions.py
├── validator.py
├── README.md
└── data/
    ├── books.json
    ├── members.json
    └── issues.json


## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Navigate to the library_management folder.
4. Run the application:

bash
python app.py


5. Follow the menu instructions.

## Data Storage
The application stores book, member, and issue records in JSON files inside the data folder. Records are loaded when the application starts and saved when changes are made.

## Error Handling
Custom exceptions are used to handle errors such as missing books, missing members, unavailable books, invalid returns, and invalid inputs.

## Testing
The application has been manually tested for adding, updating, and deleting books and members, issuing and returning books, and displaying reports.

## Conclusion
This project demonstrates Python OOP concepts, modular programming, data validation, custom exception handling, JSON file storage, and report generation.