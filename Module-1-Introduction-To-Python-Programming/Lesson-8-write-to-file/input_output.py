import os

# #### Practice Exercises
# # 1. Create a Python script to write and read a list of your favorite movies to a file.

while True:
    user_movie = input("Favorite movie: ")

    if user_movie:
        with open("favorite_movies.txt", "a") as movie:
            movie.write(f"{user_movie}\n")
    else:
        with open("favorite_movies.txt", "r") as movie:
            print(movie.read())
            break


# # 2. Write a script to check if a file named `notes.txt` exists. If it does, append a new note; if not, create and add a note.
if os.path.isfile("notes.txt"):
    with open("notes.txt", "a") as note:
        note.write("new note added\n")
else:
    with open("notes.txt", "w") as note:
        note.write("note added\n")


# #### Homework
# # 1. Develop a Python script that reads a file and counts the number of words in it.
with open("favorite_movies.txt", "r") as movie:
    print(len("".join(movie.readlines()).split()))


# 2. Create a program that lists all the files in a given directory and prints their file sizes.
for dir_path, dir_names, files in os.walk(input("Directory: ")):
    for file in files:
        file_path = os.path.join(f"{dir_path}/{file}")

        try:
            print(
                f"\n{file}\n"
                f"{os.stat(file_path).st_size} Bytes\n"
                f"{os.stat(file_path).st_size / (1024**2):.2f} MB"
            )
        except FileNotFoundError:
            pass
