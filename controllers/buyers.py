import sqlite3
import os

def initialize_databases():
    #Database creation if it does not exist
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_name TEXT,
    category TEXT,
    item TEXT,
    quantity REAL
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
    conn.commit()
    conn.close()

def user_purchase(user_name):
    initialize_databases()
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    print("PURCHASE MENU")
    print("1. Organic ")
    print("2. Inorganic ")

    category = input("Enter waste category[1-2]: ")

    if category == "1":
        category = "Organic"
        items_list = ["Food waste", "Animal waste", "Yard waste"]

    elif category == "2":
        category = "Inorganic"
        items_list = ["Plastic waste", "Metal waste", "Glass waste"]

    else:
        print("Invalid selection. Please try again!")
        conn.close()
        return

    print(category.upper() + " ITEMS AVALIABLE:")
    for i, items in enumerate(items_list, 1):
        print(f"{i}. {items}")

    item_input = input("Enter item [1-3]: ")
    quantity = input("Enter quantity(kg): ")

    try:
        selected_item = items_list[int(item_input) -1 ]
        quantity = float(quantity)

        if quantity <= 0:
            print("Quantity must be greater than 0")
        elif quantity > 100:
            print("Quantity must be less than 100kg")
            conn.close()
            return
    except (ValueError, IndexError):
        print("Invalid selection")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO purchases(buyer_name, category, item, quantity)
        VALUES (?,?,?,?)
""", (user_name, category, selected_item, quantity))

    conn.commit()
    conn.close()
    print(f"""Purchase recorded:
Category: {category}
Item: {selected_item}
Quantity: {quantity}""")


def view_order_history(user_name):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    cursor.execute("SELECT category, item, quantity FROM purchases WHERE user=?", (user_name,))
    rows = cursor.fetchall()

    if rows:
        print(f"Order history for: {user_name}: ")
        for i, (cat, item, qty) in enumerate(rows, 1):
            print(f"{i}. {cat} - {item} - {qty} kg")
    else:
        print("No order history found.")
    conn.close()

def buyer_menu():
    user_name = input("Enter your username: ")
    while True:
        print("Welcome Buyer! ")
        print("1. Make a purchase. ")
        print("2. View order history. ")
        print("3. Exit. ")
        buyer_decision = input("Enter choice [1-3]: ")

        if buyer_decision == "1":
            user_purchase(user_name)
        elif buyer_decision == "2":
            pass
        elif buyer_decision == "3":
            print("Exiting...")
            break
        else:
            print("Invalid entry. Please try again!")