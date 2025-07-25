from models.database import SessionLocal
from models.user import User

"""class User(Base):
    def __init__(self, email, password, role, **info):
        self.email = email
        self.password = password
        self.role = role
        self.info = info

    def home(self):
        print(f"\n Welcome to the {self.role.capitalize()} Home Page!")"""



class AuthSystem:
    def __init__(self):
        self.db = SessionLocal()

    def start(self):
        print("")
        print("AuthSystem.start() called")
        print("Prompting for email...")

        print("Welcome to the EcoWaste CLI App")
        email = input("Enter your email: ").strip()

        if self.user_exists(email):
            return self.login(email)
        else:
            return self.signup(email)


    def user_exists(self, email):
        return self.db.query(User).filter(User.email == email).first() is not None


    def login(self, email):
        user = self.db.query(User).filter(User.email == email).first()

        if not user:
            print("No user found with that email.")
            return None

        password = input("Enter your password: ").strip()

        if password == user.password:
            print("Login successful.")
            user.home()
            return user
        else:
            print("Incorrect password. Please try again.")
            return None

    def signup(self,email):
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
            password = input("Create password: ").strip()


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

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        print("Account created successfuly")
        user.home()
        return user
