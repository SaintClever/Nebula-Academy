# Setting Up Your Python Development Environment

## Objectives

- Understand and install essential software for Python development.
- Learn about the purpose and function of development tools and package managers.
- Create an organized file structure for the course using a Command Line Interface (CLI).

## Introduction

Setting up an efficient and effective development environment is crucial as we embark on our Python programming journey. This includes tools and applications for writing and running code. Let's understand the setup process and the purpose of each tool.

## Accessing Course Materials

- **GitHub**: A version control and collaborative coding platform. A GitHub account is required to access course materials.

## Software Tools and Terminology

## Understanding the Terminal/CLI

#### Command Line Interface (CLI)
The Command Line Interface (CLI) is a text-based interface for controlling the operating system and performing tasks. It offers more direct control and can be faster for specific tasks.

#### Shell
A shell is a program that interprets commands and acts as an intermediary between the user and the operating system. It is a command-line interface (CLI) to the operating system.

#### Bash
Bash is a Unix shell and command language. It is commonly used as the shell on most Linux distributions and is the shell Git Bash emulates.

#### Zsh
Zsh is a Unix shell and command language. It is an extended version of Bash with many improvements and features. It is the default shell on macOS. 

#### ASDF
ASDF is a version manager for programming languages and other tools. It allows you to install and manage multiple tool versions and switch between them easily. It is similar to pyenv, which we will use for our Windows Users.

#### pyenv-win
pyenv-win is a version manager for Python. It allows you to install and manage multiple versions of Python and switch between them easily. It is similar to ASDF, which we will use for our macOS Users.

## Software Installation

### For First-Time Setup

#### Windows

1. **Chocolatey**: A package manager for Windows. Simplifies software installation and updates. Install [Chocolatey](https://chocolatey.org/install) by following these steps:
   1. Open a PowerShell with Administrator privileges. (Search for PowerShell in the Start menu, click once, and select "Run as Administrator in the right pane.")
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

2. **pyenv**: Install `pyenv` using Chocolatey with the following steps from an Administrator PowerShell:
   1. Install pyenv-win `choco install pyenv-win`. 
   2. Add environment variables for pyenv.
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
  [System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
  [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
  [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
  ```
3. **Python**: Install Python using `pyenv` with the following steps from an Administrator PowerShell:
   1.  Install Python 3.9.6 `pyenv install 3.11.7`
   2. Set Python 3.9.6 as the global version `pyenv global 3.11.7`
   3. Verify the installation by running `python --version` in a new PowerShell window. You should see the installed Python version.
4.  **Visual Studio Code and Git Bash**: IDE and Unix-like CLI for Windows. Install with `choco install vscode git`.


#### MacOS

1. **Homebrew**: A package manager for MacOS. Install from [Homebrew](https://brew.sh/).
2. **git**: A version control system. Install with `brew install git`.
3. **ASDF Dependencies**: Install the dependencies for ASDF using `brew install coreutils curl`.
4. **ASDF**: A version management tool. Install using the following steps:
   1. Install asdf via Brew: `brew install asdf`
   2. Add asdf to the ZSH config file: `echo -e "\n. $(brew --prefix asdf)/asdf.sh" >> ~/.zshrc`
5. **Python via ASDF**: Manage Python versions flexibly. Install using ASDF commands.
   1. `asdf plugin add python`
   2. `asdf install python latest`
   3. `asdf global python latest`
6. **Visual Studio Code**: An IDE for Python development. Install with `brew install --cask visual-studio-code`.
7. **Code CLI**: A command-line interface for VSCode. Install by:
   1. Open VSCode.
   2. Press Ctrl+Shift+P (Windows) or Cmd+Shift+P (macOS) to open the command palette.
   3. Type `Shell Command` in the search bar and select `Install 'code' command in PATH.`

## Quick Start Guide for Returning Students

Validate you have each thing installed by running the following commands:
- Windows & macOS:
   - `git --version`
      - If git is not installed, install it.
   - `python --version`
      - If Python is not installed, install it.
         - Windows: Install via pyenv.

```pyenv
            - ```pyenv global 3.11.7```
         - MacOs: Use ASDF to install python.
            - ```asdf plugin add python```
            - ```asdf install python latest```
            - ```asdf global python latest```
         - *Missing python version?*
            - ```asdf list all python```
         - *ASDF not installed*
            - Look for install steps in the Installation section.
   - `code --version`
      - If code cli command fails:
         - Check if you have VSCode installed.
            - If you don't have it installed, install it.
               - Windows: ```choco install vscode```
               - MacOs: ```brew install --cask visual-studio-code```
            - If you have it installed, you can turn on the code cli command.
               1. Open VSCode
               2. Press Ctrl+Shift+P (Windows) or Cmd+Shift+P (macOS) to open the command palette.
               3. Type `Shell Command` in the search bar and select `Install 'code' command in PATH.`
 - MacOs:
   - `brew --version`
   - `asdf --version`
 - Windows:
   - `pyenv --version`

-  If you get an error, you need to install the software.




Even if you have everything installed, you should still update everything with the following commands:
- Windows:<br>
   `choco upgrade all`<br>
   `pyenv update`
- MacOS:<br>
   `brew upgrade` <br>
   `asdf plugin update --all` <br>
```