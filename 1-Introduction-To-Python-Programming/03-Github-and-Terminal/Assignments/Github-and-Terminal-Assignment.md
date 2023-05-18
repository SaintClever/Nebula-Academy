## Your First Python Project on GitHub

**Objective**
In this assignment, we're going to use Git and GitHub to start a Python project repository. You'll recreate a specific file structure, make modifications using commits, and then push those updates back to GitHub. 

**Instructions**
Follow the steps below to complete this assignment:

1. **New Repository:** In GitHub, create a new repository called "python-notes".

2. **Clone the Repository:** Clone the new repository to your local system using the `git clone` command.

3. **Create File Structure:** Use the structure below as a guide to create your file structure:

> **Note:** You should only be using your terminal to create the file structure. Do not use your file explorer or Finder.

``` bash
python-notes/
├── 1-Introduction-To-Python-Programming
│   ├── 03-Github-and-Terminal
│   ├── 04-Variables-and-Operators
│   ├── 05-String-and-Numbers
│   ├── 06-Lists-and-Dictionaries
│   ├── 07-Conditional-statements-and-loops
│   ├── 08-Functions-Modules-and-Dependencies
│   ├── 09-User-Input-and-File-io
│   ├── 10-Error-handling-and-debugging
│   └── Module-1-Project
├── 2-Data-Structures-And-Regex
│   ├── 01-Working-with-Structured-Data
│   ├── 02-Regular-Expressions
│   └── Module-2-Project
├── 3-Functional-Programming
│   ├── 01-Introduction-to-Functional-Programming
│   ├── 02-Lambda-Functions
│   ├── 03-Map-Filter-and-Reduce
│   ├── 04-Generator-Comprehension
│   └── Module-3-Project
├── 4-Object-Oriented-Programming
│   ├── 01-Introduction-to-Object-Oriented-Programming
│   ├── 02-Classes
│   └── Module-4-Project
├── 5-Full-Stack-Web-Development
│   ├── 01-Backend
│   ├── 02-Frontend
│   └── Module-5-Project
└── 6-Data-Vizualization-and-Browser-Automation
    ├── 01-Browser-Automation
    ├── 02-Visualization
    └── Module-6-Project
```


| Command | Description | Example |
| --- | --- | --- |
| `pwd` | Prints the name of the current directory. | `pwd` |
| `ls` | Lists all files and directories in the current directory. | `ls` |
| `cd` | Changes the current directory. | `cd ..` (to go up one level) <br> `cd [directory name]` (to go into a specific directory) |
| `mkdir` | Creates a new directory. | `mkdir [directory name]` |
| `touch` | Creates a new file. | `touch [file name]` |

1. **Add and Commit:** With the new file structure in place, add and commit the changes using `git add` and `git commit` commands.

2. **Push to GitHub:** It's time to push your changes to GitHub. Use the `git push` command to upload your changes to your repository on GitHub.

3. **Verify Your Work:** Check your repository on GitHub. You should see the new file structure in your remote repository (The part of your repository on Github.com).

By following these steps, you'll have set up a Python project repository on GitHub, with a specific file structure. You will also have committed and pushed your changes to GitHub.