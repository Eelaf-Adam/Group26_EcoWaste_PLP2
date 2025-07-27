from utils.security import hash_password, verify_password
from models.database import SessionLocal
from models.user import User

class AuthSystem:

    #Connects the user information to the database
    def __init__(self):
        self.db = SessionLocal()

    def start(self):
        """
        Function prompts the user for email information and
        syncs it to the database
        """
        print("")

        print("Welcome to the EcoWaste CLI App")
        email = input("Enter your email: ").strip()

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
            print("Login successful.")
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
            company_name = input("Comapny Name: ").strip()
            location = input("Location: ").strip()
            company_domain = input("Company Domain: ").strip()
            password = input("Create password: ").strip()
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
            name = input("Your Name: ").strip()
            location = input("Location: ").strip()
            password = input("Create password: ").strip()
            hashed_password = hash_password(password)


            user = User(
                email = email,
                password = hashed_password,
                role = role,
                name = name,
                location = location
            )

        else:
            print("Invalid selection. Signup aborted.")
            return None

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        print("Account created successfuly")
        user.home()
        return user
