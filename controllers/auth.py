from utils.security import hash_password, verify_password
from models.database import SessionLocal
from models.user import User
import re

class AuthSystem:

    #Connects the user information to the database
    def __init__(self):
        self.db = SessionLocal()

    def is_valid_email(self, email):
        #This verifies if the email is valid
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def get_valid_password(self):
        while True:
            password = input("Create password (min 8 characters): ").strip()

            if len(password) < 8:
                print("Password too short. Must be atleast 8 characters")
            else:
                return password

    def get_valid_input(self, prompt_text, min_length=4):
        pattern = r"^[a-zA-Z\s-]+$"

        while True:
            value = input(prompt_text).strip()

            if len(value) < min_length :
                print("❌ Invalid entry. Please try again.")
            elif not re.match(pattern, value):
                print("❌ Input must only contain letters.")
            else:
                return value

    def prompt_company_domain(self):
        print("Choose your company domain: ")
        print("1. waste-solutions")
        print("2. greenloop")
        print("3. ecoinnovators.africa")
        print("4. Other")

        domain_options = {
            "1": "waste-solutions",
            "2": "greenloop",
            "3": "ecoinnovators.africa"
        }
        while True:
            choice = input("Enter your choice [1-4]: ").strip()
            if choice in domain_options:
                return domain_options[choice]
            elif choice == "4":
                custom = input("Enter your custom domain (e.g cleantech.io): ").strip()
                if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', custom):
                    return custom
                else:
                    print("❌ Invalid domain format. Try again.")

            else:
                print("❌ Invalid selection. Please choose 1-4.")

    def start(self):
        while True:
            """
            Function prompts the user for email information and
            syncs it to the database
            """
            print("")

            print("Welcome to the EcoWaste CLI App")
            email = input("Enter your email: ").strip()

            if not self.is_valid_email(email):
                print("❌ Invalid email. Please try again.")
                continue

            if self.user_exists(email):
                return self.login(email)
            else:
                return self.signup(email)



    #Function checks if the user account is existing or not
    def user_exists(self, email):
        return self.db.query(User).filter(User.email == email).first() is not None


    #Function ensures the username and password match before proceeding
    def login(self, email):
        user = self.db.query(User).filter(User.email == email).first()

        if not user:
            print("No user found with that email.")
            return None

        password = input("Enter your password: ").strip()

        if verify_password(password, user.password):
            print("✅ Login successful.")
            print("")
            user.home()
            return user
        else:
            print("Incorrect password. Please try again")
            return None


    def signup(self,email):

        """
        Function prompts the user to select their user type
        and enter the respective corresponding information
        """

        print(" No account found. Let's create one.")
        print("")
        print("Are you signing up as? ")
        print("1. Buyer")
        print("2. Provider")
        choice = input("Enter [1-2]: ").strip()


        if choice == "1":
            role = "Buyer"
            print("")
            company_name = self.get_valid_input("Company Name: ")
            location = self.get_valid_input("Location: ")
            print("")
            company_domain = self.prompt_company_domain()
            password = self.get_valid_password()
            hashed_password = hash_password(password)


            user = User(
                email = email,
                password = hashed_password,
                role= role,
                company_name = company_name,
                location = location,
                company_domain =company_domain
            )

        elif choice == "2":
            role = "Provider"
            print("")
            name = self.get_valid_input("Your Name: ")
            location = self.get_valid_input("Location: ")
            password = self.get_valid_password()
            hashed_password = hash_password(password)


            user = User(
                email = email,
                password = hashed_password,
                role = role,
                name = name,
                location = location
            )

        else:
            print("❌ Invalid selection. Signup aborted.")
            return None

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        print("✅ Account created successfuly")
        user.home()
        return user
