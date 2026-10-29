# Example: Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


# Create an object
account = BankAccount(1000)

# Deposit money
account.deposit(500)

# Display balance
account.show_balance()

# Example: Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Create an object
dog = Dog()

dog.eat()   # Inherited from Animal
dog.bark()  # Defined in Dog

# Example: Multiple Inheritance

class Father:
    def gardening(self):
        print("Father teaches gardening")


class Mother:
    def cooking(self):
        print("Mother teaches cooking")


class Child(Father, Mother):
    def playing(self):
        print("Child likes playing")


# Create an object
child = Child()

child.gardening()
child.cooking()
child.playing()

# Example: Multilevel Inheritance

class Grandparent:
    def house(self):
        print("Grandparent owns a house")


class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")


class Child(Parent):
    def bike(self):
        print("Child owns a bike")


# Create an object
child = Child()

child.house()
child.car()
child.bike()

# Example: Hierarchical Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


# Create objects
dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# Example: Polymorphism and Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Create objects
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Example: Method Overloading Using Default Arguments

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


# Create an object
calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))

# Example: Composition

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        # Engine is created inside Car
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start_car()

# Example: Aggregation

class Teacher:
    def teach(self):
        print("Teacher is teaching")


class School:
    def __init__(self, teacher):
        # School receives an existing Teacher object
        self.teacher = teacher

    def conduct_class(self):
        self.teacher.teach()
        print("Class is conducted")


teacher = Teacher()
school = School(teacher)

school.conduct_class()