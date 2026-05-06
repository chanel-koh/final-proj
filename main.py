from data_manager import DataManager, Pipeline

def main():
    dataset_manager = DataManager(
        dataset="thedevastator/the-united-states-national-parks",
        save_path="data/raw"
        )

    pipeline = Pipeline(
        data_handler=dataset_manager,
        db_url="sqlite:///park_n_trail.db"
    )

    pipeline.run("NationalPark")

if __name__ == "__main__":
    main()
