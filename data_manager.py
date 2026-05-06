from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings

class DataManager:
    def __init__(self, dataset: str, save_path: str) -> None:
        """
        Initializes a dataset to load.

        Params
            dataset : str, the dataset to download 
                Notes: from Kaggle and in the form owner/dataset_name
            save_path: str, path to download the dataset to
            file_name: str, the name to call the saved dataset
        """
        self.dataset = dataset
        self.save_path = save_path

    def download(self) -> None:
        """
        Downloads a dataset from Kaggle.
        """
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(
            self.dataset,
            path=self.save_path,
            unzip=True
        )

    def load_and_clean(self) -> pd.DataFrame:
        """
        Loads the dataset into a dataframe, then performs preliminary cleaning by removing column 
        whitespace and any duplicate rows.
        """
        df = pd.read_csv("data/df_2.csv")

        df = df.drop_duplicates()
        df.columns = [c.lower().strip for c in df.columns]

        df = df[["id", "name", "location", "description"]]
        df[["state", "coords"]] = df["raw"].str.extract(r"^([A-Za-z\s]+)(.*)$")
        df = df.drop(columns=["location"])

        return df
    
class Pipeline:
    def __init__(self, data_handler: DataManager, db_url: str):
        self.data_handler = data_handler
        self.engine = create_engine(db_url)

    def run(self, table_name: str) -> None:
        self.data_handler.download()
        df = self.data_handler.load_and_clean()
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)
