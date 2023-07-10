# Introduction to GitHub and the Terminal

1.  **[Introduction](#1-introduction)**
2.  **[GitHub: Getting Started](#2-github-getting-started)**
3.  **[Terminal: Basics and Navigation](#3-terminal-basics-and-navigation)**
4.  **[Practical Applications and Key Concepts](#4-practical-applications-and-key-concepts)**
5.  **[Git: Basics and Key Concepts](#5-git-basics-and-key-concepts)**
6.  **[Exploring .gitignore](#6-exploring-gitignore)**


### 1. Introduction

In this lesson, we'll explore two indispensable tools in programming and software development: GitHub and the Terminal. GitHub is a web-based hosting service for version control — essential for collaboration on team projects — while the Terminal is a powerful interface for navigating your computer and executing commands.

### 2. GitHub: Getting Started

#### 2.1 Signing Up

To start using GitHub, you first need to sign up for an account. Follow these steps:

1.  Navigate to [GitHub.com](https://github.com/).
2.  Click on the "Sign up" button on the top right corner of the page.
3.  Fill in your chosen username, email address, and password. Then click "Create account".
4.  Verify your email address by clicking on the link sent to your email.
5.  Once your account is set up, log in to access the GitHub dashboard.

#### 2.2 Creating a Repository

After setting up your account, let's create your first repository:

1.  Click on the '+' icon at the top right corner of the GitHub dashboard, then select "New repository".
2.  Name your repository and provide a short description.
3.  Choose whether you want your repository to be public or private.
4.  Check the box for "Initialize this repository with a README" – this is a good practice as it explains what your project is about.
5.  Click "Create repository" to finish the process.

### 3. Terminal: Basics and Navigation

#### 3.1 Accessing the Terminal

The process to access the Terminal depends on your operating system. For Windows, you can use PowerShell or Command Prompt; for macOS and Linux, you can use Terminal.

#### 3.2 Basic Commands

Here are some basic commands you can try in your terminal:

 This command creates a new file. To use it, type `touch [file name]`.

| Command | Description                                               | Example                                                                                   |
| ------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `pwd`   | Prints the name of the current directory.                 | `pwd`                                                                                     |
| `ls`    | Lists all files and directories in the current directory. | `ls`                                                                                      |
| `cd`    | Changes the current directory.                            | `cd ..` (to go up one level) <br> `cd [directory name]` (to go into a specific directory) |
| `mkdir` | Creates a new directory.                                  | `mkdir [directory name]`                                                                  |
| `touch` | Creates a new file.                                       | `touch [file name]`                                                                       |


### 4. Practical Applications and Key Concepts

#### 4.1 Understanding Paths

Understanding file paths is crucial to navigate directories effectively. There are two types of paths: absolute and relative. An absolute path starts from the root directory and specifies the exact location of a file or directory. A relative path, on the other hand, starts from the current directory.

#### 4.2 Identifying and Viewing Hidden Files

By default, the Terminal doesn't show hidden files. These files usually start with a dot (`.`), for example, `.gitignore`. To view hidden files, use `ls -a`.

By the end of this lesson, you should feel comfortable navigating GitHub and the Terminal, and understand their crucial role in programming and software development.


### 5. Git: Basics and Key Concepts

#### 5.1 What is Git?

Git is a distributed version control system that allows multiple people to work on a project at the same time without overwriting each other's changes. It's free, open-source, and essential for any programming or software development project.

#### 5.2 Key Terms and Concepts

Here are some common terms and concepts in Git:

| Term              | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Repository (repo) | The project folder containing all the files and their revision history.                         |
| Commit            | A saved change or set of changes in the repo, with a unique ID for tracking purposes.           |
| Branch            | A separate version of the repo for working on new features without affecting the main codebase. |
| Clone             | A copy of the repo that resides on your computer instead of on a server.                        |
| Pull              | A command that updates your local version of a repo to the newest commit.                       |
| Push              | A command that sends your committed changes to a remote repo.                                   |

#### 5.3 Basic Git Commands

Here are some basic commands you can use in Git:

| Command                      | Description                                                                   | Example                                          |
| ---------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------ |
| `git clone [URL]`            | Clones (downloads) a repository from GitHub to your local machine             | `git clone https://github.com/username/repo.git` |
| `git status`                 | Shows the status of changes as untracked, modified, or staged                 | `git status`                                     |
| `git add [file]`             | Adds a file to the staging area in preparation for a commit                   | `git add index.html`                             |
| `git commit -m "[message]"`  | Commits the staged snapshot with a brief description                          | `git commit -m "Add index.html"`                 |
| `git pull`                   | Fetches and merges changes on the remote server to your working directory     | `git pull origin main`                           |
| `git push`                   | Pushes all committed changes in the local repository to the remote repository | `git push origin main`                           |
| `git branch`                 | Lists all local branches in the current repository                            | `git branch`                                     |
| `git checkout [branch-name]` | Switches to the specified branch and updates the working directory            | `git checkout new-feature`                       |
| `git merge [branch-name]`    | Merges the specified branch’s history into the current branch                 | `git merge new-feature`                          |

With these basic commands, you'll be able to start using Git for your projects. It may seem intimidating at first, but with practice, you'll find it's an incredibly powerful tool for collaborative work.

#### 5.4 The Quintessential Git Workflow

The average Git workflow looks something like this:

![assets/git-flow.png](./assets/git-flow.png)

### 6. Exploring .gitignore

#### 6.1 Grasping .gitignore

A .gitignore file is essentially a roadmap that Git follows to determine which files or directories should be kept out of the spotlight. You may have certain components, like local configuration files, build directories, system files, log files, or compiled code that you don't want Git to track within your repository.

#### 6.2 Constructing a .gitignore file

Creating a .gitignore file is an uncomplicated task. In your repository's root directory, you can manually craft a .gitignore file, inputting the names of files and directories that you'd prefer to keep invisible to Git's prying eyes.

To give you an idea, here's a sample .gitignore file for a Python project:

```shell
# Excusing Python build directories
__pycache__/
*.py[cod]

# Steering clear of all log files
*.log

# Bypassing the virtual environment folder
venv/

# Overlooking OS-specific files
.DS_Store
Thumbs.db
```

In the sample above, the # symbol is wielded to add commentary to the .gitignore file.
