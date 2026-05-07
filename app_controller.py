class AppController:
    """
    Manages user activity navigation.
    """
    def __init__(self, menu):
        self.menu = menu

    def run(self, valid_choices):
        """
        Displays main menu and handles submenu activity.
        """
        while True:
            self.menu.main_menu()
            choice = self.menu.get_choice(valid_choices)

            if choice == "1":
                self.menu.user_menu()

            elif choice == "2":
                self.menu.park_menu()

            elif choice == "3":
                self.menu.trail_menu()

            elif choice == "4":
                print("\nGoodbye, enjoy the parks out there!\n")
                break

