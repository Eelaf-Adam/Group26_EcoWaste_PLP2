import sqlite3
from models.providerdb import get_all_provider_listings
from models.providerdb import get_all_purchases


def view_provider_listings():
    listings = get_all_provider_listings()
    print("")
    print("Provider Listings")
    if not listings:
        print("No listings currently avaliable.")
    for (provider, cat, item, qty, price, time) in listings:
        print("")
        print(f"Provider: {provider}")
        print(f"Category: {cat}")
        print(f"Item: {item}")
        print(f"Quantity: {qty}")
        print(f"Price: {price} UGX/kg")
        print(f"Listed on: {time}")
        print("")

def view_buyers_purchases():
    purchases = get_all_purchases()
    print("Buyer purchases")
    if not purchases:
        print("No purchases found.")
    for (buyer, cat, item, qty, total, time) in purchases:
        print("")
        print(f"Buyer: {buyer}")
        print(f"Category: {cat}")
        print(f"Item: {item}")
        print(f"Quantity: {qty}")
        print(f"Total: {total} UGX ")
        print(f"Time: {time}")
        print("")


def agent_menu(agent_name):
    while True:
        print("")
        print(f"Welcome Agent {agent_name}!")
        print("1. View listed items from providers. ")
        print("2. View buyers and their requests. ")
        print("3. Exit. ")
        agents_decision = input("Enter choice [1-3]: ")
        print("")

        if agents_decision == "1":
            view_provider_listings()
        elif agents_decision == "2":
            view_buyers_purchases()
        elif agents_decision == "3":
            print("Exiting...")
            break
