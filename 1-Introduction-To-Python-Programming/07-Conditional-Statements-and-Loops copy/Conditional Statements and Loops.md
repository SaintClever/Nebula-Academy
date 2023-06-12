# Conditional Statements and Loops

1. **[Part 1: Conditional Statements](#part-1-conditional-statements)**
   - [1.1 Introduction to Conditional Statements](#1-1-introduction-to-conditional-statements)
   - [1.2 Implementing Basic Decision Making](#1-2-implementing-basic-decision-making)
   - [1.3 Enhancing Decision Making with Logical Operators](#1-3-enhancing-decision-making-with-logical-operators)
   - [1.4 Nesting Conditional Statements](#1-4-nesting-conditional-statements)
2. **[Part 2: Loops](#part-2-loops)**
   - [2.1 Understanding While and For Loops](#2-1-understanding-while-and-for-loops)
   - [2.2 Controlling Loops with Break and Continue](#2-2-controlling-loops-with-break-and-continue)
3. **[Part 3: Loop-Related Functions](#part-3-loop-related-functions)**
   - [3.1 Mastering the Magic of the range() Function](#3-1-mastering-the-magic-of-the-range-function)
   - [3.2 Utilizing the enumerate() Function](#3-2-utilizing-the-enumerate-function)

### Part 1: Conditional Statements
## 1.1 Introduction to Conditional Statements
Imagine how much easier life would be if computers could think like us! Conditional statements hold the key. At their core lies a combination of classic words: "if", "else", and "elif". To begin with anything in this language requires user input through its handy input() function.

## 1.2 Implementing Basic Decision Making
When an if statement is established in Python code and met by set conditions being fulfilled - any corresponding code within that block will execute. The basics of decision making with Python are really quite simple. By using if statements we're able to write code that executes only if certain conditions are met. If not Python moves on to check additional conditions until it finds a true condition or defaults to an else clause.

## 1.3 Enhancing Decision Making with Logical Operators
Should we need even more complexity in our decision making code Python offers operators such as "and" "or" and "not". These operators allow us to create more nuanced conditions for our if, elif, and else statements.

## 1.4 Nesting Conditional Statements
And should we find ourselves requiring even greater depth? Nesting if statements within one another makes it possible— leading towards incredibly sophisticated conditional logic.

# Part 2: Loops
## 2.1 Understanding While and For Loops
Loops allow us to execute a block of code repeatedly until a certain condition is met. In Python we use two types of loops: `while` and `for`. In a `while` loop the program continues to execute the block of code as long as the condition holds true. Conversely a `for` loop iterates over a sequence and executes its body for each value in that sequence.

## 2.2 Controlling Loops with Break and Continue
But what if we need to break out of this cycle or skip certain iterations within it? We can use keywords like `break` and `continue` to control program flow. Python's `break` and `continue` are powerful tools when it comes to controlling loops. With `break` you can stop the loop at a specific point while with `continue` you can skip over certain steps.

# Part 3: Loop-Related Functions
## 3.1 Mastering the Magic of the range() Function
Before we even get to using these handy keywords we need to understand another powerful

 Python function: `range()`. The `range()` function is often used in loops to determine the number of times a block of code should be executed.

## 3.2 Utilizing the enumerate() Function
Lastly, the `enumerate()` function is another powerful tool that adds a counter to our loop, which can be very useful for tracking the index of an item in a sequence. It returns an enumerated object that produces tuples containing indices and values of a list. This can be especially useful when you're looping over a large sequence and you need to keep track of the position of your current item.