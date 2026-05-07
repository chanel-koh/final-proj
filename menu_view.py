from sqlalchemy import select
from models.park import Park
from models.user import User
from models.trail import Trail
from models.associations import visited_parks, completed_trails

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
    
    def user_menu(self, active_user, db_manager):
        """ 
        Displays and executes user menu options.
        """
        while True:
            print("\n--- User Menu ---")
            print("1. View users")
            print("2. Set active user")
            print("3. Back")

            choice = self.get_choice(["1", "2", "3"])

            with db_manager.SessionLocal() as session:
                if choice == "1":
                    results = session.query(User).all()
                    
                    print("\n--- Users ---")
                    for user in results:
                        print(user.username)

                if choice == "2":
                    results = session.query(User).all()
                    
                    if not results:
                        print("No users found.")
                        return

                    print("\n--- Users ---")
                    for i, user in enumerate(results):
                        print(f"{i + 1}. {user.username}")

                    choice = int(input("Select a user by number: ")) - 1
                    active_user = results[choice]
                    print(f"Active user set to: {active_user.username}")

                if choice == "3":
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

    def trail_menu(self, active_user, db_manager):
        """ 
        Displays and executes trail menu options.
        """
        while True:
            print("\n--- Trail Menu ---")
            print("1. Add Visited Trail")
            print("2. View Visited Trails")
            print("3. Back")

            choice = self.get_choice(["1", "2", "3"])
            
            with db_manager.SessionLocal() as session:
                if choice == "1":
                    trail_name = input("Enter trail name: ").strip()

                    parks = session.query(Park).order_by(Park.id).all()
                    print("\n--- Park IDs ---")
                    for park in parks:
                        print(f"{park.id} | {park.park_name} ({park.us_state})")
                    park_id = int(input("Enter park id: ").strip())

                    difficulty = input("\nEnter trail difficulty (Easy, Moderate, Hard): ")
                    trail = Trail(trail_name=trail_name, park_id=park_id, difficulty=difficulty)
                    session.add(trail)
                    session.flush()

                    session.execute(
                        completed_trails.insert().values(
                            username=active_user.username,
                            park_id=park_id,
                            trail_id=trail.id
                        )
                    )
                    session.flush()
                    active_user = session.merge(active_user)
                    active_user.trails.append(trail)
                    session.commit()
                    session.refresh(trail)
                    print(f"\nCreated and visited trail: {trail.trail_name}")

                if choice == "2":
                    results = (
                            session.query(completed_trails, Trail)
                            .join(Trail, completed_trails.c.trail_id == Trail.id)
                            .filter(completed_trails.c.username == active_user.username)
                            .all()
                        )
                        
                    print("\n--- Visited Trails ---")
                    for _, trail in results:
                        print(f"{trail.trail_name} ({trail.difficulty})")

                if choice == "3":
                    print("Heading back to main menu!")
                    break

    