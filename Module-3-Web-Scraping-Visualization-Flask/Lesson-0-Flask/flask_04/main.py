import json
from flask import Flask, request, jsonify


app = Flask(__name__)


class User:
    def __init__(self, name: str, age: int, location: str):
        self.name = name
        self.age = age
        self.location = location


def create_user(user):
    with open("data.json", "w") as f:
        json.dump(vars(user), f)


@app.route("/api/", methods=["POST"])
def create():
    data = request.json
    user = User(data.get("name"), data.get("age"), data.get("location"))
    create_user(user)
    return jsonify(user.__dict__)  # user.__dict__ and vars(user) is the same


if __name__ == "__main__":
    app.run(debug=True)
