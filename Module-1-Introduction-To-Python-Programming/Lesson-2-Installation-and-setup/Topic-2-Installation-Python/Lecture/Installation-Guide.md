# Setting Up Your Python Development Environment

## Objectives
- Install essential software for Python development.
- Understand the function of development tools and package managers.
- Organize file structure for the course using a Command Line Interface (CLI).

## Introduction
Setting up an effective development environment is crucial for our journey into Python programming. This includes tools and applications for writing and running code. We'll delve into the setup process and explain the purpose of each tool.

## Accessing Course Materials
- **GitHub**: A platform for version control and collaborative coding. A GitHub account is required to access course materials.

## Software Tools and Terminology

### Understanding the Terminal/CLI
- **CLI**: A text-based interface to control the operating System and perform tasks, offering direct control and efficiency for specific operations.
- **Shell**: A program that interprets commands and acts as an intermediary between the user and the OS.
- **Bash**: A Unix shell and command language used as the default shell on most Linux distributions and by Git Bash on Windows.
- **Zsh**: An extended version of Bash with additional features, the default shell on macOS.
- **ASDF**: A version manager for various programming languages and tools, enabling easy installation and version switching.
- **pyenv-win**: A version manager for Python, allowing the installation and management of multiple Python versions on Windows.

## Software Installation

### For First-Time Setup

#### Windows
1. **Chocolatey**: Install by executing the following PowerShell command with Administrator privileges:
```PowerShell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. **pyenv-win**: Install using Chocolatey and configure the environment variables:
```PowerShell
choco install pyenv-win
[System.Environment]::SetEnvironmentVariable('PYENV', $env:USERPROFILE + "\.pyenv\pyenv-win\", "User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT', $env:USERPROFILE + "\.pyenv\pyenv-win\", "User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME', $env:USERPROFILE + "\.pyenv\pyenv-win\", "User")
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"), "User")
```
3. **Python**: Install a specific version using `pyenv` and set it as the global version:
```powershell
pyenv install 3.11.7
pyenv global 3.11.7
```
Verify the installation by checking the Python version in a new PowerShell window:
```PowerShell
python --version
```
4. **Visual Studio Code and Git Bash**: Install both using Chocolatey:
```PowerShell
choco install vscode git
```

#### MacOS
1. **Homebrew**: Install from the official [Homebrew website](https://brew.sh/).
2. **git**: Install with Homebrew:
```Bash
brew install git
```
3. **ASDF Dependencies**: Install using Homebrew:
```Bash
brew install coreutils curl
```
4. **ASDF**: Install and configure with the following commands:
```bash
brew install asdf
echo -e "\n. $(brew --prefix asdf)/asdf.sh" >> ~/.zshrc
```
5. **Python via ASDF**: Manage Python versions with ASDF:
```Bash
asdf plugin add Python
asdf install Python latest
asdf global Python latest
```
6. **Visual Studio Code**: Install with Homebrew and set up the Code CLI:
```Bash
brew install --cask visual-studio-code
```
Enable Code CLI:
- Open VSCode.
- Press `Cmd+Shift+P` to open the command palette.
- Type `Shell Command` and select `Install 'code' command in PATH`.

## Quick Start Guide for Returning Students

Validate your installations by running the following:
- `git --version`
- `python --version`
- `code --version`
- `brew --version` (MacOS)
- `asdf --version` (MacOS)
- `pyenv --version` (Windows)

If any errors occur, follow the install steps in the Installation section.

### Update Installed Software
Keep your software up to date:
- Windows: Upgrade all packages with Chocolatey and update pyenv.
```PowerShell
choco upgrade all
pyenv update
```
- MacOS: Use Homebrew to upgrade all packages.
```bash
brew upgrade
```