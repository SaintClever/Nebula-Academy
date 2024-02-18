import csv

# * **Task 1.1:** Write a Python script to create a CSV file
# Wite csv with a string. Use standare write
csv_content: str = """Name,Age,Major
Alice,24,Computer Science
Bob,22,Mathematics
Charlie,23,Physics"""

with open("students_00.csv", "w") as file:
    file.write(csv_content)


# write csv with a list. Must use csv.writer
data: list = [
    ["Name", "Age", "Major"],
    ["Alice", 24, "Computer Science"],
    ["Bob", 22, "Mathematics"],
    ["Charlie", 23, "Physics"],
]

more_data: list = [
    ["Ted", 54, "Teacher"],
    ["Frank", 42, "Chemist"],
    ["Stephen", 33, "Janitor"],
]

# writerow
with open("students_01.csv", "w") as file:
    csv_writer = csv.writer(file)
    # loop through data and write rows to the csv file that was prepared
    for row in data:
        # print(row)
        csv_writer.writerow(row)


# writerows
with open("students_01.csv", "a") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(more_data)


# * **Task 1.2:** Read the file `students.csv` you just created, print each row to the console.
with open("students_00.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
print()

with open("students_01.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
print()

# * **Task 1.3:** Append a new row with your own choice of data to `students.csv` and print the entire file content to verify the addition.

# write method
# MUST have enter space in string or \n
# string_data: str = """\nBill,12,Youtube Celebrity"""
string_data: str = """
Bill,12,Youtube Celebrity
"""

with open("students_00.csv", "a") as file:
    file.write(string_data)


# writerow method
list_data: list = [["Mike", 56, "Game Developer"]]

with open("students_01.csv", "a") as file:
    csv_write = csv.writer(file)

    for data in list_data:
        csv_write.writerow(data)


# writerows method: faster than for loop and writerow
multi_list_data: list = [
    ["Jane", 6, "Toddler"],
    ["Nelly", 16, "Gamer"],
    ["Agnes", 80, "Granny"],
]

with open("students_01.csv", "a") as file:
    csv_write = csv.writer(file)
    csv_write.writerows(multi_list_data)


# * **Task 2.1:** Create a CSV file `courses.csv` using a dictionary with fieldnames as `CourseID`, `CourseName`, and `Instructor`. Add at least 3 courses to the CSV and print the content of the file.
courses: list = [
    {"CourseID": 867, "CourseName": "Intro to Tech", "Instructor": "Jenny Hu"},
    {"CourseID": 530, "CourseName": "Home Economics", "Instructor": "Sean Phelps"},
    {"CourseID": 900, "CourseName": "Computer Science", "Instructor": "Devon Smilie"},
    {"CourseID": 112, "CourseName": "Psychology", "Instructor": "Amanda Shields"},
    {"CourseID": 311, "CourseName": "Sociology", "Instructor": "Kevin Omar"},
]

new_courses: list = [
    {"CourseID": 620, "CourseName": "Sewing", "Instructor": "Arthur Mack"},
    {"CourseID": 460, "CourseName": "Auto Body", "Instructor": "Cristy Okinova"},
    {"CourseID": 270, "CourseName": "Adulting", "Instructor": "Jeff Hardaway"},
]

field_names: list = ["CourseID", "CourseName", "Instructor"]


# Task 2.1 - write dics
with open("courses.csv", "w", newline="") as file:
    csv_dic_writer = csv.DictWriter(file, fieldnames=field_names)
    csv_dic_writer.writeheader()

    for course in courses:
        csv_dic_writer.writerow(course)


# writerows
with open("courses.csv", "a", newline="") as file:
    csv_dic_writer = csv.DictWriter(file, fieldnames=field_names)
    csv_dic_writer.writerows(new_courses)


# Task 2.2 - read dics
with open("courses.csv", "r") as file:
    csv_dic_reader = csv.DictReader(file)

    for row in csv_dic_reader:
        print(dict(row))
print()

# * **Task 2.3:** Modify the delimiter of your CSV writer and reader to use a semicolon (`;`) instead of a comma, create a new file `courses_semicolon.csv` and perform read/write operations. Verify by printing the content.
csv_course_content: str = """CourseID;CourseName;Instructor
524;Computer Science;Alice
322;Mathematics;Bob
823;Physics;Charlie"""

with open("courses_semicolon.csv", "w") as file:
    file.write(csv_course_content)


with open("courses_semicolon.csv", "r") as file:
    # delimiter removes the ;
    csv_reader = csv.reader(file, delimiter=";")

    for row in csv_reader:
        print(row)
print()

# * **Task 3.1:** Attempt to read a file `nonexistent.csv` that does not exist, handle the `FileNotFoundError` to print a custom error message instead of the default traceback.
try:
    with open("nonexistent.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File Not Found!")

# Reflection
# I prefer CVS...
