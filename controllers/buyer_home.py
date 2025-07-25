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
        while True:
            try:
                print("Browsing waste...")
                print("")
                print("*** Waste Category ***")
                print("1. Organic ")
                print("2. Inorganic")

                category_selection = int(input("Enter waste category [1-2]: "))

                if category_selection == 1:
                    print("Organic selected...")
                    print("")
                    print("*** Waste Types Avaliable ***")
                    print("1. Food waste")
                    print("2. Animal waste")
                    print("3. Yard waste")

                    type_selection = int(input("Enter waste type [1-3]: "))
                    waste_types = {
                        1: "Food waste",
                        2: "Animal waste",
                        3: "Yard waste"
                    }

                    if type_selection in waste_types:
                        print("")
                        print(f"{waste_types[type_selection]} selected...")

                        qty = float(input("Enter quantity (in kg): "))
                        location = input("Enter pickup location: ")

                        return {
                            "category": "Organic",
                            "type": waste_types[type_selection],
                            "quantity": qty,
                            "location": location
                        }
                    else:
                        print("Invalid waste type. Please try again.")


                elif category_selection == 2:
                    print("Inorganic selected...")
                    break
                else:
                    print("Invalid numeric entry.")
            except ValueError:
                print("Invalid entry. Please try again!")

    def view_history(self):
        print("Viewing purchase history...")
