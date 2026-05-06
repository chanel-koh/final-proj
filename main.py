from data_loader import DataLoader, Pipeline
from app_controller import AppController
from menu_view import MenuView
from database_manager import DatabaseManager
from local_settings import PostgresConfig as settings

def main():
    dataset_loader = DataLoader(
        dataset="thedevastator/the-united-states-national-parks",
        save_path="data/raw"
        )

    pipeline = Pipeline(data_handler=dataset_loader)
    engine = pipeline.get_engine(settings.user, settings.passwd, settings.host, settings.port, settings.db)

    menu = MenuView()
    database_manager = DatabaseManager(engine)

    app = AppController(menu, database_manager)

    pipeline.run("NationalPark", "data/raw/df_2.csv")
    app.run(['1', '2', '3', '4'])

if __name__ == "__main__":
    main()
