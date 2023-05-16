A string in Python is simply a sequence of characters enclosed in quotation marks. For example:

```python
name = "Alice"
```
In this example, the variable “name” contains the string “Alice”.

Strings can be manipulated in various ways using different methods and operators. Here are some common examples:

Concatenation: Combining two strings together using the “+” operator.
```python
greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message) # prints "Hello Alice"
```

Length: Finding the length of a string using the “len()” function.
```python
name = "Alice"
length = len(name)
print(length) # prints 5
```
Indexing: Accessing individual characters in a string using their index.
```python
name = "Alice"
first_letter = name[0]
print(first_letter) # prints "A"
```
Slicing: Extracting a portion of a string using the “[start:end]” notation.
```python
name = "Alice"
first_two_letters = name[0:2]
print(first_two_letters) # prints "Al"
```
Formatting: Replacing placeholders in a string with variables using the “.format()” method.
```python
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message) # prints "My name is Alice and I am 25 years old."
```
In addition to these methods and operators, strings in Python have many other powerful features and capabilities. For example, you can use regular expressions to search for patterns within a string, or you can use string methods to manipulate the case, spacing, and other aspects of a string.