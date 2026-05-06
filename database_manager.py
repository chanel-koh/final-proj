from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DatabaseManager:
    """
    Handles interactions between the app and the database.
    """
    def __init__(self, engine):
        self.engine = engine

    def create_tables(self):
        """
        Creates all tables specified in the models folder.
        """
        Base.metadata.create_all(self.engine)
        
