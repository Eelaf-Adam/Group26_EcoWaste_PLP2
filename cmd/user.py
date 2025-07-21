#This file contains the input prompts for the user

#This dictionary stores info of existing accounts
accounts = {}

from controllers.buyers import buyer_menu
from controllers.providers import provider_menu
from controllers.agents import agent_menu

def create_account():
    print("ACCOUNT CREATION")
    user_name = input("Create a user name: ")
    if user_name in accounts:
        print("Username already exists. Please enter new name.")
        return

    password = input("Create a password: ")
    print("Select user type: ")
    print("1. Buyer ")
    print("2. Provider ")
    print("3. Agent ")

    role = input("Enter your user type[1-3]: ")
    accounts[user_name] = password
    print(f"Your account {user_name} has been created!")

    user_roles(role, user_name)

def user_roles(role, user_name=None):
        if role == "1":
            buyer_menu()
        elif role == "2":
            provider_menu()
        elif role == "3":
            agent_menu()

def existing_account():
    print("ACCOUNT INFO MENU")
    user_name = input("Enter your user name: ")
    if user_name in accounts:
        password = input("Enter your password: ")
        if accounts[user_name] == password:
            print(f"Welcome back {user_name}!")
            print("Select your role: ")
            print("1. Buyer")
            print("2. Provider")
            print("3. Agent")
            role = input("Enter your user type[1-3]: ")
            user_roles(role,user_name)
        else:
            print("Incorrect password.")

    else:
        print("Unable to access account.")
        creation_choice = input("Would you like to create an account? [y/n]: ")
        if creation_choice == "y" or creation_choice == "Y":
            create_account()
        else:
            print("Exiting program...")

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
        else:
            print("Invalid selection. Please try again")

user_prompts()