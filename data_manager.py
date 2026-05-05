from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from sqlalchemy import create_engine

class DataManager:
    def __init__(self, dataset: str, save_path: str, file_name: str) -> None:
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
        self.file_path = f"{save_path}/{file_name}"

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
        df = pd.read_csv(self.file_path)
        df = df.drop_duplicates()
        df.columns = [c.lower().strip for c in df.columns]
        return df
    
    class Pipeline:
        def __init__(self, data_handler: DataManager, db_url: str):
            self.data_handler = data_handler
            self.engine = create_engine(db_url)

        def run(self, table_name: str) -> None:
            self.data_handler.download()
            df = self.data_handler.load_and_clean()
            df.to_sql(table_name, self.engine, if_exists="replace", index=False)
