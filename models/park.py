from sqlalchemy import Column, String, Date
from database_manager import Base

class Park(Base):
    __tablename__ = "park"

    park_name = Column(String, primary_key=True)
    us_state = Column(String, primary_key=True)
    description = Column(Date, nullable=False)