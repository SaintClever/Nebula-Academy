# Problem 1
# Create a variable that holds an integer
# Ask the user to enter a float number
# Assign the float number to the integer variable
# Print the integer variable
import math
num = 5
input_num = input('Enter a float number: ')
num = int(float(input_num))
print(num)

# Problem 2
# Create two variables, num1 and num2, and assign them integer values
# Convert num1 to a float and assign it to num1
# Convert num2 to a string and assign it to num2
# Print num1 and num2
num1 = 5
num2 = 10
num1 = float(num1)
num2 = str(num2)
print(num1, num2)

# Problem 3
# Ask the user to input their age as a string
# Convert the string to an integer and store it in age variable
# Use the age variable to calculate how many days the user has been alive and store in a variable called days_alive
# Print the value of days_alive
age = input('Enter your age: ')
age = int(age)
days_alive = age * 365
print(days_alive)

# Problem 4
# Create a variable for the radius of a circle and assign a float value
# Calculate the area of the circle using the formula area = pi * r^2
# Print the area of the circle
radius = 5.0
area = math.pi * radius ** 2
print(area)

# Problem 5
# Create a variable for the user's first name and assign a string value
# Create a variable for the user's last name and assign a string value
# Use string concatenation to create a new variable called full_name that contains the user's full name
# Print the full name
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)
