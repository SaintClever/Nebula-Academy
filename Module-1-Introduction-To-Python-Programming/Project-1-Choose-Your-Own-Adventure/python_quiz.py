import json, random


def json_load():
    with open("questions.json", "r") as f:
        random_question = json.load(f)
        return print(type(random_question[random.randint(0, len(random_question) - 1)]))


json_load()
