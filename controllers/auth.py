<<<<<<< HEAD
# This files contains the registeration process for the user of EcoWate App. It enables users to signup or login. 

import re 

class User:
    def __init__(self, email, password, role, **info):
        self.email = email
        self.password = password
        self.role = role
        self.info = info

    def home(self):
        print(f"\n Welcome to the {self.role.capitalize()} Home Page!")
=======
from utils.security import hash_password, verify_password
from models.database import SessionLocal
from models.user import User
import re
>>>>>>> Leon2-branch

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

    def is_valid_email(self, email):  # Error handling for the email input 
        # simple regex for validating user email 
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def is_valid_password(self, password): #Error handling for the password input 
        # 5 to 8 charcters, only letters and numbers
        if not (5 <= len(password) <= 8):
            return False
        return password.isalnum()
    
    def start(self):
<<<<<<< HEAD
        print("")
        print("\n 🌱 Welcome to the EcoWaste CLI App")

        while True: # Error handling 
            email = input("Enter your email: ").strip().lower()
            if not self.is_valid_email(email):
                print("❌ Invalid email format. Please try again.")
                continue
            break
=======
        while True:
            """
            Function prompts the user for email information and
            syncs it to the database
            """
            print("")
>>>>>>> Leon2-branch

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
<<<<<<< HEAD
        user = self.user[email]
        max_attempts = 3

        for attempt in range(max_attempts):
            password = input("Enter your password: ").strip()
            if password == user.password:
                print("🔐Login successful")
                user.home()
                return user
        else:
            attempts_left = max_attempts - attempt - 1
            print(f" ❌ Incorrect password. Attempts left: {attempts_left}")
            
        print(" 🚫Too many failed attempts. Login aborted.")
        return None
=======
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
>>>>>>> Leon2-branch


    def signup(self,email):
<<<<<<< HEAD
        if self.user_exists(email):
            print("⚠️ An account with this email already exsits.")
            return None
        
=======

        """
        Function prompts the user to select their user type
        and enter the respective corresponding information
        """

>>>>>>> Leon2-branch
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
<<<<<<< HEAD
            name = input("Your Name: ").strip()
            location = input("Location: ").strip()
=======
            name = self.get_valid_input("Your Name: ")
            location = self.get_valid_input("Location: ")
            password = self.get_valid_password()
            hashed_password = hash_password(password)
>>>>>>> Leon2-branch

        else:
            print("Invalid Selection. Signup aborted.")
            return None 
        
        # Password validation with confirmation 
        while True:
            password = input("Create password (5-8 chars, no symbols): ").strip()
            if not elf.is_valid_password(password):
                print("Inavlid password. Must be 5-8 letters/numbers only.")
                continue
            confirm = input("Confirm password:").strip()
            if password != confirm:
                print("Password do not match.")
                continue
            break
      

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
