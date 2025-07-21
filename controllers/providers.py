def provider_menu():
    while True:
        print("Welcome Provider!")
        print("1. List an item(s). ")
        print("2. View cart. ")
        print("3. Exit. ")
        provider_decision = input("Enter choice[1-3]: ")

        if provider_decision == "1":
            pass
        elif provider_decision == "2":
            pass
        elif provider_decision == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again!")