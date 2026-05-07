from data_loader import DataLoader, Pipeline
from app_controller import AppController
from menu_view import MenuView
from database_manager import DatabaseManager

def main():
    dataset_loader = DataLoader(
        dataset="thedevastator/the-united-states-national-parks",
        save_path="data/raw"
        )

    db_manager = DatabaseManager()
    pipeline = Pipeline(data_handler=dataset_loader, db_manager=db_manager)
    menu = MenuView()
    db_manager.create_tables()

    app = AppController(menu, db_manager)

    pipeline.run("national_park", "data/raw/df_2.csv")
    app.run(['1', '2', '3', '4'])

if __name__ == "__main__":
    main()
