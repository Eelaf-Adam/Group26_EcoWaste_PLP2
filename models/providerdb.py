import sqlite3

def add_listings(provider_name, category, item, quantity, price_per_kg):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO provider_listings(provider_name, category, item, quantity, price_per_kg)
    VALUES (?, ?, ?, ?, ?)
    """, (provider_name, category, item, quantity, price_per_kg))
    conn.commit()
    conn.close()

def get_provider_listings(provider_name):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT category, item, quantity, price_per_kg, timestamp
    FROM provider_listings
    WHERE provider_name = ?
    """, (provider_name,))

    rows = cursor.fetchall()
    conn.close()
    return rows