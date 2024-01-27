# 1. **Local Variable Usage**
#    - Define a function `greet()` where you declare a local variable `message = "Hello"` and print it.
def greet():
    message = "Hello"
    print(message)


greet()


# 2. **Global Variable Access**
#    - Declare a global variable `counter = 0`. Create a function `increment()` that modifies `counter` using the `global` keyword.
counter = 0


def increment():
    global counter
    counter = 100
    print(counter)


print(counter)
increment()
print(counter)  # The global counter is modified with the keyword global


# 3. **Using `nonlocal` in Nested Functions**
#    - Create an `outer_function()` that contains a `nested_function()`. Use `nonlocal` to modify a variable declared in `outer_function()`.
def outer_function():
    test = "Outer"

    def nested_function():
        nonlocal test
        test = "Nested"
        print(test)

    print(test)
    nested_function()  # The global test is modified if the nested_function is called invoked. Changing test to Nested
    print(test)


outer_function()
