### Lecture 1: Strings in Python

#### Table of Contents

1. **[Strings](#1-strings)**
   - [1.1 Recognizing and Crafting Strings](#11-recognizing-and-crafting-strings)
   - [1.2 String Formatting with the Format and F-String Methods](#12-string-formatting-with-the-format-and-f-string-methods)
   - [1.3 Utilizing Escape Characters and Raw Strings for Special Characters](#13-utilizing-escape-characters-and-raw-strings-for-special-characters)
   - [1.4 Accessing String Characters via Indexing](#14-accessing-string-characters-via-indexing)
   - [1.5 Utilizing Basic String Methods](#15-utilizing-basic-string-methods)
   - [1.6 Manipulating Strings with Arithmetic Operators](#16-manipulating-strings-with-arithmetic-operators)

#### 1. Strings

**1.1 Recognizing and Crafting Strings**

In Python, strings are sequences of characters enclosed within quotes. For example, `name = "Alice"` creates a variable named `name` containing the string "Alice".

**1.2 String Formatting with the Format and F-String Methods**

Python offers several ways to format strings, such as the `format()` method and f-strings. Example using `format()`: 

```python
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # prints "My name is Alice, and I am 25 years old."
```

**1.3 Utilizing Escape Characters and Raw Strings for Special Characters**

Escape characters, like `\t` for a tab space, insert special characters into strings. Raw strings, indicated by an `r` before the opening quote, ignore escape characters and print backslashes as they are.

**1.4 Accessing String Characters via Indexing**

Access individual characters in a string using their index, represented by a number in square brackets. For example:

```python
name = "Alice"
first_letter = name[0]
print(first_letter)  # prints "A"
```

**1.5 Utilizing Basic String Methods**

Python includes built-in string methods like `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and `split()`. Example using `len()`:

```python
name = "Alice"
length = len(name)
print(length)  # prints 5
```

**1.6 Manipulating Strings with Arithmetic Operators**

Arithmetic operators like `+` for concatenation and `*` for repetition manipulate strings. Example of concatenation:

```python
greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)  # prints "Hello Alice."
```

Python's string capabilities extend further, allowing slicing, case manipulation, and more.

#### Practice Assignments
1. **Create and Manipulate Strings:**
   - Define a string variable and print its length.
   - Concatenate two strings and print the result.
   - Use the `replace()` method to change a specified character in a string.

2. **String Indexing and Slicing:**
   - Extract and print the first and last character of a string.
   - Slice a string to extract a substring and print it.

3. **Experiment with String Methods:**
   - Convert a string to uppercase and lowercase.
   - Split a sentence into words and print the list of words.

#### Homework Assignments
1. **Format a Personal Introduction:**
   - Create a script that uses variables for a person's name and age, then prints an introduction using f-string formatting.

2. **Build a Simple Text Processor:**
   - Write a program that takes a sentence input from the user, counts and prints the number of words, and replaces all occurrences of a specified word.

3. **Explore Escape Characters:**
   - Create a string that includes quotes, a newline, and a tab space. Print it to see how escape characters work.