from controllers.auth import AuthSystem
from controllers.buyer_home import BuyerMenu
from controllers.provider_home import ProviderMenu

import shutil 

def logo_and_slagon ():
    ascii_art = r"""

    _____       __        __        _       
    | ____|___ __\ \      / /_ _ ___| |_ ___ 
    |  _| / __/ _ \ \ /\ / / _` / __| __/ _ \
    | |__| (_| (_) \ V  V / (_| \__ \ ||  __/
    |_____\___\___/ \_/\_/ \__,_|___/\__\___|
        


            ♻️ Your Top Choice Recycling App ♻️
        "Fighting Climate Change, One Action at a Time."
    """
    # Get terminal width 
    terminal_width = shutil.get_terminal_size().columns 

    # Print each line centered 
    for line in ascii_art.strip("\n").split("\n"):
        print(line.center(terminal_width))

# Calling 
logo_and_slagon()

class EcoWasteApp:
    def __init__(self):
        self.auth = AuthSystem()
        self.user = None

    def run(self):
        self.user = self.auth.start()

        if not self.user:
            print(" Exiting app.")
            return

        self.route_user()


    def route_user(self):
        if self.user.role == "Buyer":
            BuyerMenu(self.user).show()
        elif self.user.role == "Provider":
            ProviderMenu(self.user).show()
        else:
            print("Unknown user role.")

if __name__ == "__main__":
    app = EcoWasteApp()
    app.run()
