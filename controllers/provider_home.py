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
        while True:
            try:
                print("")
                print("*** Waste Category ***")
                print("1. Organic")
                print("2. Inorganic")
                print("3. Exit to main menu")

                waste_category = int(input("Enter waste category [1-3]: "))

                if waste_category == 1:
                    print("Organic waste selected....")
                    print("")
                    print("*** Waste Type ***")
                    print("1. Food waste")
                    print("2. Animal waste")
                    print("3. Yard waste")

                    type_selection = int(input("Enter choice [1-3]: "))

                    waste_types = {
                        1: "Food waste",
                        2: "Animal waste",
                        3: "Yard waste"
                    }

                    if type_selection in waste_types:
                        print(f"{waste_types[type_selection]} selected ...")

                        qty = float(input("Enter quantity: "))
                        location = input("Enter location: ")
                        print("Order successfully listed!")

                        if location.isalpha():
                            return {
                                "Category": "Organic",
                                "type": waste_types[type_selection],
                                "quantity": qty,
                                "location": location
                            }
                        else:
                            print("Invalid entry. Please try again!")

                    else:
                        print("Invalid waste type. Please try again!")

                elif waste_category == 2:
                    print("Inorganic waste selected...")
                    print("")
                    print("*** Waste Type ***")
                    print("1. Plastic waste")
                    print("2. Metal waste")
                    print("3. Glass waste")

                    type_selection = int(input("Enter waste type [1-3]: "))

                    waste_types = {
                        1: "Plastic waste",
                        2: "Metal waste",
                        3: "Glass waste"
                    }

                    if type_selection in waste_types:
                        print(f"{waste_types[type_selection]} selected ....")

                        qty = float(input("Enter quantity (in kg): "))
                        location = input("Enter pickup location: ")

                        if location.isalpha():
                            return {
                                "Category": "Inorganic",
                                "type": waste_types[type_selection],
                                "quantity": qty,
                                "location": location
                            }
                        else:
                            print("Invalid entry. Please try again!")

                    elif waste_category == 3:
                        print("Exiting...")
                        return

                    else:
                        print("Invalid entry. Please try again!")


            except ValueError:
                print("Invalid choice. Please try again!")

    def view_listings(self):
        print(" (Placeholder) Viewing your listings...")
