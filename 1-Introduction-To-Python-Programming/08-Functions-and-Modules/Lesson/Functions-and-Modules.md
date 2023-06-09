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

A function is a block of reusable acode that performs a specific task. It allows you to organize your code into logical and modular units, making it easier to read, understand, and maintain. Functions in Python are defined using the `def` keyword followed by the function name, parentheses, and a colon. They can have parameters and may return a value using the `return` keyword.

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

In Python, a function is defined using the `def` keyword, followed by the function name and parentheses. Parameters can be specified inside the parentheses, and the function body is indented below. 

```python
def function_name(parameters):
    # function body 
    # return value (optional)
```

To execute or "call" a function, you simply use its name followed by parentheses.

```python
function_name(arguments)
```

Pay attention to the difference here between parameters and arguments. Notice we specify or define the name of the parameters in the function definition. We refer to these names as parameters.

However, when we call the function, we pass in arguments. Arguments are the actual values that we pass into the function.

If you noticed in our previous example we had both of these parts. The first code cell contains the function definition, and the second code cell contains the function call.

> ***Note:*** I've seen a lot of students get tripped up by the difference between function reference vs function call. 
>
> A function reference, `function` (Not `function()`) references the contents of the function, but does not execute it. Imagine if I asked you to repeat to what you are going to do at the store. You would say, "I'm going to buy ingredients." You wouldn't actually go to the store and buy the ingredients. You would just reference the action you are going to take.
>
> A function call on the other hand, `function()` actually executes the task. ie. You actually go to the store and buy the ingredients.

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

As a Python developer you will likely use modules on a daily basis. Modules are a great way to organize your own code and make it more reusable, as well as gain access to tools and functionality that other developers in the community have created.

A module in Python is a file containing Python definitions, statements, and functions. It provides a way to organize related code into separate files and promotes code reusability. To use the code defined in a module, you need to import it into your program using the `import` keyword, followed by the module name.

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

Creating our own modules is straightforward. We can create a module by first creating a new Python file and saving it with a `.py` extension. This file will contain the code for our module. We can then import this module into our program using the `import` keyword. We can pick where we want to place the module file, but it is recommended to place it in the same directory as the program that will be using it. Once we have created that file, we use the path to the file to import it into our program.

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
