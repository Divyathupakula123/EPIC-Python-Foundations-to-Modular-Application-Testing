# Python Object-Oriented Programming (OOP)

## 1. Introduction

Object-Oriented Programming (OOP) is a programming approach that organizes code using classes and objects.

OOP helps developers write reusable, maintainable, and extensible applications.

### Advantages of OOP
- Code reusability
- Easy maintenance
- Better code organization
- Improved scalability

### Real-World Example

A car has properties such as color and model, and behaviors such as starting and stopping. In Python, we can represent a car using a class and create car objects from it.

## 2. Classes and Objects

### Class
A class is a blueprint used to create objects. It defines attributes and methods.

### Object
An object is an instance of a class. It can have its own data and use the methods defined by its class.

### Python Example

```python
class Student:
    def display(self):
        print("Hello Student")

s1 = Student()
s1.display()

## 3. Constructors (_init_)

### Definition
In Python, __init__() is a special initializer method that runs automatically when an object is created. It initializes the object's attributes.

### Python Example

```python
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Divya", 21)
print(s1.name)
print(s1.age)

## 4. Instance Variables and Class Variables

### Instance Variables
Instance variables store data specific to an individual object. They are commonly created using self inside instance methods.

### Class Variables
Class variables are defined in the class body, outside instance methods. They store data associated with the class and can be shared by its objects unless an instance overrides the attribute.

### Python Example

```python
class Student:
    college = "SVCE"

    def _init_(self, name):
        self.name = name

s1 = Student("Divya")
s2 = Student("Ravi")

print(s1.name)
print(s2.name)
print(Student.college)
print(s1.college)

## 5. Instance, Class, and Static Methods

Python classes commonly use three types of methods.

### 1. Instance Method
An instance method works with an individual object's data. It takes self as its first parameter by convention.

### 2. Class Method
A class method works with class-level data. It uses the @classmethod decorator and takes cls as its first parameter by convention.

### 3. Static Method
A static method is a utility operation associated with a class. It uses the @staticmethod decorator and receives no automatic self or cls parameter.

### Python Example

```python
class Student:
    college = "SVCE"

    def show_name(self, name):
        print(name)

    @classmethod
    def show_college(cls):
        print(cls.college)

    @staticmethod
    def is_adult(age):
        return age >= 18

s1 = Student()
s1.show_name("Divya")
Student.show_college()
print(Student.is_adult(21))

## 6. self and cls

### self
self refers to the current object inside an instance method. It is used to access the object's attributes and methods.

### cls
cls refers to the class itself inside a class method. It is used to access or modify class-level attributes.

### Python Example

```python
class Student:
    college = "SVCE"

    def _init_(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    @classmethod
    def show_college(cls):
        print(cls.college)

s1 = Student("Divya")
s1.show_name()
Student.show_college()

## 7. Object Lifecycle

The object lifecycle describes the stages an object goes through, from creation and initialization to becoming eligible for garbage collection.

### Stages of Object Lifecycle
1. *Creation:* Python creates an object, usually by calling the class.
2. *Initialization:* __init__() initializes the object's attributes.
3. *Usage:* The object is used to access attributes and call methods.
4. *Cleanup:* When an object is no longer reachable, Python may reclaim its memory through garbage collection.

### Lifecycle Diagram

```text
Object Creation
      |
      v
Initialization (_init_)
      |
      v
Object Usage
      |
      v
Object becomes unreachable
      |
      v
Garbage Collection

## 8. Conclusion

Python OOP helps organize programs using classes and objects.

In this lesson, I learned:
- Classes and objects
- Constructors using __init__()
- Instance variables and class variables
- Instance, class, and static methods
- The purpose of self and cls
- The object lifecycle

These concepts help developers write reusable, organized, and maintainable Python applications.