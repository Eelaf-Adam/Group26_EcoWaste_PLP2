import sqlite3

def user_purchase(user_name):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    print("")
    print("Choose waste category:")
    print("1. Organic ")
    print("2. Inorganic ")

    category = input("Enter waste category[1-2]: ").strip()

    if category == "1":
        category = "Organic"

    elif category == "2":
        category = "Inorganic"

    else:
        print("Invalid selection. Please try again!")
        conn.close()
        return

    print(category.upper() + " ITEMS AVAILABLE:")

    cursor.execute("""
        SELECT DISTINCT item FROM provider_listings
        WHERE category = ?
        """, (category,))

    items_data = cursor.fetchall()
    if not items_data:
        print(f"No {category} listings available from providers.")
        conn.close()
        return

    items_list = [row[0] for row in items_data]
    print(items_list)

    print("")
    for i, items in enumerate(items_list, 1):
        print(f"{i}. {items}")

    try:
        item_choice = int(input("Enter item number [1-n]: "))
        selected_item = items_list[item_choice - 1]

    except (ValueError, IndexError):
        print("Invalid selection")
        conn.close()
        return

    try:
        quantity = float(input("Enter quantity (kg): "))
        if quantity <= 0 or quantity > 100:
            raise ValueError
    except:
        print("Quantity must be between 0 and 100kg.")
        conn.close()
        return

    cursor.execute("""
        SELECT provider_name, price_per_kg, quantity
        FROM provider_listings
        WHERE category = ? AND item = ? AND quantity >= ?
        ORDER BY price_per_kg ASC
        """, (category, selected_item, quantity))

    offers = cursor.fetchall()

    if not offers:
        print("No providers have enough quantity for this item.")
        conn.close()
        return

    print("")
    print("")
    print("AVAILABLE OFFERS")
    for idx, (provider, price, available_qty) in enumerate(offers, 1):
        print(f"{idx}. Provider: {provider}")
        print(f"Price: {price} UGX")
        print(f"Available: {available_qty} kg")


    try:
        offer_choice = int(input("Choose offer [1-n]: "))
        selected_offer = offers[offer_choice - 1]
    except(ValueError, IndexError):
        print("Invalid offer selection.")
        conn.close()
        return

    provider_name , price_per_kg, _ = selected_offer
    total_cost = price_per_kg * quantity

    cursor.execute("""
        INSERT INTO purchases(buyer_name, category, item, quantity, total_cost)
        VALUES (?, ?, ?, ?, ?)
        """, (user_name, category, selected_item, quantity, total_cost))

    cursor.execute("""
        UPDATE provider_listings
        SET quantity = quantity - ?
        WHERE provider_name = ? AND item = ? AND category = ?
        """, (quantity, provider_name, selected_item, category))

    conn.commit()
    conn.close()


    print("")
    print("====================================")
    print(f"""
Purchase recorded:
Category: {category}
Item: {selected_item}
Quantity: {quantity}
Total Cost: {total_cost} UGX
""")
    print("====================================")


def view_order_history(user_name):
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    cursor.execute("SELECT category, item, quantity, total_cost FROM purchases WHERE buyer_name=?", (user_name,))
    rows = cursor.fetchall()

    if rows:
        print("")
        print("")
        print(f"Order history for: {user_name}: ")
        for i, (cat, item, qty, price) in enumerate(rows, 1):
            print(f"{i}. Category: {cat}")
            print(f"    Item: {item}")
            print(f"    Quantity: {qty}kg")
            print(f"    Total cost: {price} UGX\n")
    else:
        print("No order history found.")
    conn.close()

def buyer_menu(user_name):
    #user_name = input("Enter your username: ")
    while True:
        print("")
        print("")
        print(f"Welcome Buyer! {user_name} ")
        print("1. Make a purchase. ")
        print("2. View order history. ")
        print("3. Exit. ")
        buyer_decision = input("Enter choice [1-3]: ")

        if buyer_decision == "1":
            user_purchase(user_name)
        elif buyer_decision == "2":
            view_order_history(user_name)
        elif buyer_decision == "3":
            print("Exiting...")
            break
        else:
            print("Invalid entry. Please try again!")