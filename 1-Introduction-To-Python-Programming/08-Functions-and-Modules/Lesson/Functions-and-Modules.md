 Additional things to add
    - Scope


# Learning Outcomes
- Discern what a function is and the process of creating one.
- Grasp the distinction between a function definition and a function call.
- Learn to utilize the `return` keyword to return a value from a function.
- Understand the concept of a module and the process to import one.
- Learn to employ the `from` keyword to import specific functions from a module.
- Learn to use the `as` keyword to alias a module or function.
<<<<<<< Updated upstream
~~- Understand the `if __name__ == "__main__"` conditional statement to manage a program's execution.~~
~~- Discover how to use the `sys` module to access command line arguments.~~
=======
>>>>>>> Stashed changes

---

# Table of Contents
- [Learning Outcomes](#learning-outcomes)
- [Table of Contents](#table-of-contents)
- [Section 1: Introduction to Functions](#section-1-introduction-to-functions)
  - [1.1 What is a Function?](#11-what-is-a-function)
- [Section 2: Modules and Importing](#section-2-modules-and-importing)
  - [2.1 Understanding Modules](#21-understanding-modules)
  - [2.2 Creating Your Own Modules](#22-creating-your-own-modules)

---

# Section 1: Introduction to Functions

## 1.1 What is a Function?

**Functions in Python**

In programming, a function is a set of instructions that can be used repeatedly to perform a particular task. It helps to organize code into manageable and understandable units. In Python, you define a function using the `def` keyword, followed by the function name, parentheses, and a colon. Functions can also have parameters and may return values using the `return` keyword.

I've got an idea. Let's have a picnic! Let's start by buying some ingredients at the store.

```python
def buy_ingredients():
    print("Buying ingredients...")
    print("Done!")
    return ["bread", "cheese", "ham", "lettuce"]
```

```python
buy_ingredients()
```

**Function Definition and Function Call**

To define a function in Python, use the `def` keyword followed by the function name and parentheses. You can specify parameters inside the parentheses and indent the function body below.

```python
def function_name(parameters):
    # function body 
    # return value (optional)
```

To execute or "call" a function, you simply use its name followed by parentheses.

```python
function_name(arguments)
```

It's important to distinguish between parameters and arguments. Parameters are defined in the function and are like placeholders for data that will be passed in. Arguments are the values passed in when the function is called. In our previous example, the function definition in the first code cell included the parameter names. The function call in the second code cell provided the actual argument values.

> ***Note:*** I've seen a lot of students get tripped up by the difference between function reference vs function call. 
>
> A function reference, written as `function` (without parentheses), refers to the contents of the function but does not execute it. It's like when someone asks you what you would do at the store, and you reply, "I'm going to buy ingredients." You are referencing the action you plan to take but aren't buying the ingredients at that moment.
>
> When you use the function call `function()`, it actually performs the task. It's like going to the store and buying the necessary ingredients.

**Returning Values From Our Functions**

Often the entire purpose of a function is to return a value. In order to do this, we use the `return` keyword. The `return` keyword is followed by the value we want to return.

```python
string_returning_function():
    return "Hello World!"
```
We can only place the `return` where we plan to complete the function. If we place it before the function is complete, the function will exit and return the value.

Try moving the return in the following statement. What happens?

```python
def string_returning_function():
    return "Hello World!"
    print("This will never print")
```

**👩🏿‍💻 You Do**

*Use a Function*
Let's continue putting together our picnic. 

1. Go to the store and buy the ingredients. (Call the `buy_ingredients()` function and assign it to a variable called `ingredients`.)
2. Write a function `assemble_sandwiches()` that assembles your ingredients into a list and returns it from the function.

```python
```

# Section 2: Modules and Importing

## 2.1 Understanding Modules

*Modules in Python*

As a Python developer, you'll use modules a lot. They can help you keep your code organized, make it easier to reuse, and give you access to tools and functions that other developers have created.

A module is just a file that contains Python code. It lets you group related code together and reuse it in different programs. To use a module in your program, you need to import it using the `import` keyword and the module's name.

Some built-in python modules include `math`, `random`, and `sys`. You can find a list of all the built-in modules in the [Python Standard Library](https://docs.python.org/3/library/index.html). There modules are available to you without having to install any additional packages.

Here is an example of using one of these modules.

```python
import math
print(math.pi)
```

Other packages are available to you through the [Python Package Index](https://pypi.org/). These packages can be installed using the `pip` command. We will cover this in more detail in the next section. Some commonly used packages include `jupyter`, which we are using to run this notebook, `numpy`, `pandas`, and `matplotlib`.

Here is an example of using Matplotlib to plot a graph.

> Note: You need to install Matplotlib using `pip install matplotlib` before running this code. We will cover this in more detail in the next section.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Cool Graph')
plt.show()
```

**Managing packages/modules with `pip`**

The `pip` command is used to install and manage Python packages. It is a package manager that allows you to install, remove, and update packages from the [Python Package Index](https://pypi.org/). It is included by default with Python 3.4 and above. Throughout this course, we will be using `pip` to install and manage packages.

Here are some common `pip` commands:

| Command | Description |
| --- | --- |
| `pip install package_name` | Installs a package |
| `pip uninstall package_name` | Uninstalls a package |
| `pip freeze` | Outputs installed packages in requirements format |
| `pip list` | Lists installed Python packages |
| `pip show package_name` | Shows information about a specific package |
| `pip install -r requirements.txt` | Installs multiple packages from a requirements file |
| `pip upgrade package_name` | Upgrades a specific package |
| `pip install --upgrade pip` | Upgrades pip itself |
| `pip check` | Checks for broken dependencies |

Additional packages can be found on the [Python Package Index](https://pypi.org/) and managed using the commands above.

**👩🏿‍💻 You Do**

*Using `pip` to install packages*





**`pip` - requirements.txt**

`pip` includes the ability to utilize a file, `requirements.txt`, to manage package dependencies.

We can use the `pip freeze` command to output a list of installed packages in requirements format. This is useful when you want to share your code with others and want to make sure they have all the required packages installed. 

Later a developer who downloads your code can use the `pip install -r requirements.txt` command to install all the packages listed in the requirements file.

"You Do" Section

**Importing Modules**
We import modules using the `import` keyword, followed by the module name. This allows us to access the code defined in the module. We ca

```python
import math
print(math.pi)
```

**Importing Specific Modules**

In addition to importing an entire module, you can import specific functions or objects from a module using the `from` keyword. This allows you to access and use only the required functions or objects without importing the entire module. You can specify the specific names after the `from` keyword, separated by commas.

```python
from math import pi

print(pi)
```
**👩🏿‍💻 You Do**

*Importing Modules*

1. Import the `math` module and print the value of pi.
2. Using pip install the 

```python
```

**Importing Multiple Modules**

You can import multiple modules in a single line by separating the module names with commas.

```python
import math, random
```

As well you can import multiple specific functions or objects from a module in a single line by separating the module names with commas.

```python
from math import pi, sqrt
```

**Aliasing Modules and Functions**

Sometimes, when importing modules or functions with long names, it can be tedious to repeatedly type the full name. In such cases, you can use the `as` keyword to provide an alias or shorter name for the module or function. This alias can be used to refer to the module or function throughout your code.

With Aliasing:
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [10, 20, 15, 25, 30])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Cool Graph')
plt.show()
```
Without Aliasing:
```python
import matplotlib.pyplot

matplotlib.pyplot.plot([1, 2, 3, 4, 5], [10, 20, 15, 25, 30])
matplotlib.pyplot.xlabel('X-axis')
matplotlib.pyplot.ylabel('Y-axis')
matplotlib.pyplot.title('My Cool Graph')
matplotlib.pyplot.show()
```

**👩🏿‍💻 You Do**

*Aliasing Modules*

1. Import the `math` module and alias it as `m`.
2. Print the value of pi using the alias.



## 2.2 Creating Your Own Modules

**Creating Modules**

Making our own modules is easy. We can create a module by making a new Python file and saving it with a `.py` extension. This file will contain the code for our module. We can import this module into our program using the `import` keyword. We can choose where to put the module file, but it's better to put it in the same directory as the program that will be using it. Once we have made the file, we use its path to import it into our program.git add 

Here is an example of creating a module and importing it into our program.

```python
# my_module.py
def say_hello():
    print("Hello World!")
```

```python
# main.py
import my_module

my_module.say_hello()
```

**👩🏿‍💻 You Do**

*Create a Module*

Let's create a picnic module so we have picnics in other programs.
1. Create a new file called `picnic.py`.
2. Add our `buy_ingredients()` function to the file.
3. Add our `assemble_sandwiches()` function to the file.
4. Add a `main()` function to the file. This function should `buy_ingredients()` and `assemble_sandwiches()`. We should return a picnic basket list with the sandwiches.
5. Import the `picnic` module into our notebook.
6. Have a picnic!
