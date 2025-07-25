class BuyerMenu:
    def __init__(self, user):
        self.user = user

    def show(self):
        while True:
            print("\n Buyer Menu")
            print("1. Browse available waste")
            print("2.View purchase history")
            print("3. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.browse_waste()
            elif choice == "2":
                self.view_history()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def browse_waste(self):
        print(" (Placeholder) Browsing waste...")


    def view_history(self):
        print(" (Placeholder) Viewing purchase history...")
