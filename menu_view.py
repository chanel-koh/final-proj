from sqlalchemy import select
from models.park import Park
from models.associations import visited_parks

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
                print("Heading back to main menu!")
                break

    def park_menu(self, active_user, db_manager):
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

            with db_manager.SessionLocal() as session:

                active_user = session.merge(active_user)

                choice = self.get_choice(["1", "2", "3", "4", "5"])

                if choice == "1":
                    term = input("\nSearch for a park: ")
                    results = session.query(Park).filter(Park.park_name.ilike(f"%{term}%")).all()

                    if not results:
                        print("No parks found.")
                        return

                    print()
                    for i, park in enumerate(results):
                        print(f"{i + 1}. {park.park_name} ({park.us_state})")

                    choice = int(input("Select a park by number: ")) - 1

                    selected_park = results[choice]
                    active_user.visited_parks.append(selected_park)
                    session.commit()

                if choice == "2":
                    results = (
                        session.query(visited_parks, Park)
                        .join(Park, visited_parks.c.park_id == Park.id)
                        .filter(visited_parks.c.username == active_user.username)
                        .all()
                    )
                    
                    print("\n--- Visited Parks ---")
                    for _, _, visit_date, park in results:
                        print(f"{park.park_name} ({park.us_state}) - Visited on {visit_date}")

                if choice == "3":
                    results = (
                        session.query(Park)
                        .outerjoin(visited_parks, 
                                   (Park.id == visited_parks.c.park_id) &
                                   (visited_parks.c.username == active_user.username)
                        )
                        .filter(visited_parks.c.park_id.is_(None))
                        .all()
                    )

                    print("\n--- Unvisited Parks ---")
                    for park in results:
                        print(f"{park.park_name}")

                if choice == "4":
                    term = input("\nSearch for a park: ")
                    results = session.query(Park).filter(Park.park_name.ilike(f"%{term}%")).all()

                    if not results:
                        print("No parks found.")
                        return

                    print()
                    for i, park in enumerate(results):
                        print(f"{i + 1}. {park.park_name} ({park.us_state})")

                    choice = int(input("Select a park by number: ")) - 1

                    selected_park = results[choice]
                    print(f"\n{selected_park.park_name} ({selected_park.us_state})")
                    print(f"Description: {selected_park.description}")

                if choice == "5":
                    print("\nHeading back to main menu!")
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
                print("Heading back to main menu!")
                break

    