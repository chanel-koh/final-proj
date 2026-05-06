from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

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
        from models.user import User
        from models.park import Park
        from models.trail import Trail
        from models.associations import visited_parks, completed_trails

        Base.metadata.create_all(self.engine)
        
