class MenuView:
    def display_menu(self):
        print("\n--- Main Menu ---")
        print("1. Add User")
        print("2. View Parks")
        print("3. View Trails")
        print("4. Exit")

    def get_choice(self, valid_choices):
        while True:
            choice = input("Enter choice: ").strip()

            if choice in valid_choices:
                return choice
            
            print(f"Invalid choice. Choose from: {', '.join(valid_choices)}")

    