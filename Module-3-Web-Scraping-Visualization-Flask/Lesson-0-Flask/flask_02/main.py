from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello World!"})


@app.route("/api/data", methods=["POST"])
def post():
    data = request.json

    print(request.is_json)  # Boolean: True or false
    print(request.json)  # {'name': 'Saint. Clever', 'age': 100}
    print(request.get_json())  # {'name': 'Saint. Clever', 'age': 100}

    # Check if it's JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Check for name key / value
    if "name" not in data or not isinstance(data.get("name"), str):
        return jsonify({"error": '"name" missing in JSON or not a string'}), 400

    # Check for age key / value
    if "age" not in data or not isinstance(data.get("age"), int):
        return jsonify({"error": '"age" missing in JSON or not an int'}), 400

    # Check for age and name key / value
    if "name" not in data and "age" not in data:
        return jsonify({"error": "Both name and age are not in JSON"}), 400

    # return jsonify({"name": data.get("name"), "age": data.get("age")}), 200

    # Return with status key with a value of processed! if all is true
    data["status"] = "processed!"
    return jsonify(data), 200


if "__main__" == __name__:
    app.run(debug=True)
