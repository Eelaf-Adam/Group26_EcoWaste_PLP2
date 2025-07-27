# This file contains the featuers for the buyer menu where they can view availabe waste product 

class BuyerMenu:
    def __init__(self, user):
        self.user = user

    def show(self):
        while True:
            try:
                print("\n Buyer Menu")
                print("1. Browse available waste")
                print("2. View purchase history")
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

            except KeyboardInterrput:
                print("\nDetected interruption. Logging out...")
                break 
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def browse_waste(self):
        try:
            print("Browsing waste...")
            # Adding actual browsing logic
        except Exception as e:
            print(f"Error while browsing waste: {e}")

    def view_history(self):
        try:
            print("Viewing purchase history...")
            # Adding actual viewing logic 
        except Exception as e:
            print(f"Error while viewing purchase history: {e}")
