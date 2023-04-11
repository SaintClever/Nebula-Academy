In the world of programming, numbers are like building blocks – they provide a foundation upon which we can construct more complex programs and algorithms. In Python, there are several different types of numbers, each with its own unique characteristics and uses.

The most basic type of number in Python is the integer. An integer is like a whole number – it is a numerical value that does not contain any decimal places. For example:

```python
age = 25
```
In this example, the variable “age” contains the integer value 25.

Integers can be manipulated in various ways using different operators and functions. Here are some common examples:

Arithmetic: Performing basic arithmetic operations like addition, subtraction, multiplication, and division using the “+, -, *, /” operators.
```python
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y
print(sum, difference, product, quotient) # prints 15 5 50 2.0
```
Exponentiation: Raising a number to a certain power using the “**” operator.
```python
x = 2
y = 3
result = x ** y
print(result) # prints 8
```
Modulo: Finding the remainder of a division operation using the “%” operator.
```python
x = 10
y = 3
remainder = x % y
print(remainder) # prints 1
```
modulo operator is sometimes refered to as the circular operator as it can be used to constrain a value between a range of numbers:
```python
# create a variable that represents an angle
angle = 540
# while 540° is a valid rotation sometimes it can be more commonly represented between the 0° - 359°
smaller_angle = 540 % 360
print(smaller_angle) # 180

# another common scenario would be too infinitely loop through a list of items
word_list = ['hello','world','python']
for i in range(10):
  # print(word_list[i]) if we uncomment this line our program will fail with a IndexError: list index out of range
  # when we ask for word_list[3] that will be out of bounds of our array which will crash the program

  # so instead we can grab the current index and mod it by 3. Now when we're on the 3rd element 3 % 3 = 0 so we're starting at the beginning of the array again
  word_index = i % len(word_list)
  print(word_list[word_index]) # hello world python hello world python hello
```


---
In addition to integers, Python also supports floating-point numbers, which are like real numbers – they are numerical values that can contain decimal places. For example:
```python
temperature = 98.6
```
In this example, the variable “temperature” contains the floating-point value 98.6.

Floating-point numbers can be manipulated in the same way as integers, but they have some additional capabilities as well. For example, you can use floating-point numbers to represent values like pi or e, or you can use them to perform more precise calculations.