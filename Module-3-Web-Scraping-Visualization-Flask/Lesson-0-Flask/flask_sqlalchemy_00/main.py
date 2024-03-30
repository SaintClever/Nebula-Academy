from flask import Flask, request, jsonify
from models import User
from database import SessionLocal

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    user_list = [
        {"id": user.id, "name": user.name, "email": user.email} for user in users
    ]
    return jsonify(user_list), 200


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    db = SessionLocal()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.close()
    return jsonify(data), 201


@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    name = data.get("name")
    email = data.get("email")

    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()

    if user:
        user.name = name
        user.email = email
        db.commit()
        db.close()
        return jsonify({"message": "Usere updated successfully"}), 204
    else:
        db.close()
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
