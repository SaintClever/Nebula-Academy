"""These examples demonstrate the use of instance methods, class methods, and static methods in different contexts. Instance methods operate on instance variables, class methods operate on class-level variables, and static methods are independent of both instance and class variables."""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

"""Instance methods: These are used when you need to access or modify instance variables within a class. They are typically used for actions or behaviors that depend on the specific instance of the class. For example, methods to manipulate or retrieve data associated with an instance, or perform calculations based on instance attributes. A typical application might be a class representing a person with instance methods for updating their information, calculating their age, or performing actions related to that specific person."""

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Calling instance methods
car1.display_info()
car2.display_info()



class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

"""Class methods: These are used when you need to access or modify class-level variables or perform operations that are not specific to any particular instance. They are commonly used for alternative constructors, factory methods, or utility methods that operate on class-level data. For example, a class representing a database connection might have a class method for creating a connection pool or configuring connection settings. Another example is a class representing mathematical operations where you might have class methods for performing common operations like addition, multiplication, etc."""

# Creating instances of the Circle class using class method
circle1 = Circle.from_diameter(10)
circle2 = Circle.from_diameter(6)

# Printing the radius of the circles
print("Radius of circle1:", circle1.radius)
print("Radius of circle2:", circle2.radius)



class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

"""Static methods: These are used when you don't need access to instance or class variables within a method. They are essentially utility methods that are logically related to the class but do not require access to instance or class attributes. They are often used for helper functions or operations that are independent of class state. For example, a static method might be used for converting units, formatting strings, or performing other generic tasks related to the class. A common application might be a utility class with static methods for performing common string manipulation operations."""

# Using static methods
result_add = MathUtils.add(5, 3)
result_multiply = MathUtils.multiply(5, 3)

print("Result of addition:", result_add)
print("Result of multiplication:", result_multiply)
