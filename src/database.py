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

if __name__ == "__main__":
    create_tables()
    insert_claim_types()