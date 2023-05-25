# Learning Outcomes
- Discern what a function is and the process of creating one.
- Grasp the distinction between a function definition and a function call.
- Learn to utilize the `return` keyword to return a value from a function.
- Understand the concept of a module and the process to import one.
- Learn to employ the `from` keyword to import specific functions from a module.
- Learn to use the `as` keyword to alias a module or function.
- Understand the `if __name__ == "__main__"` conditional statement to manage a program's execution.
- Discover how to use the `sys` module to access command line arguments.

---

# Table of Contents
- [Learning Outcomes](#learning-outcomes)
- [Table of Contents](#table-of-contents)
- [Section 1: Introduction to Functions](#section-1-introduction-to-functions)
  - [1.1 What is a Function?](#11-what-is-a-function)
- [Section 2: Modules and Importing](#section-2-modules-and-importing)
  - [2.1 Understanding Modules](#21-understanding-modules)
- [Section 3: Conditional Statements and `sys` Module](#section-3-conditional-statements-and-sys-module)
  - [3.1 Conditional Execution](#31-conditional-execution)
  - [3.2 Accessing Command Line Arguments](#32-accessing-command-line-arguments)

---

# Section 1: Introduction to Functions

## 1.1 What is a Function?

*Functions in Python*

A function is a block of reusable code that performs a specific task. It allows you to organize your code into logical and modular units, making it easier to read, understand, and maintain. Functions in Python are defined using the `def` keyword followed by the function name, parentheses, and a colon. They can have parameters and may return a value using the `return` keyword.

I've got an idea. Let's have a picnic! Let's start by buying some ingredients at the store.

```python
def buy_ingredients():
    print("Buying ingredients...")
    print("Done!")
    return ["bread", "cheese", "ham", "lettuce"]
```

```python
buy_ingredients()
```

**Function Definition and Function Call**

In Python, a function is defined using the `def` keyword, followed by the function name and parentheses. Parameters can be specified inside the parentheses, and the function body is indented below. 

```python
def function_name(parameters):
    # function body 
    # return value (optional)
```

To execute or "call" a function, you simply use its name followed by parentheses.

```python
function_name(arguments)
```

Pay attention to the difference here between parameters and arguments. Notice we specify or define the name of the parameters in the function definition. We refer to these names as parameters.

However, when we call the function, we pass in arguments. Arguments are the actual values that we pass into the function.

If you noticed in our previous example we had both of these parts. The first code cell contains the function definition, and the second code cell contains the function call.

> ***Note:*** I've seen a lot of students get tripped up by the difference between function reference vs function call. 
>
> A function reference, `function` (Not `function()`) references the contents of the function, but does not execute it. Imagine if I asked you to repeat to what you are going to do at the store. You would say, "I'm going to buy ingredients." You wouldn't actually go to the store and buy the ingredients. You would just reference the action you are going to take.
>
> A function call on the other hand, `function()` actually executes the task. ie. You actually go to the store and buy the ingredients.

**Returning Values From Our Functions**

Often the entire purpose of a function is to return a value. In order to do this, we use the `return` keyword. The `return` keyword is followed by the value we want to return.

```python
string_returning_function():
    return "Hello World!"
```
We can only place the `return` where we plan to complete the function. If we place it before the function is complete, the function will exit and return the value.

Try moving the return in the following statement. What happens?

```python
def string_returning_function():
    return "Hello World!"
    print("This will never print")
```

**👩🏿‍💻 You Do**

*Use a Function*
Let's continue putting together our picnic. 

1. Go to the store and buy the ingredients. (Call the `buy_ingredients()` function and assign it to a variable called `ingredients`.)
2. Write a function to assemble sandwiches with the ingredients you bought.

```python
```

# Section 2: Modules and Importing

## 2.1 Understanding Modules

*Modules in Python*

A module in Python is a file containing Python definitions, statements, and functions. It provides a way to organize related code into separate files and promotes code reusability. To use the code defined in a module, you need to import it into your program using the `import` keyword, followed by the module name.

**Importing Specific Modules**

In addition to importing an entire module, you can import specific functions or objects from a module using the `from` keyword. This allows you to access and use only the required functions or objects without importing the entire module. You can specify the specific names after the `from` keyword, separated by commas.

**Aliasing Modules and Functions**

Sometimes, when importing modules or functions with long names, it can be tedious to repeatedly type the full name. In such cases, you can use the `as` keyword to provide an alias or shorter name for the module or function. This alias can be used to refer to the module or function throughout your code.

Example with Python Code Block

"You Do" Section

---

# Section 3: Conditional Statements and `sys` Module

## 3.1 Conditional Execution

*Conditional Execution in Python*

Conditional execution allows your program to make decisions and perform different actions based on certain conditions. In Python, the `if` statement is used for conditional execution. You can use comparison operators like `==`, `!=`, `<`, `>`, `<=`, `>=`, and logical operators like `and`, `or`, and `not` to create conditional expressions.

**Managing Program Execution with `if __name__ == "__main__"`**

In Python, the `if __name__ == "__main__"` conditional statement is often used to manage the execution of a program. It allows certain code blocks to be executed only when the script is run directly, but not when it is imported as a module. This can be useful for writing executable scripts and reusable modules.

Example with Python Code Block

"You Do" Section

---

## 3.2 Accessing Command Line Arguments

*Working with Command Line Arguments*

The `sys` module in Python provides access to various system-specific parameters and functions. One useful feature is accessing command line arguments passed to a script. By importing the `sys` module and using the `sys.argv` list, you can access the command line arguments provided when running the script.

Example with Python Code Block

"You Do" Section
