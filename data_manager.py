from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import PostgresConfig as settings
import os

class DataManager:
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
    def __init__(self, data_handler: DataManager):
        self.data_handler = data_handler
        self.engine = self.get_engine_config_from_settings()

    
    def get_engine(self, user: str, passwd: str, host: str, port: int, db: str):
        """
        Creates a db connection with SQLALchemy with user defined pool size (persistent connections kept open).
        """
        url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"

        if not database_exists(url):
            create_database(url)
        
        engine = create_engine(url, pool_size=15, echo=False)

        return engine
    
    def get_engine_config_from_settings(self):
        """
        Gets config information from local settings file to establish db connection.
        """
        
        return self.get_engine(settings.user, settings.passwd, settings.host, settings.port, settings.db)
    
    def get_session(self):
        """
        Gets current db session.
        """
        Session = sessionmaker(bind=self.engine)
        return Session

    def run(self, table_name: str, datafile_path: str) -> None:
        """
        Runs the full data seeding pipeline of downloading the external data, cleaning it, and conversion to sql.
        """
        self.data_handler.download()
        df = self.data_handler.load_and_clean(datafile_path)
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)
