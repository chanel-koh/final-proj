from sqlalchemy.orm import DeclarativeBase, sessionmaker
from local_settings import PostgresConfig as settings
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class DatabaseManager:
    """
    Handles interactions between the app and the database.
    """
    def __init__(self):
        self.engine = self._create_engine(settings.user, settings.passwd, settings.host, settings.port, settings.db)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def _create_engine(self, user: str, passwd: str, host: str, port: int, db: str):
        """
        Creates a db connection with SQLALchemy with user defined pool size (persistent connections kept open).
        """
        url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"

        if not database_exists(url):
            create_database(url)
        
        engine = create_engine(url, pool_size=15, echo=False)

        return engine
    
    def get_session(self):
        """
        Gets the current session.
        """
        return self.SessionLocal
    
    def create_tables(self):
        """
        Creates all tables specified in the models folder.
        """
        from models.user import User
        from models.park import Park
        from models.trail import Trail
        from models.associations import visited_parks, completed_trails

        Base.metadata.create_all(self.engine)
        
