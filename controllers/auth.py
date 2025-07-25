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

class AuthSystem:
    def __init__(self):
        self.user = {}

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
        print("")
        print("\n 🌱 Welcome to the EcoWaste CLI App")

        while True: # Error handling 
            email = input("Enter your email: ").strip().lower()
            if not self.is_valid_email(email):
                print("❌ Invalid email format. Please try again.")
                continue
            break

        if self.user_exsits(email):
            return self.login(email)
        else:
            return self.signup(email)


    def user_exsits(self, email):
        return email in self.user


    def login(self, email):
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

    def signup(self,email):
        if self.user_exists(email):
            print("⚠️ An account with this email already exsits.")
            return None
        
        print(" No account found. Let's create one.")
        print("")
        print("Are you signing up as:")
        print("1. Buyer")
        print("2. Provider")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            role = "Buyer"
            print("")
            company_name = input("Comapny Name: ").strip()
            location = input("Location: ").strip()
            company_domain = input("Company Domain: ").strip()
            password = input("Create password: ").strip()


            user = User(
                email = email,
                password = password,
                role= role,
                company_name = company_name,
                location = location,
                company_domain =company_domain
            )

        elif choice == "2":
            role = "Provider"
            print("")
            name = input("Your Name: ").strip()
            location = input("Location: ").strip()

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
                password = password,
                role = role,
                name = name,
                location = location
            )
        
        else:
            print("Invalid selection. Signup aborted.")
            return None

        self.user[email] = user
        print("Account created successfuly")
        user.home()
        return user
