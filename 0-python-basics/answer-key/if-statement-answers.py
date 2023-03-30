# Problem 1: Prompt the user to enter their age. If their age is greater than or equal to 18, print "You are an adult". Otherwise, print "You are not an adult".
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# Problem 2: Prompt the user to enter a number. If the number is positive, print "The number is positive". If the number is negative, print "The number is negative". If the number is zero, print "The number is zero".
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Problem 3: Prompt the user to enter their name. If their name is "Alice" or "Bob", print "Hello, Alice/Bob!". Otherwise, print "Hello, stranger!".
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")

# Problem 4: Prompt the user to enter a password. If the password is "password123", print "Access granted". Otherwise, print "Access denied".
password = input("Enter your password: ")
if password == "password123":
    print("Access granted")
else:
    print("Access denied")
