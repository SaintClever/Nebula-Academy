from flask import Flask, request, jsonify
from db import get_db_connection
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
