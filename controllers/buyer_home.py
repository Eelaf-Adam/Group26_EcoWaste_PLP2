from models.database import SessionLocal
from models.listings import Listing
from models.purchases import Purchase
from datetime import datetime


class BuyerMenu:
    def __init__(self, user):
        self.user = user

    def show(self):
        while True:

            """
            This function displays the buyer menu
            when called upon and prompts user to
            select next action
            """

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
                print("❌ Invalid choice. Please try again.")

    def browse_waste(self):

        """
        This function interacts with the database
        to display available waste listed by the
        providers
        """

        #Accessing the database
        db = SessionLocal()
        try:
            #Accessing the listings table in the database
            listings = db.query(Listing).filter(Listing.quantity > 0).all()

            if not listings:
                print("")
                print("No listings available.")
                return

            print("")
            print("*** Available Waste Listings ***")

            #Displays the available providers
            for idx, l in enumerate(listings, start=1):
                print("")
                print(f"{idx}. Type: {l.type}")
                print(f"Category: {l.category}")
                print(f"Qty: {l.quantity} kg")
                print(f"Location: {l.location}")

        except (ValueError, IndexError):
            print("❌ Invalid input. Try again.")

        finally:
            db.close()

            try:
                #Prompt for the user to either select a buyer or exit the menu
                selected = int(input("Enter number of listing to purchase (0 to cancel): "))

                if selected == 0:
                    print("❌ Cancelled.")
                    return

                #Removes waste selected from avaliable waste
                listing = listings[selected - 1]

                if listing.provider_id == self.user.id:
                    print("You cannot purchase your own listing.")
                    return

                qty = float(input("Enter quantity to purchase (kg): "))

                if qty <= 0 or qty > listing.quantity:
                    print("❌ Invalid quantity. Must be > 0 and less than available.")
                    return

                listing.quantity -= qty

                purchase = Purchase(
                    buyer_id = self.user.id,
                    listing_id = listing.id,
                    quantity = qty,
                    timestamp = datetime.utcnow()
                )

                db.add(purchase)
                db.commit()

                confirm = input("Confirm your purchase? (yes/no): ").strip().lower()

                if confirm != "yes":
                    print("❌ Purchase cancelled.")
                else:
                    print("✅ Purchase successful!")

            except (ValueError, IndexError):
                print("❌ Invalid input. Try again.")

            finally:
                db.close()


    def view_history(self):

        """
        This function allows the buyers to view
        their previous transactions
        """

        db = SessionLocal()
        try:
            #Accessing the purchases table in the database
            purchases = db.query(Purchase).filter(Purchase.buyer_id == self.user.id).all()

            if not purchases:
                print("You have no past purchases.")
                return

            #Displaying previous purchases
            print("")
            print("*** Your Purchase History ***")
            for p in purchases:
                listing = db.query(Listing).get(p.listing_id)
                provider = listing.provider

                print("")
                print(f"Type: {listing.type}")
                print(f"Category: {listing.category}")
                print(f"Qty bought: {p.quantity} kg")
                print(f"Location: {listing.location}")
                print(f"Time: {p.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

        finally:
            db.close()
