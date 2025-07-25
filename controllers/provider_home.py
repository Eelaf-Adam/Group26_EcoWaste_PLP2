class ProviderMenu:
    def __init__(self, user):
        self.user = user

    def show(self):
        while True:
            print("\n Provider Menu")
            print("1. Add new wate")
            print("2. View my listings")
            print("3. Logout")


            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_waste()
            elif choice == "2":
                self.view_listings()
            elif choice == "3":
                print("Logging out..")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_waste(self):
        print(" (Placeholder) Add waste coming soon...")


    def view_listings(self):
        print(" (Placeholder) Viewing your listings...")
