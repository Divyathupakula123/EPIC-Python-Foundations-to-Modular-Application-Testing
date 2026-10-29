"""OOP coding challenges with clean Python coding practices."""

from abc import ABC, abstractmethod


# 1. Student Class
class Student:
    """Store student information and marks."""

    def __init__(self, name: str, marks: float) -> None:
        """Initialize a student."""
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.name = name
        self.marks = marks

    def display(self) -> None:
        """Display student information."""
        print(f"Student: {self.name}, Marks: {self.marks}")


# 2. Bank Account Class
class BankAccount:
    """Manage a bank account securely."""

    def __init__(
        self, account_holder: str, balance: float = 0
    ) -> None:
        """Initialize a bank account."""
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit a positive amount."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money if sufficient funds are available."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.__balance


# 3. Employee Management
class Employee:
    """Represent an employee."""

    def __init__(
        self, employee_id: int, name: str, salary: float
    ) -> None:
        """Initialize employee details."""
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self) -> None:
        """Display employee details."""
        print(
            f"ID: {self.employee_id}, Name: {self.name}, "
            f"Salary: {self.salary}"
        )


class EmployeeManagement:
    """Manage a collection of employees."""

    def __init__(self) -> None:
        """Create an empty employee collection."""
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee if the ID is not already present."""
        for existing in self.employees:
            if existing.employee_id == employee.employee_id:
                raise ValueError("Employee ID already exists.")

        self.employees.append(employee)

    def display_all(self) -> None:
        """Display all employees."""
        for employee in self.employees:
            employee.display()


# 4. Vehicle Inheritance
class Vehicle:
    """Represent a general vehicle."""

    def start(self) -> str:
        """Return the vehicle starting message."""
        return "Vehicle is starting"


class Car(Vehicle):
    """Represent a car."""

    def start(self) -> str:
        """Return the car starting message."""
        return "Car is starting"


class Bike(Vehicle):
    """Represent a bike."""

    def start(self) -> str:
        """Return the bike starting message."""
        return "Bike is starting"


# 5. Shape Area Calculator
class Shape(ABC):
    """Define the interface for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the shape's area."""
        raise NotImplementedError


class Rectangle(Shape):
    """Calculate the area of a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        """Initialize rectangle dimensions."""
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive.")

        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the rectangle's area."""
        return self.length * self.width


class Circle(Shape):
    """Calculate the area of a circle."""

    def __init__(self, radius: float) -> None:
        """Initialize the circle radius."""
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self.radius = radius

    def area(self) -> float:
        """Return the circle's area."""
        return 3.14159 * self.radius ** 2


# 6. Shopping Cart
class ShoppingCart:
    """Manage shopping items and calculate their total cost."""

    def __init__(self) -> None:
        """Create an empty shopping cart."""
        self.items: dict[str, tuple[float, int]] = {}

    def add_item(
        self, name: str, price: float, quantity: int = 1
    ) -> None:
        """Add an item or increase its quantity."""
        if not name.strip():
            raise ValueError("Item name cannot be empty.")

        if price < 0 or quantity <= 0:
            raise ValueError("Invalid price or quantity.")

        if name in self.items:
            old_price, old_quantity = self.items[name]

            if old_price != price:
                raise ValueError("Item price does not match.")

            self.items[name] = (
                old_price, old_quantity + quantity
            )
        else:
            self.items[name] = (price, quantity)

    def total_price(self) -> float:
        """Calculate the total shopping cost."""
        return sum(
            price * quantity
            for price, quantity in self.items.values()
        )

    def display(self) -> None:
        """Display cart items and total cost."""
        for name, (price, quantity) in self.items.items():
            print(f"{name}: {quantity} x {price}")

        print(f"Total: {self.total_price():.2f}")


# 7. Movie Rating System
class Movie:
    """Store movie ratings and calculate their average."""

    def __init__(self, title: str) -> None:
        """Initialize a movie."""
        self.title = title
        self.ratings: list[int] = []

    def add_rating(self, rating: int) -> None:
        """Add a rating between 1 and 5."""
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")

        self.ratings.append(rating)

    def average_rating(self) -> float:
        """Return the average rating or zero if unrated."""
        if not self.ratings:
            return 0.0

        return sum(self.ratings) / len(self.ratings)


