# Variables

In python there is no initialization of a variable when you assign a value a variable is created

```python
# create a new string hello world
str = "Hello World"
print(str)
```

The variable can be reassigned at any time to any data-type

```python
str = "My name is John"
print(str)
str = 31
print(str)
```

You can convert between data-types by casting

```python
str = float("33.3")
print(str)
```

In all programming langauge data-type conversions is going to be one of your most utilized tool because data-types are the containers of data. Each data-type contains `methods` and `properties` to help you interact and manipulate the data

This first example showcases why paying attention to data-types is important. Imagine you are working to make the logic for an ATM machine. The users balance will be a float but the incoming input will be a string.

In programming if you add to a numeric data-type it does arithmitic, however if you add to a string it will append the values
```python
# Create a variable for the users current bank balance
bank_balance = 142.50
# Ask the user how much they want to deposit
deposit_amount = input('How much do you want to deposit\n')
# The following line would give the wrong value because when you add a string to a number it will turn the number into a string and append them
# bankBalance = depositAmount + bankBalance

# So instead we cast depositAmount to a floating point then add to get the arthemtic addition
bank_balance = float(deposit_amount) + bank_balance
print(bank_balance)
```