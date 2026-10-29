from abc import ABC, abstractmethod


# 1. Single Responsibility Principle (SRP)
# A class should have only one main responsibility.

class Report:
    def create_report(self):
        return "Report created"


class ReportPrinter:
    def print_report(self, report):
        print(report)


# 2. Open/Closed Principle (OCP)
# New shapes can be added without changing AreaCalculator.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate(self, shape):
        return shape.area()


# 3. Liskov Substitution Principle (LSP)
# A child object should work wherever its parent is expected.

class Bird:
    def eat(self):
        return "Bird is eating"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"


def feed_bird(bird):
    print(bird.eat())


# 4. Interface Segregation Principle (ISP)
# Classes should implement only the methods they need.

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document")


# 5. Dependency Inversion Principle (DIP)
# High-level code depends on an abstraction.

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(MessageSender):
    def send(self, message):
        print(f"Email sent: {message}")


class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)


# Main program
if __name__ == "__main__":

    # SRP
    report = Report()
    printer = ReportPrinter()
    printer.print_report(report.create_report())

    # OCP
    calculator = AreaCalculator()
    print("Rectangle area:", calculator.calculate(Rectangle(4, 5)))
    print("Circle area:", calculator.calculate(Circle(2)))

    # LSP
    sparrow = Sparrow()
    feed_bird(sparrow)

    # ISP
    simple_printer = SimplePrinter()
    simple_printer.print_document("Hello")

    multi_printer = MultiFunctionPrinter()
    multi_printer.print_document("Report")
    multi_printer.scan_document()

    # DIP
    notification = Notification(EmailSender())
    notification.notify("Your task is complete")