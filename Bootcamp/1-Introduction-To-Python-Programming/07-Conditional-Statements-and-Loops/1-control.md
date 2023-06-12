# Conditionals

Code is determistic it will always run exactly in the same order from top to bottom.

If there is ever a case where sometimes you want your code to execute some code only some of the time then your brain should immediately think **I NEED A CONDITION!** The most commonly used conditonal statement is a `if` statement.

```python
input = int(input("Pick a number between 1 - 10"))

if input > 10:
    print("That number is too large")

if input < 1:
    print("That number is too small")
```

When working with conditions sometimes we want logic that fires when the condition is true **AND** when the condition is false. This is where the `else` keyword comes into play.

```python
input = int(input("Pick a number larger than 10"))

if input < 11:
    print("That number is too small")

else:
    print("Success!")
```

There are sometimes where you would want to chain multiple conditions together. This is what the `elif` keyword is for. This is short for *else if*. This can be thought as "if the previous conditions were not true, then try this condition"

Combining all three of these keywords (`if`, `elif`, `else`) will allow us to fix up our first example to show a message if the user succesfully inputs a number between 1-10

```python
input = int(input("Pick a number between 1 - 10"))

if input > 10:
    print("That number is too large")

elif input < 1:
    print("That number is too small")

else
    print("You have followed the rules congratulations!!!~")
```