import models
from controllers.auth import AuthSystem
from controllers.buyer_home import BuyerMenu
from controllers.provider_home import ProviderMenu

import shutil

#Logo to enhance User experience
def logo_and_slogan ():
    ascii_art = r"""

    ____       __        __        _
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
logo_and_slogan()

class EcoWasteApp:

    """
    This class contains the logic that links
    all files to the database and ensures
    functionality of the program
    """

    def __init__(self):

        """
        This function accesses the AuthSystem class in
        the auth.py file that contains the logic for
        user account access and creation
        """

        self.auth = AuthSystem()
        self.user = None

    """
    This function starts the logic for user account
    creation and access
    """
    def run(self):

        """
        This function starts the logic for user
        account creation and access
        """

        self.user = self.auth.start()

        if not self.user:
            print(" Exiting app.")
            return

        self.route_user()


    def route_user(self):

        """
        This function contains the logic for user type
        selection. It links the user selection to the
        corresponding class in the specific file
        """


        if self.user.role == "Buyer":
            BuyerMenu(self.user).show()
        elif self.user.role == "Provider":
            ProviderMenu(self.user).show()
        else:
            print("Unknown user role.")



"""Runs the main file"""
if __name__ == "__main__":
    app = EcoWasteApp()
    app.run()