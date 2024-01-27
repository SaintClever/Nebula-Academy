# Practice Assignments
# Create and Manipulate Strings:

# Define a string variable and print its length.
# Concatenate two strings and print the result.
# Use the replace() method to change a specified character in a string.
# String Indexing and Slicing:

# Extract and print the first and last character of a string.
# Slice a string to extract a substring and print it.
# Experiment with String Methods:

# Convert a string to uppercase and lowercase.
# Split a sentence into words and print the list of words.

#
print(("Hello beautiful world!").replace("Hello beautiful", "Bye cruel"))

#
print(len("Joey: How you doing?"))

#
print("You dirty CON! " + "You mean sly cat ;)")

#
print("Racecar".replace("Race", "Sports"))

#
print("Nebula"[2])
print("Nebula Academy".split())

#
print("Nebula Academy"[0], "Nebula Academy"[-1])

#
print("nebula academy".upper(), "nebula academy".lower(), "nebula academy".capitalize())

#
print(("         Experiment with string methods           ").strip())

#
print("Split a sentence into words and print the list of words.".split())


# Homework Assignments
# Format a Personal Introduction:
name = "Saint"
print(f"hello, my name is {name}. Nice to meet you!".capitalize())

# Create a script that uses variables for a person's name and age, then prints an introduction using f-string formatting.
# Build a Simple Text Processor:
user_name = "Saint"
age = 400
print(f"Hello, my name is {user_name}. I'm {age} years old :)")

# Write a program that takes a sentence input from the user, counts and prints the number of words, and replaces all occurrences of a specified word.
# Explore Escape Characters:
user_input = input("\nWhat's your favorite movie quote? ").capitalize()
print(len(user_input))
print(user_input.replace("filthy", "beautiful"))


# Create a string that includes quotes, a newline, and a tab space. Print it to see how escape characters work.
print('\t"Hello\nWorld!"')
