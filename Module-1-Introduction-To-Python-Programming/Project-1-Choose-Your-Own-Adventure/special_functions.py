import os, random


# Clear Terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Random Question
def random_question():
    questions: dict = {
        "What year was python created: ": "1991",
        "Who created Python (Full-Name): ": "Guido van Rossum",
    }

    answer = random.choice(list(questions))
    user_input = input(answer).lower()

    if user_input == questions[answer].lower():
        return True
    return False
