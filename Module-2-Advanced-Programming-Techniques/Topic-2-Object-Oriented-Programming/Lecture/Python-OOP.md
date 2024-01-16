# Object-Oriented Programming in Python

## Introduction to Object-Oriented Programming (OOP)
Welcome to our comprehensive exploration of Object-Oriented Programming (OOP) in Python. OOP is a paradigm that organizes code around data and objects rather than functions and logic. It is instrumental in constructing robust, reusable, and scalable code.

### Why OOP in Python?
- **Real-world Modeling:** OOP facilitates the representation of real-world entities and relationships.
- **Code Reusability:** Inheritance allows classes to be extended and reused.
- **Scalability and Maintainability:** OOP enhances code manageability for growing projects.

## Core Principles of OOP

### 1. Encapsulation
Encapsulation is about bundling data and methods that operate on the data within classes. It helps hide the internal state of an object from the outside world and provides a public interface for interaction.

### 2. Inheritance
Inheritance enables new classes to inherit properties and methods from existing classes, promoting code reusability and establishing relationships.

### 3. Polymorphism
Polymorphism allows a shared interface for different underlying forms, enabling functions to interact with objects of other classes through a common interface.

## Dive into Classes and Objects
Classes are blueprints for creating objects and encapsulating variables and functions into a single entity.

### Creating and Using Classes
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido", 3)
fido.bark()
```

## Access Modifiers in Python: Public, Protected, and Private
Python handles access modifiers differently than some other object-oriented languages. It follows a convention more than strict enforcement.

### Public Members
- **Default Access:** All class members in Python are public by default.
- **Accessibility:** Public members can be accessed anywhere inside or outside a class.

### Protected Members
- **Single Underscore:** Members with a single underscore prefix (`_member`) are protected.
- **Intended Use:** Protected members are intended for internal use but can be accessed from outside classes, though it is conventionally discouraged.

### Private Members
- **Double Underscore:** Members with a double underscore prefix (`__member`) are private.
- **Name Mangling:** Python implements private members by name mangling, which means the interpreter changes the name to make it harder to access from outside. However, it is still technically accessible.

### Encapsulation Example
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

## Inheritance and `super()`
Inheritance is a cornerstone of OOP, and Python's `super()` function is vital in inheritance.

### Basic Inheritance
Inheritance allows extending and customizing classes, while `super()` enables calling methods from the parent class.
```python
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Canine")
        self.name = name
        self.age = age
```

## Implementing Polymorphism
Polymorphism allows for different implementations of methods defined in a parent class.
```python
class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"
```

## Advanced OOP Concepts
- **Dunder Methods:** Customize object behavior with methods like `__str__` and `__repr__`.
- **Composition vs. Inheritance:** Strategies for code reuse.
- **Abstract Base Classes:** Define a common interface for subclasses.

## Practical Exercises
1. **Car Class Implementation:** Create a `Car` class with methods like `start_engine`.
2. **Electric Car Extension:** Develop an `ElectricCar` subclass with unique attributes.
3. **Polymorphism Demonstration:** Use method overriding to demonstrate polymorphism with animal classes.

## Conclusion
Object-Oriented Programming in Python is a powerful tool for building modular, flexible, and scalable applications. Understanding classes, objects, inheritance, polymorphism, access modifiers, and the `super()` function equips you to craft effective software solutions. Practice these concepts, explore different class designs, and embrace OOP's flexibility.

Remember, mastering OOP in Python is a continuous learning and application journey. Happy coding!


## Assignment 1: Implement a Vehicle Class Hierarchy
**Objective:** Design a set of classes representing different types of vehicles.

### Tasks:
1. **Base Vehicle Class:** Create a `Vehicle` class with essential attributes like make, model, year, and starting and stopping methods.
2. **Car Subclass:** Develop a `Car` subclass that extends `Vehicle` and includes car-specific attributes like number of doors.
3. **Truck Subclass:** Create a `Truck` subclass with additional features such as load capacity.

## Assignment 2: Build a Simple Contact Book
**Objective:** Develop a contact book application using OOP principles.

### Tasks:
1. **Contact Class:** Design a `Contact` class with details like name, phone number, and email.
2. **Contact Book Class:** Implement a `ContactBook` class to manage a collection of contacts, with methods to add, remove, and search for contacts.

## Assignment 3: Create a Simple Bank Account Class
**Objective:** Model a basic bank account system using encapsulation.

### Tasks:
1. **Bank Account Class:** Build a `BankAccount` class with private attributes for the account balance and public methods for deposits and withdrawals.
2. **Interest Calculation:** Add a method to calculate interest on the current balance over a period.

## Homework 1: Implement a Basic Product Inventory System
**Objective:** Create a simple system to manage product inventory.

### Tasks:
1. **Product Class:** Develop a class representing products with properties like name, price, and quantity.
2. **Inventory Class:** Design an inventory class to manage a collection of products, including adding and removing items.

## Homework 2: Student and Course Management
**Objective:** Model a basic relationship between students and courses.

### Tasks:
1. **Student Class:** Create a `Student` class with attributes like student ID, name, and enrolled courses.
2. **Course Class:** Implement a `Course` class with details such as course ID, title, and enrolled students.
3. **Enrollment Methods:** Add functionality for students to enroll in and drop courses.

## Homework 3: Build a Simple Employee Management System
**Objective:** Design a system to manage employee information.

### Tasks:
1. **Employee Class:** Construct an `Employee` class with data such as employee ID, name, and position.
2. **Department Class:** Create a `Department` class that manages a group of employees, with methods to add and remove employees.