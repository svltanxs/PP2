"""Console PhoneBook application for Practice 08.

Uses the existing connect.py/config.py/database.ini files for PostgreSQL access.
Expected database table: phonebook(id, username, phone).
Expected SQL routines: pattern_check, upsert_contact, add_many_users,
get_contacts, and delete_contact.
"""

import sys

import psycopg2


try:
    from connect import get_connection
except ImportError:
    from connect import connect as get_connection


def db_conn():
    conn = get_connection()
    if conn is None:
        raise RuntimeError(
            "Database connection failed. Check config.py, database.ini, "
            "and whether PostgreSQL is running."
        )
    return conn


def run_select(query, params=()):
    conn = db_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()
    finally:
        conn.close()


def run_call(query, params=(), fetch_one=False):
    conn = db_conn()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchone() if fetch_one else None
    finally:
        conn.close()


def search_contacts(pattern):
    return run_select("SELECT * FROM pattern_check(%s)", (pattern,))


def upsert_contact(username, phone):
    run_call("CALL upsert_contact(%s, %s)", (username, phone))


def add_many_contacts(usernames, phones):
    if len(usernames) != len(phones):
        raise ValueError("The number of usernames and phones must be equal.")

    result = run_call(
        "CALL add_many_users(%s, %s, NULL)",
        (usernames, phones),
        fetch_one=True,
    )
    return result[0] if result else []


def get_contacts_page(page_number, page_size):
    if page_number < 1:
        raise ValueError("Page number must be 1 or greater.")
    if page_size < 1:
        raise ValueError("Page size must be 1 or greater.")

    return run_select(
        "SELECT * FROM get_contacts(%s, %s)",
        (page_number, page_size),
    )


def delete_by_username(username):
    run_call("CALL delete_contact(%s, %s)", (username, None))


def delete_by_phone(phone):
    run_call("CALL delete_contact(%s, %s)", (None, phone))


def print_rows(rows):
    if not rows:
        print("No contacts found.")
        return

    for row in rows:
        print(" | ".join(str(value) for value in row))


def main():
    while True:
        print("\n========== PHONEBOOK ==========")
        print("1. Search by username or phone")
        print("2. Add or update one contact")
        print("3. Add many contacts")
        print("4. Show contacts (pagination)")
        print("5. Delete by username")
        print("6. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                pattern = input("Enter search text: ").strip()
                print_rows(search_contacts(pattern))

            elif choice == "2":
                username = input("Username: ").strip()
                phone = input("Phone (+7XXXXXXXXXX): ").strip()
                if not username or not phone:
                    raise ValueError("Username and phone cannot be empty.")
                upsert_contact(username, phone)
                print("Contact saved.")

            elif choice == "3":
                usernames = [x.strip() for x in input(
                    "Usernames separated by commas: "
                ).split(",")]
                phones = [x.strip() for x in input(
                    "Phones separated by commas: "
                ).split(",")]
                if len(usernames) != len(phones):
                    raise ValueError("Enter the same number of usernames and phones.")
                incorrect = add_many_contacts(usernames, phones)
                print("Bulk insert completed.")
                if incorrect:
                    print("Incorrect records:")
                    for item in incorrect:
                        print("-", item)
                else:
                    print("There were no invalid records.")

            elif choice == "4":
                page_number = int(input("Page number (starting from 1): "))
                page_size = int(input("Number of contacts per page: "))
                print_rows(get_contacts_page(page_number, page_size))

            elif choice == "5":
                username = input("Username to delete: ").strip()
                if not username:
                    raise ValueError("Username cannot be empty.")
                delete_by_username(username)
                print("Delete procedure executed.")

            elif choice == "6":
                phone = input("Phone to delete: ").strip()
                if not phone:
                    raise ValueError("Phone cannot be empty.")
                delete_by_phone(phone)
                print("Delete procedure executed.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Unknown option. Choose 0-6.")

        except (ValueError, TypeError) as error:
            print("Input error:", error)
        except (psycopg2.Error, RuntimeError) as error:
            print("Database error:", error)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped.")
        sys.exit(0)
