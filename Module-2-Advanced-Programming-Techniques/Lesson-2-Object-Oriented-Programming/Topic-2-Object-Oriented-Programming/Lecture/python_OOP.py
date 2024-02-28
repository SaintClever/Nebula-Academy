# ## Assignment 1: Implement a Vehicle Class Hierarchy
# **Objective:** Design a set of classes representing different types of vehicles.

# ### Tasks:
# 1. **Base Vehicle Class:** Create a `Vehicle` class with essential attributes like make, model, year, and starting and stopping methods.
# 2. **Car Subclass:** Develop a `Car` subclass that extends `Vehicle` and includes car-specific attributes like number of doors.
# 3. **Truck Subclass:** Create a `Truck` subclass with additional features such as load capacity.

# ## Assignment 2: Build a Simple Contact Book
# **Objective:** Develop a contact book application using OOP principles.

# ### Tasks:
# 1. **Contact Class:** Design a `Contact` class with details like name, phone number, and email.
# 2. **Contact Book Class:** Implement a `ContactBook` class to manage a collection of contacts, with methods to add, remove, and search for contacts.

# ## Assignment 3: Create a Simple Bank Account Class
# **Objective:** Model a basic bank account system using encapsulation.

# ### Tasks:
# 1. **Bank Account Class:** Build a `BankAccount` class with private attributes for the account balance and public methods for deposits and withdrawals.
# 2. **Interest Calculation:** Add a method to calculate interest on the current balance over a period.

# ## Homework 1: Implement a Basic Product Inventory System
# **Objective:** Create a simple system to manage product inventory.

# ### Tasks:
# 1. **Product Class:** Develop a class representing products with properties like name, price, and quantity.
# 2. **Inventory Class:** Design an inventory class to manage a collection of products, including adding and removing items.

# ## Homework 2: Student and Course Management
# **Objective:** Model a basic relationship between students and courses.

# ### Tasks:
# 1. **Student Class:** Create a `Student` class with attributes like student ID, name, and enrolled courses.
# 2. **Course Class:** Implement a `Course` class with details such as course ID, title, and enrolled students.
# 3. **Enrollment Methods:** Add functionality for students to enroll in and drop courses.

# ## Homework 3: Build a Simple Employee Management System
# **Objective:** Design a system to manage employee information.

# ### Tasks:
# 1. **Employee Class:** Construct an `Employee` class with data such as employee ID, name, and position.
# 2. **Department Class:** Create a `Department` class that manages a group of employees, with methods to add and remove employees.


# ### Practical Exercises:
# 1. **Car Class Implementation:** Create a Car class with methods like start_engine.
# 2. **Electric Car Extension:** Develop an ElectricCar subclass with unique attributes.
# 3. **Polymorphism Demonstration:** Use method overriding to demonstrate polymorphism with animal classes.


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Vroom!!! Vroom!!!"

    # for developers
    def __repr__(self):
        return f"The {self.make} {self.model} goes {self.start_engine()}"

    # for customers
    def __str__(self):
        return f"The {self.make} {self.model} goes {self.start_engine()}"


class ElectricCar(Car):
    def __init__(self):
        super().__init__("Mazda", "RX-7")

    def start_engine(self):
        return "Zoom zoom!!!"


class Truck(Car):
    def __init__(self):
        super().__init__("Tesla", "Cybertruck")


mazda = ElectricCar()
print(mazda.__repr__())
print(mazda.__str__())

tesla = Truck()
print(tesla.__repr__())
print(tesla.__str__())


class Animal:
    def __init__(self, species):
        self.species = species


class Bird(Animal):
    def __init__(self, breed, fly: str | None = None):
        super().__init__("Aves")
        self.breed = breed
        self.fly = fly


turkey = Bird("Turkey", "No")
print(turkey.species, turkey.breed, turkey.fly)

halk = Bird("Hawk", "Yes")
print(halk.species, halk.breed, halk.fly)
