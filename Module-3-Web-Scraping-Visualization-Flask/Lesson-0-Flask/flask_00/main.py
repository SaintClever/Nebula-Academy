from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/api/greet/", methods=["GET"])  # For default "World" param
@app.route("/api/greet/<name>", methods=["GET"])
def greet(name="World"):
    return jsonify([{"message": f"Hello, {name.title()}!"}])


if __name__ == "__main__":
    app.run(debug=True, port=8080)
