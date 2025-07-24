class User:
    def __init__(self, email,password,role, **info):
        self.email = email 
        self.password = password
        self.role = role
        self.info = info

    def home(self):
        print(f"\n Welcome to the {self.role.capitalize()} Home Page!")


class AuthSystem:
    def __init__(self):
        self.user = {}

    def start(self):
        print("Welcome to the EcoWaste CLI App")
        email = input("Enter your email:").strip()

        if self.user_exsists(email):
            self.login(email)
        else:
            self.signup(email)


    def user_exsits(self,email):
        user=self.user[email]
        password=input("Enter your password: ").strip()
        if password == user.password:
            print("Login is successful")
            user.home()
        else:
            print("Incorrect password. Please try again.")

    
    def signup(self,email):
        print("\n No account found. Let's create one.")
        print("Are you signing up as:")
        print("1. Buyer")
        print("2. Provider")
        choice = input("Enter 1 or 2:").strip()

        if choice == "1":
            rile = "Buyer"
            company_name = input("Comapny Name: ").strip()
            location = input("Location:").strip()
            company_domain = input("Company Domain: ").strip()
            password = input("Create password:").strip()


            user = User(
                email=email,
                password=password,
                role=role,
                company_name=company_name,
                location=location,
                company_domain=company_domain
            )

        elif choice == "2":
            role = "provider"
            name = input("Your Name:").strip()
            location = input("Location:").strip()
            password = input("Create password:").strip()


            user = User(
                email=email,
                password=password,
                role=role,
                name=name,
                location=location
            )

        else:
            print("Invalid selection. Signup aborted.")
            return
        
        self.user[email] = user 
        print("Account created successfuly")
        user.home()

if __name__ == "__main__":
    app = AuthSystem()
    app.start()