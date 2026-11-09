import psycopg2
from config import load_config


def connect():
    """Establish and return a database connection."""
    try:
        conn = psycopg2.connect(**load_config())
        return conn
    except Exception as error:
        print("Could not connect to the database:", error)
        return None


get_connection = connect

if __name__ == "__main__":
    conn = connect()
    if conn:
        print("Connected to the PostgreSQL server.")
        conn.close()
