class AppController:
    def __init__(self, menu, database):
        self.menu = menu
        self.database = database

    def run(self):
        while True:
            self.menu.display_menu()
            choice = self.menu.get_choice()

            if choice == "1":
                parks = self.database.get_parks()
                print(parks)

            elif choice == "2":
                ## todo
                continue

            elif choice == "3":
                break