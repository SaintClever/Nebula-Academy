# * **Task 1.1:** Define a function named `square` that takes one parameter, `number`, and returns the square of that number.
# Call the function with a number of your choice and print the result.
def square(number):
    return number**2


print(square(4))


# * **Task 1.2:** Create a function called `say_hello` that takes no parameters and simply prints `"Hello, Python!"` when called.
def say_hello():
    print("Hello, Python!")


say_hello()


# * **Task 2.1:** Write a function named `add` that takes two parameters, `a` and `b`, adds them together,
# and returns the result. Call the function with two numbers as arguments and print the result.
def add(a, b):
    return a + b


print(add(3, 4))


#  **Task 2.2:** Define a function called `is_even` that takes a single parameter, `num`, and returns
# `True` if the number is even, and `False` otherwise. Demonstrate its use by printing the result of a call with an even and an odd number.
def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(5))


# * **Task 3.1:** Define a function `greet_user` with one parameter, `name`, with a default value of `"Guest"`.
# The function should print a greeting message using the name.
# Call the function twice: first, without any arguments, and second, with a name of your choice.
def greet_user(name="Guest"):
    print(f"Hello {name}")


greet_user()
greet_user("Sebastian!")


# * **Task 3.2:** Create a function named `describe_animal` with two parameters: `animal_type` and `pet_name`.
# Print a description of the animal using these parameters.
# Call this function using keyword arguments to specify the name and type of your pet or a fictional animal.
def describe_animal(animal_type, pet_name):
    print(f"I live with a {animal_type} named {pet_name}")


describe_animal(animal_type="Dog", pet_name="Hennessy")


# * **Challenge 1:** Write a function `max_of_three` that takes three numbers as arguments and returns the largest of them.
# Ensure your function works for a set of any three numbers.
def max_of_three(param_01, param_02, param_03):
    print(max(param_01, param_02, param_03))


max_of_three(867, 5, 309)


# * **Challenge 2:** Implement a function `concat_strings` that takes an arbitrary number of strings (using `*args`) and concatenates
# them into a single string separated by spaces. Test your function with multiple strings.
def concat_strings(*args):
    print(args)

    sentence = ""
    for i in args:
        sentence += i

    print(sentence)


concat_strings("Hello World! ", "Bye sweet World!")
