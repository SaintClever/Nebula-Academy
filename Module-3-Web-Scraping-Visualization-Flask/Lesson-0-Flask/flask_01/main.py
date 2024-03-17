from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello World!"


@app.route("/<username>", methods=["GET"])
def user_name(username):
    return render_template("index.html",
                           name=username.title())  # name is the html file variable. username is the python variable


@app.route("/api/data/")  # Default path name is "Devon"
@app.route("/api/data/<name>", methods=["GET"])
def api(name="Devon"):
    return jsonify({"data": {
                        "name": f"{name.title()}",
                        "age": 100,
                        "location": "NY"}})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
