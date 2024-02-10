import os

# #### Practice Exercises
# 1. Create a Python script to write and read a list of your favorite movies to a file.

while True:
    user_movie = input("Favorite movie: ")

    if user_movie:
        with open("favorite_movies.txt", "a") as movie:
            movie.write(f"{user_movie}\n")
    else:
        with open("favorite_movies.txt", "r") as movie:
            print(movie.read())
            break


# 2. Write a script to check if a file named `notes.txt` exists. If it does, append a new note; if not, create and add a note.

if os.path.isfile("notes.txt"):
    print("notes.txt exist")
else:
    print("notes.txt is nonexistent")


# #### Homework
# 1. Develop a Python script that reads a file and counts the number of words in it.
with open("favorite_movies.txt", "r") as movie:
    print(len("".join(movie.readlines()).split()))


# 2. Create a program that lists all the files in a given directory and prints their file sizes.
user_path = os.path.expanduser(input("Paste directory: "))
print(f"\n{os.listdir(user_path)}")
