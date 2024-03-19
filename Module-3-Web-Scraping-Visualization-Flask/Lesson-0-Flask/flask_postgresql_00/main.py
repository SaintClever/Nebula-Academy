import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")


# insert data into table
name = input("Name: ")
age = int(input("Age: "))
cursor.execute(f"INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
conn.commit()