# Homework:

# Temperature Converter:

# Write a program that converts temperature from Fahrenheit to Celsius and vice versa. Use an if-elif-else block to handle both conversions within the same program.
# Input: Temperature and the unit to convert to (Celsius or Fahrenheit).
# Output: Converted temperature.

temp = input("Temp ex: 32F or 100C: ").lower()
celsius = (32 - 32) * 5 / 9
fahrenheit = (0 * 9 / 5) + 32

if "f" in temp:
    print(f"{celsius}C")
print(f"{fahrenheit}F")
print()

# Grading System:
# Implement a grading system based on scores: A (90-100), B (80-89), C (70-79), D (60-69), F (<60).
# Input: Score as a percentage.
# Output: The corresponding grade.

grade = float(input("Score: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("c")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade < 60:
    print("F")
