# Lecture 3: Understanding Variable Scoping in Python

## Educational Objectives
- Comprehend the concept of variable scope in Python.
- Differentiate between local and global variables.
- Learn about the `global` and `nonlocal` keywords.

### Introduction to Variable Scope
Variable scope refers to the part of the program where a variable is accessible. Understanding scope is crucial for avoiding conflicts and unintended side effects in your code.

### Local vs Global Variables
- **Local Variables:** These are declared inside functions and can only be used within that function. They are created when the function starts and destroyed when the function ends.
- **Global Variables:** These are declared outside any function and can be accessed anywhere in the program. However, to modify a global variable inside a function, you must use the `global` keyword.

### The `global` Keyword
To modify a global variable inside a function, you declare it as `global` in the function. For example:

```python
x = 10  # Global variable

def modify():
    global x
    x = 20

modify()
print(x)  # This will print 20
```

### The `nonlocal` Keyword
The `nonlocal` keyword is used in nested functions to refer to variables in the outer (non-global) scope. It's particularly useful in closures.

```python
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
    
    inner()
    print(x)

outer()  # This will print "nonlocal"
```

## Practice Exercises

1. **Local Variable Usage**
   - Define a function `greet()` where you declare a local variable `message = "Hello"` and print it.

2. **Global Variable Access**
   - Declare a global variable `counter = 0`. Create a function `increment()` that modifies `counter` using the `global` keyword.

3. **Using `nonlocal` in Nested Functions**
   - Create an `outer_function()` that contains a `nested_function()`. Use `nonlocal` to modify a variable declared in `outer_function()`.

## Homework
- Develop a script with a function `show_scope()` that demonstrates a local variable.
- Include a global variable `data` and a function `update_data()` that modifies it.
- Implement an `outer()` function with a

nested `inner()` function, where `inner()` modifies a variable declared in `outer()` using the `nonlocal` keyword.