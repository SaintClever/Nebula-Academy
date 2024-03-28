"""
Flask-SQLAlchemy
----------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
db = SQLAlchemy(app)


SQLAlchemy
----------
from sqlalchemy import create_engine
engine = create_engine('postgresql://localhost/[YOUR_DATABASE_NAME]')
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(
    dbname="anonymous", user="anonymous", password="***************", host="localhost"
)

# Set the isolation level for the connection to AUTOCOMMIT
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE nebula_academy;")
cursor.execute("DROP DATABASE IF EXISTS nebula_academy")
