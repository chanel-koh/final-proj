class MenuView:
    def main_menu(self):
        """
        Displays the main app menu.
        """
        print("\n--- Main Menu ---")
        print("1. User Management")
        print("2. Parks")
        print("3. Trails")
        print("4. Exit")

    def get_choice(self, valid_choices):
        """
        Gets a menu choice from a user.
        """
        while True:
            choice = input("Enter choice: ").strip()

            if choice in valid_choices:
                return choice
            
            print(f"Invalid choice. Choose from: {', '.join(valid_choices)}")
    
    def user_menu(self):
        """ 
        Displays and executes user menu options.
        """
        while True:
            print("\n--- User Menu ---")
            print("1. Create user")
            print("2. View users")
            print("3. Set active user")
            print("4. Back")

            choice = self.get_choice(["1", "2", "3", "4"])

            if choice == "1":
                continue
            if choice == "2":
                continue
            if choice == "3":
                continue
            if choice == "4":
                break

    def park_menu(self):
        """ 
        Displays and executes park menu options.
        """
        while True:
            print("\n--- Park Menu ---")
            print("1. Add Visited Park")
            print("2. View Visited Parks")
            print("3. View Unvisited Parks")
            print("4. See Park Description")
            print("5. Back")

            choice = self.get_choice(["1", "2", "3", "4", "5"])

            if choice == "1":
                continue
            if choice == "2":
                continue
            if choice == "3":
                continue
            if choice == "4":
                continue
            if choice == "5":
                break

    def trail_menu(self):
        """ 
        Displays and executes trail menu options.
        """
        while True:
            print("\n--- Trail Menu ---")
            print("1. Add Visited Trail")
            print("2. View Visited Trails")
            print("3. Back")

            choice = self.get_choice(["1", "2", "3"])

            if choice == "1":
                continue
            if choice == "2":
                continue
            if choice == "3":
                break

    