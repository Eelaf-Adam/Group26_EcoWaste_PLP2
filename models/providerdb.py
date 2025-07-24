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
    WHERE provider_name = ? AND status = 'available'
    """, (provider_name,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_provider_listings():
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT provider_name, category, item, quantity, price_per_kg, timestamp
    FROM provider_listings
    WHERE status = 'available'
    """)

    listings = cursor.fetchall()
    conn.close()
    return listings

def get_all_purchases():
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT buyer_name, category, item, quantity, total_cost, timestamp
        FROM purchases
        """)

    purchases = cursor.fetchall()
    conn.close()
    return purchases

def mark_listings_claimed(provider, item, timestamp):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE provider_listings
        SET status = 'claimed'
        WHERE provider_name = ? AND item = ? AND timestamp = ?
        """, (provider, item, timestamp))
    conn.commit()
    conn.close()
