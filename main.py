from data_loader import DataLoader, Pipeline

def main():
    dataset_manager = DataLoader(
        dataset="thedevastator/the-united-states-national-parks",
        save_path="data/raw"
        )

    pipeline = Pipeline(
        data_handler=dataset_manager,
    )

    pipeline.run("NationalPark", "data/raw/df_2.csv")

if __name__ == "__main__":
    main()
