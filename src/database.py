import sqlite3

DATABASE_PATH = "data/operations.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_tables():
    connection = get_connection()

    connection.execute("""
    CREATE TABLE IF NOT EXISTS claim_types (
        claim_type_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )""")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            identity_number TEXT NOT NULL,
            address TEXT,
            postal_code TEXT
        )
    """)

    connection.commit()
    connection.close()

def insert_claim_types():
    connection = get_connection()

    connection.execute(
        "INSERT OR IGNORE INTO claim_types (name) VALUES (?)",
        ("Billing",)
    )

    connection.execute(
        "INSERT OR IGNORE INTO claim_types (name) VALUES (?)",
        ("Credit",)
    )

    connection.commit()
    connection.close()

def insert_customer(name, identity_number, address, postal_code):
    connection = get_connection()

    existing_customer = connection.execute(
        "SELECT customer_id FROM customers WHERE identity_number = ?",
        (identity_number,)
    ).fetchone()

    if existing_customer is None:
        connection.execute(
            """
            INSERT INTO customers (name, identity_number, address, postal_code)
            VALUES (?, ?, ?, ?)
            """,
            (name, identity_number, address, postal_code)
        )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    insert_claim_types()

    insert_customer(
        "Ana García",
        "12345678Z",
        "Calle Mayor 10",
        "41001"
    )

    insert_customer(
        "Luis Martín",
        "87654321X",
        "Avenida Andalucía 25",
        "41002"
    )