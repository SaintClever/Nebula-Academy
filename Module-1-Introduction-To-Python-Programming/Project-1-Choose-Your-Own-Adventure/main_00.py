import os, random
from random_question import random_question


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def final_room():
    question_answer = input(
        """
        Congrats, You're on the final room's question!
        
        Which logical operator would you use to check if a number is both positive and even?
        Question 3Select one:

        a. not
        b. or
        c. is
        d. and

        Answer: """
    )

    if question_answer == "a":
        clear_terminal()
        print("Horay! You completed the game!. You survied Nebula Pymanji\n")
    elif question_answer == "r":
        clear_terminal()
        if random_question():
            print("Great JOB! You're going to the Final stage")
            final_room()
        else:
            print("Mission incomplete :(")
            exit()
    else:
        clear_terminal()
        print(
            """Let's try that again or TYPE "r" for a random question that may lead to death"""
        )

        final_room()


def first_question():
    question_answer = input(
        """
        Congrats, You're on question number 2!
        What function is used to open a file in Python?\n
        
        a. open()
        b. file.open()
        c. file()
        d. open_file()

        Answer: """
    )

    if question_answer == "a":
        clear_terminal()
        final_room()
    elif question_answer == "r":
        clear_terminal()
        if random_question():
            print("Great JOB! You're going to the Final stage")
            final_room()
        else:
            print("Mission incomplete :(")
            exit()
    else:
        clear_terminal()
        print(
            """\tLet's try that again or TYPE "r" for a random question that may lead to death"""
        )

        first_question()


def intro_scene():
    question_answer = input(
        """
        How do you generate a random integer between 1 and 10 using Python?\n
        
        a. random.randint(1, 10)
        b. random.random(1, 10)
        c. random.randrange(1, 11)
        d. random.range(1, 10)

        Answer: """
    )

    if question_answer == "a":
        clear_terminal()
        first_question()
    elif question_answer == "r":
        clear_terminal()
        if random_question():
            print("Great JOB! You're going to the Final stage")
            final_room()
        else:
            print("Mission incomplete :(")
            exit()
    else:
        clear_terminal()
        print(
            """\tLet's try that again or TYPE "r" for a random question that may lead to death"""
        )
        intro_scene()


while True:
    print(
        """
        Welcome to Nebula Pymanji!
        the only way to make it out Graduate / alive is to solve python questions.
        You can exit the game at any time by type Q or E, quiting leads to your doom!
        """
    )

    name = input(
        """
        What's your name: """
    )

    clear_terminal()

    print(
        f"""
        Good luck, {name}!
        """
    )

    intro_scene()
    break
