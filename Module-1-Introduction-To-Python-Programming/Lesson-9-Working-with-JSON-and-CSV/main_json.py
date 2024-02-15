import json

############ Load JSON     # Create JSON
# INTERNAL: json.loads() |  json.dumps()
# EXTERNAL: json.load()  |  json.dump()


# JSON Handling in Python Assignment
## Exercise 1: Parsing JSON Strings
# Understanding how to convert JSON strings into Python data structures is a fundamental skill for working with JSON in Python.
# ***Task 1.1:** Given the JSON string `{"name": "Alice", "age": 30, "city": "New York"}`, parse it into a Python dictionary and print the dictionary.
json_string = """
{
  "name": "Alice",
  "age": 30,
  "city": "New York"
}"""


# json.loads for internal json string
# ***Task 1.2:** Access the value of the `name` key from the dictionary created in Task 1.1 and print it.
# ***Task 1.3:** Modify the `age` value to `31` in the dictionary from Task 1.1 and print the updated dictionary.
user_info = json.loads(json_string)
print(type(user_info), user_info)
print(user_info["name"])
user_info["age"] = 31
print()


# json.load for external json file
## Exercise 4: JSON and Files
# Working with JSON files is a common task for configuration files, data storage, and more.
# ***Task 4.1:** Write a Python script to load a JSON file named `data.json` containing an array of objects. Print the loaded data.
with open("data.json", "r") as file:
    user_info = json.load(file)
    print(type(user_info), user_info)
print()


# ***Task 4.2:** Modify the data loaded in Task 4.1 by adding a new object to the array. Save the updated array back to `data.json`.
user_info["occupation"] = "Python Developer"
user_info["siblings"] = {
    "brother_00": "Mike",
    "brother_01": "Josh",
    "sister": "Janette",
}

print(user_info)
print()

# CONVERT TO JSON
# The dumps() is used when the objects are required to be in string format and is used for parsing, printing, etc, .
colors: list = ["red", "green", "blue"]
colors_json_string: str = json.dumps(colors, indent=4)
print(type(colors_json_string), colors_json_string)
print()


# CONVERT TO external JSON
# The dump() method is used when the Python objects have to be stored in a file.
## Exercise 2: Generating JSON Strings
# Converting Python data structures to JSON strings is crucial for data storage and communication.
# * **Task 2.1:** Create a Python list named `colors` with the elements `"red"`, `"green"`, and `"blue"`. Convert this list to a JSON string and print the string.
colors_json_str: dict = {
    "ketchup": "red",
    "grass": "green",
    "sky": "blue",
    "human_colors": [
        "red",
        "white",
        "blue",
        "green",
        "black",
        "yellow",
        "pink",
        "purple",
    ],
}

with open("colors.json", "w") as file:
    json.dump(colors_json_str, file, indent=4, sort_keys=True)


# ***Task 2.2:** Create a Python dictionary representing a person with keys `name`, `age`, and `skills`, where `skills` is a list of skills. Convert this dictionary to a JSON string with an indentation of 4 spaces and print it.
# Task 2.2
user: dict = {
    "name": "Saint",
    "age": 30,
    "skills": ["Python", "JavaScript", "Drawing", "BMX"],
}

json_string = json.dumps(user)
print(type(json_string), json_string)
print("")


# ***Task 3.1:** Given the nested JSON string `{"employee": {"name": "John Doe", "roles": ["Admin", "User"], "email": "johndoe@example.com"}}`, parse it into a Python object and print the roles of the employee.
# Task 3.1
json_string_00 = """
{
  "employee": {
    "name": "John Doe",
    "roles": ["Admin", "User"],
    "email": "johndoe@example.com"
  }
}"""

print(type(json_string_00))
print()

employee = json.loads(json_string_00)
print(type(employee), employee)
print()


# ***Task 3.2:** Add a new role `"Manager"` to the employee roles in the Python object from Task 3.1, then convert the entire object back to a JSON string and print it.
# Task 3.2
print(employee["employee"]["roles"])
employee["employee"]["roles"].append("Manager")
print(employee)
