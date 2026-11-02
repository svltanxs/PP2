import csv
import os
import re

import psycopg2
from psycopg2.errors import UniqueViolation

from connect import connect

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.csv")


def create_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name  VARCHAR(50),
            phone      VARCHAR(20) NOT NULL UNIQUE
        )
    """
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)


def is_valid_phone(phone):
    return re.fullmatch(r"\+?\d{10,15}", phone) is not None


def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return
    print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<16}")
    print("-" * 51)
    for contact_id, first_name, last_name, phone in rows:
        print(f"{contact_id:<5}{first_name:<15}{last_name or '':<15}{phone:<16}")


def insert_from_csv(conn):
    contacts = []
    with open(CSV_FILE, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header line
        for row in reader:
            if len(row) != 3:
                print("Skipped bad row:", row)
                continue
            first_name, last_name, phone = [value.strip() for value in row]
            if first_name and is_valid_phone(phone):
                contacts.append((first_name, last_name or None, phone))
            else:
                print("Skipped bad row:", row)

    if not contacts:
        print("No valid contacts in the file.")
        return

    # ON CONFLICT: a phone that is already in the table is skipped instead of raising an error
    sql = """
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT (phone) DO NOTHING
    """
    with conn:
        with conn.cursor() as cur:
            cur.executemany(sql, contacts)
            added = cur.rowcount
    print(f"Added {added} new contacts ({len(contacts) - added} were already in the phonebook).")


def insert_from_console(conn):
    first_name = input("First name: ").strip()
    last_name = input("Last name (can be empty): ").strip() or None
    phone = input("Phone (e.g. +77011234567): ").strip()

    if not first_name:
        print("First name cannot be empty.")
        return
    if not is_valid_phone(phone):
        print("Wrong phone format: use 10-15 digits, + at the start is allowed.")
        return

    sql = """
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        RETURNING id
    """
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, phone))
                new_id = cur.fetchone()[0]
        print(f"Contact saved with id {new_id}.")
    except UniqueViolation:
        print("A contact with this phone already exists.")


def update_contact(conn):
    phone = input("Phone of the contact you want to change: ").strip()

    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, first_name, last_name, phone FROM phonebook WHERE phone = %s", (phone,))
            contact = cur.fetchone()
    if contact is None:
        print("No contact with this phone.")
        return
    print_contacts([contact])

    print("1. Change first name")
    print("2. Change phone")
    choice = input("Choose: ").strip()

    if choice == "1":
        new_value = input("New first name: ").strip()
        if not new_value:
            print("First name cannot be empty.")
            return
        sql = "UPDATE phonebook SET first_name = %s WHERE phone = %s"
    elif choice == "2":
        new_value = input("New phone: ").strip()
        if not is_valid_phone(new_value):
            print("Wrong phone format: use 10-15 digits, + at the start is allowed.")
            return
        sql = "UPDATE phonebook SET phone = %s WHERE phone = %s"
    else:
        print("Wrong choice.")
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_value, phone))
        print("Contact updated.")
    except UniqueViolation:
        print("Another contact already has this phone.")


def search_contacts(conn):
    print("1. Show all contacts")
    print("2. Search by name (part of first or last name)")
    print("3. Search by phone prefix")
    choice = input("Choose: ").strip()

    if choice == "1":
        sql = "SELECT id, first_name, last_name, phone FROM phonebook ORDER BY id"
        params = None
    elif choice == "2":
        text = input("Name contains: ").strip()
        sql = """
            SELECT id, first_name, last_name, phone FROM phonebook
            WHERE first_name ILIKE %s OR last_name ILIKE %s
            ORDER BY first_name
        """
        params = (f"%{text}%", f"%{text}%")
    elif choice == "3":
        prefix = input("Phone starts with: ").strip()
        sql = """
            SELECT id, first_name, last_name, phone FROM phonebook
            WHERE phone LIKE %s
            ORDER BY phone
        """
        params = (prefix + "%",)
    else:
        print("Wrong choice.")
        return

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
    print_contacts(rows)


def delete_contact(conn):
    print("1. Delete by first name")
    print("2. Delete by phone")
    choice = input("Choose: ").strip()

    if choice == "1":
        value = input("First name: ").strip()
        sql = "DELETE FROM phonebook WHERE first_name = %s RETURNING id, first_name, last_name, phone"
    elif choice == "2":
        value = input("Phone: ").strip()
        sql = "DELETE FROM phonebook WHERE phone = %s RETURNING id, first_name, last_name, phone"
    else:
        print("Wrong choice.")
        return

    # no "with conn" here: the DELETE stays uncommitted until we call commit(),
    # so the user can still cancel it and rollback() brings the rows back
    with conn.cursor() as cur:
        cur.execute(sql, (value,))
        deleted = cur.fetchall()

    if not deleted:
        conn.rollback()
        print("No contacts found.")
        return

    print_contacts(deleted)
    answer = input(f"Delete {len(deleted)} contact(s)? (y/n): ").strip().lower()
    if answer == "y":
        conn.commit()
        print("Deleted.")
    else:
        conn.rollback()
        print("Cancelled, nothing was deleted.")


def main():
    conn = connect()
    if conn is None:
        return

    create_table(conn)

    while True:
        print()
        print("===== PhoneBook =====")
        print("1. Import contacts from CSV")
        print("2. Add a contact from console")
        print("3. Update a contact")
        print("4. Search contacts")
        print("5. Delete a contact")
        print("0. Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                insert_from_csv(conn)
            elif choice == "2":
                insert_from_console(conn)
            elif choice == "3":
                update_contact(conn)
            elif choice == "4":
                search_contacts(conn)
            elif choice == "5":
                delete_contact(conn)
            elif choice == "0":
                break
            else:
                print("Wrong choice.")
        except psycopg2.Error as error:
            conn.rollback()
            print("Database error:", error)

    conn.close()
    print("Bye!")


if __name__ == "__main__":
    main()
