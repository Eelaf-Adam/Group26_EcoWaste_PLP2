def buyer_menu():
    while True:
        print("Welcome Buyer! ")
        print("1. Make a purchase. ")
        print("2. View order history. ")
        print("3. Exit. ")
        buyer_decision = input("Enter choice [1-3]: ")

        if buyer_decision == "1":
            pass
        elif buyer_decision == "2":
            pass
        elif buyer_decision == "3":
            print("Exiting...")
            break
        else:
            print("Invalid entry. Please try again!")
