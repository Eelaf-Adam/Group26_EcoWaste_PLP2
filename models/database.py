import sqlite3

def initialize_databases():
    """Initializes the database with all required tables"""
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_name TEXT NOT NULL,
    category TEXT NOT NULL,
    item TEXT NOT NULL,
    quantity REAL NOT NULL,
    total_cost REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS provider_listings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_name TEXT,
    category TEXT,
    item TEXT,
    quantity REAL,
    price_per_kg REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
""")

    conn.commit()
    conn.close()
    print("Database initialized successfully")