# Basic Decision Making:
# Write a program to check if a number is positive, negative, or zero.
# Input: Any integer.
# Output: A string stating the type of number.
user_input = int(input("check value: "))

if user_input > -1:
    print("positive")
elif user_input < 0:
    print("negative")
else:
    print("zero")
print()

# Logical Operators:
# Create a program that determines if a year is a leap year. Use logical operators.
# Input: A year.
# Output: True if a leap year, False otherwise.
leap_year = int(input("leap year: "))

if leap_year % 4 == 0 or leap_year % 100 == 0 or leap_year == 400:
    print("leap year")
else:
    print("no leap")
print()


# Nested Conditional Statements:
# Develop a program that categorizes a person's life stage: child (< 18), adult (18-64), senior (> 64).
# Input: Age as an integer.
# Output: The life stage.

life_stage = int(input("life stage: "))

if life_stage < 18 and life_stage >= 0:
    print("child")
elif life_stage >= 18 and life_stage <= 64:
    print("adult")
elif life_stage > 64:
    print("senior")
else:
    print("Your potential parents are still contemplating parenthood...")
