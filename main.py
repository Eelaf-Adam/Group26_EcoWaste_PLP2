from controllers.auth import AuthSystem 
from controllers.buyer_home import BuyerMenu
from controllers.provider_home import ProviderMenu


class EcoWasteApp:
    def __hash__(self):
        self.auth = AuthSystem()
        self.user = None

    def run(self):
        self.user = self.auth.start()

        if not self.user:
            print(" Exiting app.")
            return
        
        self.route_user()

    
    def route_user(self):
        if self.user.role == "buyer":
            BuyerMenu(self.user).show()
        elif self.user.role == "provider":
            ProviderMenu(self.user).show()
        else:
            print("Unkwon user role.")

if __name__ == "__main__":
    app = EcoWasteApp()
    app.run()
