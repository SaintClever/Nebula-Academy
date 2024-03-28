### Step 1: Setup PostgreSQL Database
First, make sure your PostgreSQL server is running, and then create a new database and a `users` table.

1. **Create Database:**
   Open your PostgreSQL command line tool and run:
   ```sql
   CREATE DATABASE test_db;
   ```

2. **Create Users Table:**
   Connect to the `test_db` database and create a `users` table.
   ```sql
   \c test_db
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100)
   );
   ```
   
  **Insert test user**
  
  ```sql
  INSERT INTO users (name, email) VALUES ('Test User', 'testuser@example.com');
  ```

### Step 2: Setup Flask API
You'll need Flask and Psycopg2 to connect to your PostgreSQL database. If you haven't installed these yet, you can do so by running:

```sh
pip install Flask psycopg2
```

### Step 3: Flask App Structure
Your Flask application structure could look something like this:
```
/your-directory
    app.py
    db.py
```

- **db.py:** This file will handle the database connection.
- **app.py:** This is where you'll define your Flask API routes for CRUD operations.

### Step 4: Database Connection (db.py)
Create a file named `db.py` with the following content to handle database connections:

```python
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='test_db',
        user='your_username',
        password='your_password'
    )
    return conn
```

Replace `your_username` and `your_password` with your actual PostgreSQL credentials.

### Step 5: Flask API for CRUD Operations (app.py)
Create `app.py` with the following content. This script defines routes for creating, reading, updating, and deleting users.

```python
from flask import Flask, request, jsonify
from db import get_db_connection
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)',
                (data['name'], data['email']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s',
                (data['name'], data['email'], id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 6: Run Your Flask App
Run your Flask application by executing:
```sh
python app.py
```

This setup will give you a basic Flask API for creating, reading, updating, and deleting users in your PostgreSQL database. Remember to adjust your database connection details in `db.py` as needed.