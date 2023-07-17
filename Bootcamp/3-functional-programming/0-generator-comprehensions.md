# Generators

One of the reasons why python is growing at such a rapid pace is because of the simplicity of its syntax and powerful baseline functionality

To utilize python to its fullest potential you are going to have to understand `generators`. Generators are use quickly create a sequence.

While you can certainly choose to not use generators you will have to type more lines of code to do similar things and you will see these patterns out in the wild, so their good to practice!

## List Comprehensions

```python
a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [ e**2 for e in a_list if type(e) == types.IntType ]

print(squared_ints)
```

But the key to not getting overwhelmed is to read one character at a time

The first `[` indicates that the generated set will be an array.

The next part (`e**2`) is the `expression output` this is indicating that each element will be squared

The next part is the `input sequence` for `e in a_list` here we create a variable e and iterate over each element in the list as e

The final part of the a generator is an `(optional) predicate` this allows you to put conditions on the elements that will be introduced into the set.

## Set Comprehensions

Here we have a list of names. If we wanted to convert this into a set of proper names, and filter out all the invalid names we could do this very simply with a generator

```python
names = ['John', 'Z', 'dAVID', 'Kira', 'Sam', 'JERRY']

print({
# expression output
    # first character of name    
    name[0].upper() 
    # plus every character after 1st
    + name[1:].lower() 
# input sequence
    # create a variable name that represents each string in names
    for name in names 
# preticate
    # if the length of the name is longer than 1 add it to the set
    if len(name) > 1 
})
# or as a one liner
# print({ name[0].upper() + name[1:].lower() for name in names if len(name) > 1 })

# {'Jerry', 'David', 'Sam', 'Kira', 'John'}
```

## Dictionary Comprehensions

Translating data is one of the most common scenarios a programmer has to solve for. Again the syntax may look confusing at first glance, but all generators follow the `expression output`, `input sequence` & `(optional) predicate` syntax.

For instance lets say we want to generate all the square roots of the numbers between 1-10 easily
```python

print({
# expression output
    # create a key of number
    { num:
    # create a value that is number squared
     num * num }
# input sequence
    # create a variable num that represents every number between 1 and 10
    for num in range(1, 11)
})

# or as a one liner
# print({ num: num * num for num in range(1, 11) })

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```