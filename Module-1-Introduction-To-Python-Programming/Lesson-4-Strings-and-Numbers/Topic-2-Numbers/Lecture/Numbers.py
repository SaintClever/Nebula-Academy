# Practice Assignments
# Basic Arithmetic Operations:
import math

# Perform addition, subtraction, multiplication, and division with integers and floats. Print the results.
# Using Built-In Functions:
print(1 + 1)
print(8674309 - 1000)
print("Hello " * 3)
print(100 / 3.5)
print()

# Find the absolute value, round off a float, and calculate the power of numbers using built-in functions.
# Experiment with the Math Module:
print(abs(-3.14))
print(round(100 / 3.5))
print(pow(5, 2))  # no need for math import
print(5**5)
print()

# Use at least three functions from the math module, such as math.sqrt(), math.pi, and math.pow(), and print their results.
# Homework Assignments
# Calculator Program:
print(math.sqrt(16))
print(math.pi)
print(math.pow(5, 2))


# Write a simple calculator that asks the user for two numbers and an operation (add, subtract, multiply, divide) and then prints the result.
# Explore the Random Module:
def calculator():
    user_input = input("Calculate: ").split()

    try:
        if user_input[1] == "+":
            total = int(user_input[0]) + int(user_input[2])

        elif user_input[1] == "-":
            total = int(user_input[0]) - int(user_input[2])

        elif user_input[1] == "x":
            total = int(user_input[0]) * int(user_input[2])

        elif user_input[1] == "*":
            total = int(user_input[0]) * int(user_input[2])

        elif user_input[1] == "/":
            total = int(user_input[0]) / int(user_input[2])

        print(total)
    except IndexError:
        print("Try adding a space between your int like 4 x 4 instead of 4x4")
        calculator()


calculator()


# Create a script that generates and prints 5 random integers between 1 and 100.
# Infinite and NaN (Not a Number) Concepts:

import random

print(random.sample(range(1, 100), 5))

# or

result = []
while len(result) != 5:
    result.append(random.randint(2, 99))
print(result)
print()


# Write a script demonstrating the use of infinity and NaN in Python. Show how to test for these values in a variable.

import math

# Nan
print(float("nan"), math.isnan(float("nan")))

if math.isnan(float("nan")):
    print("NaN")
else:
    print("It's just Nanna or a number")
print()


# infinity
print(float("inf"), float("-inf"))
print(math.inf, -math.inf)


jeff_bezos_bank_account = 100_000_000_000_000_000_000
infinite_universe = math.inf

if infinite_universe > jeff_bezos_bank_account:
    print("I guess Bezos isn't that rich")
else:
    print("seriously... -___-")
