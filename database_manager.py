import pandas as pd

class DatabaseManager:
    """
    Handles queries from user choices.
    """
    def __init__(self, engine):
        self.engine = engine

    def get_parks(self):
        query = "SELECT * FROM national_park"
        df = pd.read_sql(query, self.engine)
        return df
        
    ## more actions to be added 