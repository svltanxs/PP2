import psycopg2
from config import load_config


def connect():
    try:
        conn = psycopg2.connect(**load_config())
        print("Connected to the PostgreSQL server.")
        return conn
    except Exception as error:
        print("Could not connect to the database:", error)
        return None


if __name__ == "__main__":
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version()")
            print(cur.fetchone()[0])
        conn.close()