# 8. Hospital Patient Records
class Patient:
    """Store basic patient information."""

    def __init__(
        self, patient_id: int, name: str, illness: str
    ) -> None:
        """Initialize patient details."""
        self.patient_id = patient_id
        self.name = name
        self.illness = illness

    def display(self) -> None:
        """Display patient information."""
        print(
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.name}, Illness: {self.illness}"
        )


class Hospital:
    """Manage hospital patient records."""

    def __init__(self) -> None:
        """Create an empty patient collection."""
        self.patients: list[Patient] = []

    def add_patient(self, patient: Patient) -> None:
        """Add a patient with a unique patient ID."""
        for existing in self.patients:
            if existing.patient_id == patient.patient_id:
                raise ValueError("Patient ID already exists.")

        self.patients.append(patient)

    def display_patients(self) -> None:
        """Display all patient records."""
        for patient in self.patients:
            patient.display()


# 9. School Result Processing
class SchoolResult:
    """Calculate a student's result from subject marks."""

    def __init__(
        self, student_name: str, marks: list[float]
    ) -> None:
        """Initialize the student's marks."""
        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks must be between 0 and 100.")

        self.student_name = student_name
        self.marks = marks.copy()

    def total_marks(self) -> float:
        """Return the sum of all subject marks."""
        return sum(self.marks)

    def average_marks(self) -> float:
        """Return the average marks."""
        if not self.marks:
            return 0.0

        return self.total_marks() / len(self.marks)

    def result(self) -> str:
        """Return Pass or Fail using a 35-mark pass threshold."""
        if not self.marks:
            return "No marks available"

        if all(mark >= 35 for mark in self.marks):
            return "Pass"

        return "Fail"


# 10. Online Course Management
class Course:
    """Manage course enrollment."""

    def __init__(self, course_name: str) -> None:
        """Initialize a course."""
        self.course_name = course_name
        self.students: list[str] = []

    def enroll(self, student_name: str) -> None:
        """Enroll a student if not already enrolled."""
        if not student_name.strip():
            raise ValueError("Student name cannot be empty.")

        if student_name not in self.students:
            self.students.append(student_name)

    def display_students(self) -> None:
        """Display the course and enrolled students."""
        print(f"Course: {self.course_name}")
        print(f"Enrolled students: {self.students}")


def main() -> None:
    """Run demonstrations of all ten coding challenges."""

    try:
        print("\n1. Student Class")
        student = Student("Divya", 90)
        student.display()

        print("\n2. Bank Account")
        account = BankAccount("Divya", 1000)
        account.deposit(500)
        account.withdraw(200)
        print(f"Balance: {account.get_balance()}")

        print("\n3. Employee Management")
        manager = EmployeeManagement()
        manager.add_employee(Employee(101, "Ravi", 25000))
        manager.add_employee(Employee(102, "Priya", 30000))
        manager.display_all()

        print("\n4. Vehicle Inheritance")
        vehicles: list[Vehicle] = [Car(), Bike()]
        for vehicle in vehicles:
            print(vehicle.start())

        print("\n5. Shape Area Calculator")
        shapes: list[Shape] = [
            Rectangle(5, 4),
            Circle(3),
        ]
        for shape in shapes:
            print(f"Area: {shape.area():.2f}")

        print("\n6. Shopping Cart")
        cart = ShoppingCart()
        cart.add_item("Book", 200, 2)
        cart.add_item("Pen", 10, 3)
        cart.display()

        print("\n7. Movie Rating System")
        movie = Movie("Example Movie")
        movie.add_rating(4)
        movie.add_rating(5)
        print(f"Average rating: {movie.average_rating():.2f}")

        print("\n8. Hospital Patient Records")
        hospital = Hospital()
        hospital.add_patient(Patient(1, "Anu", "Fever"))
        hospital.display_patients()

        print("\n9. School Result Processing")
        result = SchoolResult("Ravi", [80, 75, 90])
        print(f"Total: {result.total_marks()}")
        print(f"Average: {result.average_marks():.2f}")
        print(f"Result: {result.result()}")

        print("\n10. Online Course Management")
        course = Course("Python OOP")
        course.enroll("Divya")
        course.enroll("Ravi")
        course.display_students()

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
