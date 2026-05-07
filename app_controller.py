from models.user import User
from datetime import date

class AppController:
    """
    Manages user activity navigation.
    """
    def __init__(self, menu, db_manager):
        self.menu = menu
        self.db_manager = db_manager
        self.active_user = None

    def login(self):
        session = self.db_manager.SessionLocal()

        username = input("Username: ")
        user = session.query(User).filter_by(username=username).first()

        if not user:
            print("\nUser not found.")
            print("Would you like to:")
            print("1. Create new user")
            print("2. Try again")

            choice = input("Choice: ")

            if choice == "1":
                email = input("Enter email: ").strip()
                user = User(username=username, email=email, date_joined=date.today())
                session.add(user)
                session.commit()
                session.refresh(user) 
                print(f"\nCreated user: {user.username}")
            if choice == "2":
                self.login()

        self.active_user = user
        print(f"Logged in as {self.active_user.username}")

        session.close()

    def run(self, valid_choices):
        """
        Displays main menu and handles submenu activity.
        """
        self.login()

        while True:
            self.menu.main_menu()
            choice = self.menu.get_choice(valid_choices)

            if choice == "1":
                self.menu.user_menu(self.active_user, self.db_manager)

            elif choice == "2":
                self.menu.park_menu(self.active_user, self.db_manager)

            elif choice == "3":
                self.menu.trail_menu(self.active_user, self.db_manager)

            elif choice == "4":
                print("\nGoodbye, enjoy the parks out there!\n")
                break

