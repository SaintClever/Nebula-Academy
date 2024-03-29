import os

# ### 1. Simple Text Editor
# Create a Python script that acts as a simple text editor. The script should allow the user to create a new text file, write content to it, and save it. It should also allow reading and displaying the content of an existing text file.

# ```python
# # Hint: Use input() to get the filename and operation (e.g., read or write) from the user.
# # Use 'open()' with 'w' or 'r' mode accordingly.
# ```


with open("text_editor.txt", "a") as text_editor:
    user_input: str = input("Text Editor (r to read note): ")

    if user_input == "r":
        with open("text_editor.txt") as text_editor:
            print(text_editor.read())
    else:
        text_editor.write(f"{user_input}\n")
        print("Note added!")


### 2. Log File Summary
# Write a Python program to read a log file (assume it's a text file with each entry on a new line) and print a summary showing how many lines are in the file.

# ```python
# Hint: Open the log file in read mode, use a loop to count the lines, and then print the count.
# ```

with open("text_editor.txt", "r") as text_editor:
    for i, line in enumerate(text_editor.readlines()):
        print(f'{i+1}: {line.replace("\n", "")}')


# ### 3. Update a Text File
# Create a script that updates a specific line in a text file. The user should specify the line number they want to update and the new text for that line.

# ```python
# # Hint: Read the file's content into a list, update the specific line, then write the list back to the file.
# ```

DATA: list = []
# DATA: dict = {}

with open("text_editor.txt", "r") as text_editor:
    print("What line to replace:\n")

    for i, line in enumerate(text_editor.readlines()):
        print(f'{i}: {line.replace("\n", "")}')
        DATA.append(line.replace("\n", ""))
        # DATA[i] = line.replace("\n", "")

with open("text_editor.txt", "w") as text_editor:
    line_number = int(input("\nChoose line number: "))
    DATA[line_number] = input(f"New text for {line_number}: ")
    print("")

    for i, new_line in DATA:
        print(f"\n{i}: {new_line}")
        text_editor.write(f"{new_line}")

    # for key, value in DATA.items():
    #     print(f"{key}: {value}")
    #     text_editor.write(f"{value}\n")


# ### 4. List and Count Words in a Directory
# Develop a Python script that lists all the `.txt` files in a given directory and counts the total number of words across all these text files.

# ```python
# # Hint: Use 'os.listdir()' to find `.txt` files, then open each file, read its contents, and count the words.
# ```

for dir_path, dir_names, files in os.walk(input("Directory: ")):
    for file in files:
        if ".txt" in file:
            with open(file, "r") as read_file:
                print(f"{file}: Word Count - {len(read_file.read().replace('\n', ''))}")

            with open(file, "r") as read_file:
                print(read_file.read() + "\n")
