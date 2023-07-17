# Lecture: Loops

## Learning Outcomes
- Understand the concept of loops and their importance in programming.
- Differentiate between the `for` and `while` loops.
- Learn to use the `range()` function in loop iterations.
- Grasp the concept of loop control statements: `break` and `continue`.
- Explore practical examples of loops in Python.

## Table of Contents
- [Lecture: Loops](#lecture-loops)
  - [Learning Outcomes](#learning-outcomes)
  - [Table of Contents](#table-of-contents)
  - [Section 1: Introduction to Loops](#section-1-introduction-to-loops)
        - [1.1 What are Loops?](#11-what-are-loops)
  - [Section 2: The `for` Loop](#section-2-the-for-loop)
        - [2.1 Using the `range()` Function](#21-using-the-range-function)
          - [2.2 Iterating with `for` Loops](#22-iterating-with-for-loops)
  - [Section 3: The `while` Loop](#section-3-the-while-loop)
        - [3.1 What is the `while` Loop?](#31-what-is-the-while-loop)
        - [3.2 Executing with `while` Loops](#32-executing-with-while-loops)
        - [3.3 Loop Control Statements](#33-loop-control-statements)
  - [Section 4: Practical Examples](#section-4-practical-examples)
        - [4.1 Example 1: Printing Numbers](#41-example-1-printing-numbers)
        - [4.2 Example 2: Sum of Digits](#42-example-2-sum-of-digits)
        - [4.3 Example 3: Finding Prime Numbers](#43-example-3-finding-prime-numbers)

---

## Section 1: Introduction to Loops

##### 1.1 What are Loops?

**Loops in Python**

Loops are essential components in programming that allow us to repeat a set of instructions multiple times. They help us automate repetitive tasks, iterate over collections of data, and solve complex problems more efficiently. In Python, there are two main types of loops: the `for` loop and the `while` loop.

---

## Section 2: The `for` Loop

**The `for` Loop**

The `for` loop is used when we know the number of iterations in advance or when we want to iterate over elements of a sequence, such as a list or a string. It follows a specific syntax:

```python
for item in sequence:
    # code to be executed
```

Here, `item` represents a variable that will take the value of each element in the sequence, and `sequence` is the collection of elements to iterate over. The code within the loop's block will be executed for each iteration.


**🧑🏽‍💻 You Do**

1. Create a list called `airplanes` with the following planes: "Boeing", "Airbus", "Embraer", "Bombardier", and "ATR".
2. Use a `for` loop to iterate over the list and print each element.

```python
# Your code here

```


##### 2.1 Using the `range()` Function

**The `range()` Function**

The `range()` function allows us to generate a sequence of numbers based on the specified start, stop, and step values. It follows the syntax:

```python
range(start, stop, step)
```

The `start` argument defines the starting value (inclusive), the `stop` argument defines the ending value (exclusive), and the `step` argument defines the increment or decrement between numbers. By default, the `start` value is 0, and the `step` value is 1.

Let's explore some examples of using the `range()` function:

```python
for number in range(5):
    print(number)
```

This code will print the numbers 0, 1, 2, 3, and 4.

```python
for number in range(1, 10, 2):
    print(number)
```

In this example, the loop will iterate over the odd numbers from 1 to 9: 1, 3, 5, 7, and 9.

**🧑🏽‍💻 You Do**

1. Use the `range()` function to print the numbers 1 to 10.
2. Use the `range()` function to print the numbers 10 to 1.

```python
# Your code here
```

###### 2.2 Iterating with `for` Loops

**Iterating Over Elements**

One common use of the `for` loop is to iterate over a sequence, such as a list, string, or tuple. Let's consider an example of printing each element in a list:

```python
dog_breeds = ["Labrador", "Poodle", "Husky", "Beagle", "Bulldog"]
for breed in dog_breeds:
    print(breed)
```

In this example, the `dog_breeds` list is iterated over, and the `print()` function is called for each iteration, displaying the corresponding breed.


```python
for letter in "Python":
    print(letter)
```
**🧑🏽‍💻 You Do**

1. Create a list called `numbers` with the following numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
2. Use a `for` loop to iterate over the list and print each element.

```python
# Your code here
```


**Iterating with `for` and `range()`**

The `range()` function is often used in conjunction with the `for` loop to specify a range of numbers to iterate over. The `range()` function generates a sequence of numbers from a starting value to an ending value (exclusive).

```python
for number in range(1, 6):
    print(number)
```

In this example, the loop will iterate over the numbers 1, 2, 3, 4, and 5, printing each number on a separate line.

**🧑🏽‍💻 You Do**

1. Use the `range()` function with a `for` loop to print the word "Python" from the string `"Python'sAwesome"`.

```python
# Your code here

```

---

## Section 3: The `while` Loop

##### 3.1 What is the `while` Loop?

**The `while` Loop**

The `while` loop is used when we want to repeat a set of instructions until a specific condition is no longer true. It follows a different syntax compared to the `for` loop:

```python
while condition:
    # code to be executed
```

The loop will continue executing as long as the `condition` remains true. If the condition becomes false, the loop will terminate, and the program will proceed to the next line of code after the loop.

##### 3.2 Executing with `while` Loops

**Using a Condition**

The `while` loop continues executing as long as the specified condition remains true. The condition is evaluated before each iteration. Let's consider an example of printing numbers from 1 to 5 using a `while` loop:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

In this code, the loop will execute as long as `number` is less than or equal to 5. After each iteration, the value of `number` is incremented by 1 using the `+=` operator.

**🧑🏽‍💻 You Do**

1. Create a `while` loop that prints the string `"Python's Awesome"` 5 times.

```python
# Your code here

```

##### 3.3 Loop Control Statements

**The `break` Statement**

The `break` statement is used to exit a loop prematurely. It allows us to terminate the loop based on a certain condition, even if the loop's condition is still true. Let's consider an example:

```python
number = 1

while number <= 10:
    if number == 5:
        break
    print(number)
    number += 1
```

In this code, the loop will terminate when `number` becomes 5. The `break` statement is encountered, causing the loop to exit immediately.

Use the `break` statement to exit the loop when `number` is equal to 5.

```python
# Your code here

while number <= 10:
    if number == 5:
        break
    print(number)
    number += 1
```

**The `continue` Statement**

The `continue` statement is used to skip the remaining code in the current iteration and move on to the next iteration. It allows us to bypass certain iterations based on a specific condition. Let's see an example:

```python
number = 1

while number <= 5:
    if number == 3:
        number += 1
        continue
    print(number)
    number += 1
```

In this code, when `number` is equal to 3, the `continue` statement is encountered, and the loop proceeds to the next iteration without executing the remaining code within the loop block. Therefore, the number

 3 will not be printed.


**🧑🏽‍💻 You Do**

**Use the continue and break statements**

1. Print the numbers 1 to 100, skipping odd numbers. Use continue to skip odd numbers.
2. Use the break statement to exit the loop when the number is 50.

```python
# Your code here

```

---

## Section 4: Practical Examples

##### 4.1 Example 1: Printing Numbers

Let's consider an example of using a loop to print numbers from 1 to 10:

```python
for number in range(1, 11):
    print(number)
```

This code will display the numbers 1 to 10, each on a separate line.

##### 4.2 Example 2: Sum of Digits

Here's an example of using a loop to calculate the sum of the digits of a given number:

```python
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("The sum of digits is:", sum_of_digits)
```

In this code, the user is prompted to enter a number. The loop calculates the sum of the digits by continuously extracting the last digit (`digit`) using the modulus operator `%`, adding it to the `sum_of_digits`, and then dividing the number by 10 (`number //= 10`) to remove the last digit. The loop continues until the number becomes 0.

##### 4.3 Example 3: Finding Prime Numbers

Let's see an example of using a loop to find all prime numbers within a given range:

```python
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, "are:")

for number in range(start, end + 1):
    if number > 1:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            print(number)
```

In this code, the user is asked to enter the starting and ending numbers of the range. The loop iterates over each number in the range and checks if it is prime. A number is considered prime if it is greater than 1 and not divisible by any number other than 1 and itself. The inner loop checks for divisibility from 2 to the square root of the number. If a divisor is found, the loop is exited using the `break` statement. If no divisor is found, the `else` block is executed, and the prime number is printed.

---

With loops, we can automate repetitive tasks, iterate over collections, and solve complex problems more efficiently. By mastering the `for` and `while` loops, along with loop control statements like `break` and `continue`, you'll have a powerful set of tools to tackle a wide range of programming challenges.