# Decoding Variables in Python

## Introduction to Variables
Variables in Python are essential. They are like containers in the programming world that store data values. A variable can be considered a label attached to a value, making it easier to reference and manipulate that value in your code. Here's how you declare a variable in Python:

```python
greeting = "Hello, World!"
```

In this example, `greeting` is a variable that holds the string `"Hello, World!"`.

## Variable Naming Conventions
When naming variables in Python, there are a few rules and best practices to follow:
- Names can include letters, numbers, and underscores but cannot start with a number.
- Variable names should be descriptive, making the code readable (e.g., `student_age` instead of `sa`).
- Avoid using Python's reserved words and function names as variable names.
- Use lowercase letters and underscores for readability (e.g., `my_variable`).

## Dynamic Typing in Python
Python is dynamically typed, meaning the data type of a variable is set when you assign it a value, and it can be changed later. For example:

```python
x = 4      # x is of type int
x = "Sally" # Now x is of type str
```