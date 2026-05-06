from sqlalchemy import Column, String, ForeignKey, Float, Integer
from database_manager import Base

class Trail(Base):
    __tablename__ = "trail"

    id = Column(Integer, nullable=False, unique=True)
    trail_name = Column(String, primary_key=True)
    park_id = Column(Integer, ForeignKey("park.id"), primary_key=True)
    length_miles = Column(Float, nullable=False)
    difficulty = Column(String, nullable=False)