from special_functions import clear_terminal, random_question
from rich import print
from rich.console import Console
import json, random

quit_: list = ["e", "q"]

console = Console()

def json_load() -> dict:
    with open("questions.json", "r") as f:
        random_question = json.load(f)
        return random_question[random.randint(0, len(random_question) - 1)]


def final_room():
    question = json_load()
    user_input = input(f"{question["question"]}\n\na. {question["a"]}\nb. {question["b"]}\nc. {question["c"]}\nd. {question["d"]}\n\nAnswer: ")

    if question.get(user_input) == question["answer"]:
        clear_terminal()
        console.print("Horay! You completed the game!. You survied Nebula Pymanji\n", style="bold green")
    elif user_input == "r":
        clear_terminal()
        if random_question():
            console.print("Great JOB! You're going to the Final stage", style="bold green")
            final_room()
        else:
            console.print("\nMission incomplete :(", style="bold red")
            exit()
    elif user_input in quit_:
        exit()
    else:
        clear_terminal()
        print('Let\'s try that again or TYPE "r" for a random question that may lead to death or a quick WIN!')
        final_room()


def first_question():
    question = json_load()
    user_input = input(f"{question["question"]}\n\na. {question["a"]}\nb. {question["b"]}\nc. {question["c"]}\nd. {question["d"]}\n\nAnswer: ")

    if question.get(user_input) == question["answer"]:
        clear_terminal()
        final_room()
    elif user_input == "r":
        clear_terminal()
        if random_question():
            console.print("Great JOB! You're going to the Final stage", style="bold green")
            final_room()
        else:
            console.print("\t\nMission incomplete :(", style="bold red")
            exit()
    elif user_input in quit_:
        exit()
    else:
        clear_terminal()
        print('Let\'s try that again or TYPE "r" for a random question that may lead to death or a quick WIN!')
        first_question()


def intro_scene():
    question = json_load()
    user_input = input(f"{question["question"]}\n\na. {question["a"]}\nb. {question["b"]}\nc. {question["c"]}\nd. {question["d"]}\n\nAnswer: ")

    if question.get(user_input) == question["answer"]:
        clear_terminal()
        first_question()
    elif user_input == "r":
        clear_terminal()
        if random_question():
            console.print("Great JOB! You're going to the Final stage", style="bold green")
            final_room()
        else:
            console.print("Mission incomplete :(", style="bold red")
            exit()
    elif user_input in quit_:
        exit()
    else:
        clear_terminal()
        print('Let\'s try that again or TYPE "r" for a random question that may lead to death or a quick WIN!')
        intro_scene()


while True:
    console.print("\nWelcome to Nebula Pymanji!\n\nthe only way to make it out Graduate / alive is to solve python questions.\nYou can exit the game at any time by type Q or E, quiting leads to your doom!\n", style="bold yellow")

    name = input("What's your name: ")

    clear_terminal()
    console.print(f"Good luck {name}!\n", style="bold yellow")
    intro_scene()
    break
