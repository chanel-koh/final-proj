from sqlalchemy import text

class DatabaseManager:
    def __init__(self, engine):
        self.engine = engine

    def get_parks(self):
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM parks_n_trails"))
            return result.fetchall()
        
    ## more actions to be added 