# This files provides the logic for the provider menue featuers 

class ProviderMenu:
    def __init__(self, user):
        self.user = user
        self.listing = [] # For listing storage (to keep track of what the provider has listed)

    def show(self):
        while True:
            print("\n Provider Menu")
            print("1. Add new wate")
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
                print("Invalid choice. Please enter 1,2, or 3.")

    def add_waste(self):
        while True:
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

    def view_listing(self):
        print("\n Your Waste Listing:")
        if not self.listing:
                print("You have not listed any waste yet.")
                return 
        
        for i, listing in enumerate(self.listing, 1):
                print(f"{i}. {listing['Category']} - {listing['Type']}, {listing['Quantity (kg)']}kg@ {listing['Location']}")
               
               