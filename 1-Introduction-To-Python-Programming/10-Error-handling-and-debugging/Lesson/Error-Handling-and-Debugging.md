# Error Handling and Debugging
# Objectives 🎓
- Understand the nature of an error and techniques to manage it.
- Learn about different types of errors, how to interpret them, and importantly, how to find resources to rectify them.
- Discover how to use `try`, `except`, `else`, and `finally` keywords to manage errors.

---

# Table of Contents 📚
- [Error Handling and Debugging](#error-handling-and-debugging)
- [Objectives 🎓](#objectives-)
- [Table of Contents 📚](#table-of-contents-)
- [Section 1: Acquainting with Python Errors 🛋️](#section-1-acquainting-with-python-errors-️)
  - [1.1 Understanding Python Errors](#11-understanding-python-errors)
  - [1.2 Classifying Errors](#12-classifying-errors)
- [Section 2: Error Control 🛠️](#section-2-error-control-️)
  - [2.1 Using `try` and `except` Constructs](#21-using-try-and-except-constructs)
  - [2.2 Implementing `else` and `finally` Constructs](#22-implementing-else-and-finally-constructs)

---

# Section 1: Acquainting with Python Errors 🛋️

## 1.1 Understanding Python Errors 

When programming in Python, errors can disrupt the code's functionality. These errors can range from simple mistakes like typos to more significant issues that unintentionally cause the program to execute tasks. Python responds to errors by stopping the program and presenting an error message, similar to an alarm indicating something is wrong.

For instance, let's say we're organizing a picnic and must divide the total expenses by the number of participants. If we accidentally try to divide by zero, it would violate basic mathematical principles.

```python
def calculate_cost_per_person(total_cost, num_people):
    return total_cost / num_people

calculate_cost_per_person(100, 0)
```

Executing this code will yield a `ZeroDivisionError`, with Python essentially asserting, "Hold on, division by zero is mathematically unacceptable!"

## 1.2 Classifying Errors

Python code can be disrupted by several types of errors, including:

- **Syntax Errors:** These arise when the code does not adhere to Python's language rules (usually straightforward to rectify).
- **Name Errors:** These manifest when you attempt to utilize an undefined variable or function.
- **Type Errors:** These surface when you perform an operation on an inappropriate type of value.
- **Value Errors:** These occur when you supply a function with an argument of the correct type but an invalid value.
- **ZeroDivision Errors:** These errors pop up when you attempt to divide a number by zero.

Here's an example illustrating each type of error:

```python
# Syntax Error
print("Hello)

# Name Error
print(x)

# Type Error
"2" + 2

# Value Error
int("two")

# ZeroDivision Error
1 / 0
```

**👩🏿‍💻 Your Turn**

*Spot the Errors*

1. Execute the above code cells and identify the specific error type for each one.
2. Correct the errors and rerun the code cells.

```python
```

# Section 2: Error Control 🛠️

## 2.1 Using `try` and `except` Constructs

In programming, errors can be anticipated and even utilized to control the flow of your program. Python's `try` and `except` constructs enable you to test a code block and specify how to handle a particular error. This is like having an emergency plan: if a problem arises, you know what actions to take.
Consider the following function, which converts a string to an integer:

```python
def convert_to_int(input_string):
    return int(input_string)
```

If we pass a non-numeric string, such as 'hello', we'll encounter a `ValueError`.

To prevent our program from halting when this happens, we can handle this specific error using `try` and `except`:

```python
def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        print(f"The input {input_string} cannot be converted to an integer.")
```

If a `ValueError` occurs within the `try` block, the program now executes the code in the `except` block instead of halting entirely.

## 2.2 Implementing `else` and `finally` Constructs

Along with `try` and `except`, Python offers two additional constructs for error handling: `else` and `finally`.

- The `else` block executes if the `try` block doesn't encounter any errors. This can be helpful when you want to perform an action only if no errors occur.

- The `finally` block executes irrespective of whether an error occurs or not. This is usually used for cleanup tasks, such as closing files or releasing resources.

Here's an example to illustrate:

```python
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"The result is {result}")
    finally:
        print("This executes no matter what.")
```

**👨🏽‍💻 Your Turn**

*Implementing Error Handling*

1. Write a function that opens a file and reads its content. Use a `try`/`except` block to handle the potential `FileNotFoundError`.
2. Extend the function by adding `else` and `finally` clauses. The `else` clause should print the file content, and the `finally` clause should ensure the file is closed.

```python
```

To write more robust and reliable code, it's crucial to comprehend Python errors and know how to manage them. Remember that errors are not always negative, as they are crucial for the progress of the development process.

