from flask import Flask, request, jsonify
import json


app = Flask(__name__)


# LOAD json file
def load_data():
    with open("data.json") as f:
        return json.load(f)


# SAVE json file
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


# READ
@app.route("/users", methods=["GET"])
def get_users():
    data = load_data()
    return jsonify(data.get("users"))


# CREATE
@app.route("/users", methods=["POST"])
def post_user():
    if request.is_json:  # True or False
        print(request.get_json())  # The is from thunder client POST body
        new_user = request.get_json()
        data = load_data()
        data.get("users").append(new_user)
        save_data(data)
        return jsonify(new_user), 201


# UPDATE
@app.route("/users/<int:user_id>", methods=["PUT"])
def put_user(user_id: int):
    data = load_data()

    user_index = None
    for index, user in enumerate(data.get("users")):
        if user_id == user.get("id"):
            user_index = index
            break

    if user_index:
        user = data.get("users")[user_index]
        print(user)
        update_data = request.get_json()
        user.update(update_data)  # Python method update dict
        data.get("users")[user_index] = user
        save_data(data)
        return jsonify(user), 200
    return jsonify({"message": "Error: user does not exist"}), 400


# DELETE
@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    data = load_data()
    user_index = None
    user_dictionary = None

    for index, user in enumerate(data.get("users")):
        if user_id == user.get("id"):
            user_index = index
            user_dictionary = user
            break

    if user_index:
        data.get("users").pop(user_index)
        save_data(data)
        return jsonify(user_dictionary)
    else:
        return jsonify({"message": "Error: user not found"})


if "__main__" == __name__:
    app.run(debug=True)
