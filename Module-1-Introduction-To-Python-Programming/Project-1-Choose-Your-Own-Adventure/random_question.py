import random


def random_question():
    questions: dict = {
        "\tWhat year was python created: ": "1991",
        "\tWho created Python (Full-Name): ": "Guido van Rossum",
    }

    answer = random.choice(list(questions))
    user_input = input(answer).lower()

    if user_input == questions[answer].lower():
        return True
    return False
