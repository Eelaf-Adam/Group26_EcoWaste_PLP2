from models.database import SessionLocal
from models.listings import Listing


class BuyerMenu:
    def __init__(self, user):
        self.user = user

    def show(self):
        while True:
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

    def browse_waste(self):
        db = SessionLocal()
        listings = db.query(Listing).all()

        if not listings:
            print("")
            print("No listings available.")
            return

        print("*** Available Waste Listings ***")

        for l in listings:
            print("")
            print(f"Type: {l.type}")
            print(f"Category: {l.category}")
            print(f"Qty: {l.quantity}")
            print(f"Location: {l.location}")

    def view_history(self):
        print("Viewing purchase history...")
