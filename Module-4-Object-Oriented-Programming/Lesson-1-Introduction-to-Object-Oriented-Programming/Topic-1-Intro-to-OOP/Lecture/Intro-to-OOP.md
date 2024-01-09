# Lecture 1: Introduction to Object-Oriented Programming in Python

---

### **Objectives:**

1. **Familiarize with OOP Concepts:**
   - Introduction to Object-Oriented Programming.
   - Contrasting OOP with Functional Programming: Key Differences and Use Cases.

2. **Understanding Classes and Objects:**
   - Differentiating Classes (Blueprints) and Objects (Instances).
   - Class Structure and Object Creation.

3. **Basic Principles of OOP:**
   - **Encapsulation**: Grouping data and methods within a class.
   - **Inheritance**: Basics of inheriting properties and methods.
   - **Polymorphism**: Designing objects to share behaviors.

---

#### **Introduction to Object-Oriented Programming (OOP)**

- **Core Concept**: Everything is an `Object` in Python and other OOP languages.
- **Functional vs OOP**: Foundational Role of Objects in OOP.

#### **Understanding Objects**

- **Objects as Containers**: Objects are containers for variables.
- **Object Structure and Operations**:
  - Objects have keys mapping to values, e.g., `car = {"topSpeed": 30, "wheels": 4}`.
  - Reading and updating values: `car["topSpeed"] = 50`.
  - Assigning new key-value pairs: `car["currentSpeed"] = 0`.

#### **Introduction to Classes**

- **Classes as Blueprints**: Objects in Python are created from a `class`.
- **Class Example**:
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  ```
- **Constructor Method (`__init__`)**: Initializes new objects from a class.

#### **Creating Objects from Classes**

- **Object Instantiation**: Creating objects, e.g., `person1 = Person("Alice", 25)`.
- **Individual Characteristics**: Objects have unique characteristics.

#### **Adding Methods to Classes**

- **Methods as Actions**: Methods enable objects to perform actions.
- **Method Example**:
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      
      def say_hello(self):
          print("Hello, my name is " + self.name)
  ```
  - Using methods: `person1.say_hello()` → "Hello, my name is Alice".

#### **Conclusion**

- **Summary**: Objects in Python are versatile and defined by their classes.
- **Imagination in OOP**: There are limitless possibilities in Python OOP.