import sqlite3
from models.providerdb import add_listings, get_provider_listings

def provider_menu(provider_name):
    while True:
        print("")
        print(f"Welcome Provider! {provider_name}")
        print("1. List an item(s). ")
        print("2. View cart. ")
        print("3. Exit. ")
        provider_decision = input("Enter choice[1-3]: ")

        if provider_decision == "1":
            list_items(provider_name)
        elif provider_decision == "2":
            view_cart(provider_name)
            pass
        elif provider_decision == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again!")

def list_items(provider_name):

    print("")
    print("Choose waste category: ")
    print("1. Organic ")
    print("2. Inorganic ")
    category = input("Enter a waste category: ")

    if category == "1":
        category = "Organic"
        items = ["Food waste", "Animal waste", "Yard waste" ]
    elif category == "2":
        category = "Inorganic"
        items = ["Plastic waste", "Metal waste", "Glass waste" ]
    else:
        print("Invalid selection. Please try again!")
        return

    for i, item_name in enumerate(items, 1):
        print(f"{i}. {item_name}")
    try:
        item_choice = int(input("Enter item choice: "))
        selected_item = items[item_choice - 1]
        quantity = float(input("Enter quantity (kg): "))
        price = float(input("Enter price per kg (UGX): "))

        add_listings(provider_name, category, selected_item, quantity, price)

        #conn.commit()
        print(f"{selected_item} listed successfully!")

    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        #conn.close()
        return

def view_cart(provider_name):
    #conn = sqlite3.connect("eco_waste.db")
    #cursor = conn.cursor()
    listings = get_provider_listings(provider_name)

    if listings:
        print("")
        print(f"Listed items for {provider_name}.")
        for i, (cat, item, qty, price, time) in enumerate(listings, 1):
            print(f"{i}. {cat}")
            print(f"{item}")
            print(f"{qty} at {price} UGX/kg")
            print(f"Listed on: {time}")
            print("")
    else:
        print("You have not listed any items yet!")
