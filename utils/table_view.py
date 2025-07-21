import sqlite3

conn = sqlite3.connect("eco_waste.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

cursor.execute("SELECT * FROM purchases;")
purchases = cursor.fetchall()
print("Purchases:", purchases)

conn.close()