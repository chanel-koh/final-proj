from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import os
from database_manager import DatabaseManager
from models.park import Park

class DataLoader:
    def __init__(self, dataset: str, save_path: str) -> None:
        """
        Initializes a dataset to load.

        Params
            dataset : str, the dataset to download 
                Notes: from Kaggle and in the form owner/dataset_name
            save_path: str, path to download the dataset to
        """
        self.dataset = dataset
        self.save_path = save_path

    def download(self) -> None:
        """
        Downloads a dataset from Kaggle.
        """
        api = KaggleApi()
        api.authenticate()

        os.makedirs(self.save_path, exist_ok=True)
        
        api.dataset_download_files(
            self.dataset,
            path=self.save_path,
            unzip=True
        )

    def load_and_clean(self, file_path: str) -> pd.DataFrame:
        """
        Loads the dataset into a dataframe, then performs preliminary cleaning by removing column 
        whitespace and any duplicate rows.
        """
        df = pd.read_csv(file_path)

        df = df.drop_duplicates()
        df.columns = [c.lower().strip() for c in df.columns]

        df = df[["name", "location", "description"]]
        df[["state", "coords"]] = df["location"].str.extract(r"^([A-Za-z\s]+)(.*)$")
        df = df.drop(columns=["location"])

        df = df[["name", "state", "description"]]

        return df
    
class Pipeline:
    def __init__(self, data_handler: DataLoader, db_manager: DatabaseManager):
        self.data_handler = data_handler
        self.db_manager = db_manager

    def run(self, datafile_path: str) -> None:
        """
        Runs the full data seeding pipeline of downloading the external data, cleaning it, and conversion to sql.
        """
        self.data_handler.download()
        df = self.data_handler.load_and_clean(datafile_path)
        session = self.db_manager.get_session()

        for _, row in df.iterrows():
            park = Park(
                park_name=row["name"],
                us_state=row["state"],
                description=row["description"]
            )

            existing = session.query(Park).filter_by(
            park_name=park.park_name,
            us_state=park.us_state
            ).first()

            if not existing:
                session.add(park)

            session.commit()

        session.close()
