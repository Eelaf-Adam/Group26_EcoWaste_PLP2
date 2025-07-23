#This file contains the input prompts for the user
import sqlite3

from controllers.buyers import buyer_menu
from controllers.providers import provider_menu
from controllers.agents import agent_menu

def create_account():
    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    print("ACCOUNT CREATION")
    user_name = input("Create a user name: ").strip()
    password = input("Create a password: ").strip()

    cursor.execute("SELECT * FROM users WHERE username=?", (user_name,))
    if cursor.fetchone():
        print("Username already exists. Please enter new name.")
        conn.close()
        return

    if not user_name or not password:
        print("User name and password cannot be empty")
        conn.close()
        return

    cursor.execute("INSERT INTO users(username, password) VALUES (?,?)", (user_name, password))
    conn.commit()
    conn.close()
    print(f"Your account {user_name} has been created!")

    print("Select user type: ")
    print("1. Buyer ")
    print("2. Provider ")
    print("3. Agent ")

    role = input("Enter your user type[1-3]: ")
    if role not in ["1", "2", "3"]:
        print("Invalid role selected.")
        return

    user_roles(role, user_name)

def user_roles(role, user_name=None):
        if role == "1":
            buyer_menu()
        elif role == "2":
            provider_menu()
        elif role == "3":
            agent_menu()

def existing_account():

    conn = sqlite3.connect("eco_waste.db")
    cursor = conn.cursor()

    print("ACCOUNT INFO MENU")
    user_name = input("Enter your user name: ").strip()
    cursor.execute("SELECT password FROM users WHERE username=?", (user_name,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0]
        password = input("Enter your password: ").strip()

        if password == stored_password:
            print(f"Welcome back {user_name}!")
            print("Select your role: ")
            print("1. Buyer")
            print("2. Provider")
            print("3. Agent")
            role = input("Enter your user type[1-3]: ")
            user_roles(role,user_name)

            if role not in ["1", "2", "3"]:
                print("Invalid user type selected.")
                return
            user_roles(role, user_name)
        else:
            print("Incorrect password.")

    else:
        print("Unable to access account.")
        creation_choice = input("Would you like to create an account? [y/n]: ")
        if creation_choice == "y" or creation_choice == "Y":
            create_account()
        else:
            print("Exiting program...")

    conn.close()

def user_prompts():
    while True:
        print("EcoWaste Management System")
        print("1. Create new account: ")
        print("2. Existing account: ")
        print("3. Exit")
        user_account = input("Enter your selection[1-3]: ")

        if user_account == "1":
            create_account()
        elif user_account == "2":
            existing_account()
        elif user_account == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid selection. Please try again")

if __name__ == "__main__":
    from models.database import initialize_databases
    initialize_databases()
    user_prompts()