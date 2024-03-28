import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="postgres",
        password="4321PostgreSQL!",
    )
    return conn
