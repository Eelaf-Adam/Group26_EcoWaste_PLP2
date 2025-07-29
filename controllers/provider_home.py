<<<<<<< HEAD
# This files provides the logic for the provider menue featuers 
=======
import re
from models.database import SessionLocal
from models.listings import Listing

>>>>>>> Leon2-branch

class ProviderMenu:
    def __init__(self, user):
        self.user = user
        self.listing = [] # For listing storage (to keep track of what the provider has listed)

    def notify_sold_out(self):
        db = SessionLocal()
        sold_out_listings = db.query(Listing).filter(
            Listing.provider_id == self.user.id,
            Listing.quantity == 0
        ).all()
        db.close()

        if sold_out_listings:
            print("⚠️  You have sold-out listings! Consider restocking.")
            for l in sold_out_listings:
                print(f"- {l.type} at {l.location}")

    def show(self):

        self.notify_sold_out()

        """
         This function displays the provider menu
        when called upon and prompts user to
        select next action
        """

        while True:
            print("\n Provider Menu")
            print("1. Add new waste")
            print("2. View my listings")
            print("3. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
               listing = self.add_waste()
               if listing:
                   self.listing.append(listing)
                   print("Waste successfully listed")
            elif choice == "2":
                self.view_listings()
            elif choice == "3":
                print("Logging out..")
                break
            else:
<<<<<<< HEAD
                print("Invalid choice. Please enter 1,2, or 3.")
=======
                print("❌ Invalid choice. Please try again.")

>>>>>>> Leon2-branch

    def add_waste(self):

        """
        This function displays the waste categories
        once user selects add new waste and corresponding
        prompts to input desired quantity and pickup location
        """

        #Connects to the database to save information entered by user
        db = SessionLocal()
        try:
                print("")
                print("*** Waste Category ***")
                print("1. Organic")
                print("2. Inorganic")
                print("3. Exit to main menu")

                waste_category = int(input("Enter waste category [1-3]: "))
                if not waste_category.isdigit() or int(waste_category) not in [1, 2, 3]:
                    print(" Invalid input. Please enter 1, 2, or 3.")
                    continue

                waste_category = int(waste_category)

                if waste_category == 3:
                    print(" Returing to main menu...")
                    return None 
                
                category_name = "Organic" if waste_category == 1 else "Inorganic"

                wate_types = {
                    1: "Food waste" if waste_category == 1 else "Plastic waste",
                    2: "Animal wate" if waste_category == 1 else "Metal Waste",
                    3: "Yard waste" if waste_category == 1 else "Glass waste"
                }

                print(f"\n {category_name} Waste Types:")
                for key, value in waste_types.items():
                    print(f"{key}. {value}")

<<<<<<< HEAD
                type_selection = input("Enter waste type [1-3]:").strip()
                if not type_selection.isdigit() or int(type_selection) not in waste_types:
                    print("Invalid type selection. Try again.")
                    continue

                selected_type = waste_types[int(type_selection)]

                # Quantity 
                qty_input = input("Enter quantity (in kg):").strip()
                try:
                    qty = float(qty_input)
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue
                except ValueError:
                    print("Quantity must be a valid number.")
                    continue
=======
                        while True:
                            try:
                                qty = float(input("Enter quantity (in kg): "))
                                if qty <= 0:
                                    print("❌ Quantity must be greater than 0.")
                                else:
                                    break
                            except ValueError:
                                print("❌ Please enter a valid number.")

                        location = input("Enter location: ")
                        #print("✅ Order successfully listed!")

                        #Error handling for invalid location
                        if not re.match(r"^[a-zA-Z\s-]+$", location):
                            print("❌ Location must only contain letters.")
                            return


                        new_listing = Listing(
                            provider_id = self.user.id,
                            category = "Organic",
                            type = waste_types[type_selection],
                            quantity = qty,
                            location = location
                        )
                        db.add(new_listing)
                        db.commit()

                        print("✅ Listing successfully added!")
                        return

                    else:
                        print("❌ Invalid waste type. Please try again!")
>>>>>>> Leon2-branch

                #Location 
                location = input("Enter pickup location:").strip()
                if not location.replace("","").isalpha():
                    print("Location must only contain letters.")
                    continue

                return{
                    "Category": category_name,
                    "Type": selected_type,
                    "Quantity (kg)": qty,
                    "Location": location 
                }
            
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

<<<<<<< HEAD
    def view_listing(self):
        print("\n Your Waste Listing:")
        if not self.listing:
                print("You have not listed any waste yet.")
                return 
        
        for i, listing in enumerate(self.listing, 1):
                print(f"{i}. {listing['Category']} - {listing['Type']}, {listing['Quantity (kg)']}kg@ {listing['Location']}")
               
               
=======
                    waste_types = {
                        1: "Plastic waste",
                        2: "Metal waste",
                        3: "Glass waste"
                    }

                    if type_selection in waste_types:
                        print(f"{waste_types[type_selection]} selected ....")

                        while True:
                            try:
                                qty = float(input("Enter quantity (in kg): "))
                                if qty <= 0:
                                    print("❌ Quantity must be greater than 0.")
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid number.")

                        location = input("Enter pickup location: ")

                        if not re.match(r"^[a-zA-Z\s-]+$", location):
                            print("❌ Location must only contain letters.")
                            return

                        new_listing = Listing(
                            provider_id = self.user.id,
                            category = "Inorganic",
                            type = waste_types[type_selection],
                            quantity = qty,
                            location = location
                        )
                        db.add(new_listing)
                        db.commit()

                        print("✅ Listing successfully added!")
                        return

                elif waste_category == 3:
                    print("Exiting...")
                    return

                else:
                    print("❌ Invalid entry. Please try again!")


        except ValueError:
            print("❌ Invalid choice. Please try again!")

    def view_listings(self):

        """
        This function displays previous order history
        of the user stored in the database when called
        upon
        """

        #Accessing the database
        db = SessionLocal()
        listings = db.query(Listing).filter(Listing.provider_id == self.user.id).all()

        if not listings:
            print("")
            print("No listings found.")
            return

        for l in listings:
            print("")
            print("Your listings.")
            print(f"Type: {l.type}")
            print(f"Category: {l.category}")
            print(f"Qty: {l.quantity} kg")
            print(f"Location: {l.location}")

            if l.quantity == 0:
                print("⚠️  This listing is fully sold out!")
        db.close()
>>>>>>> Leon2-branch
