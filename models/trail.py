from sqlalchemy import Column, String, ForeignKey, Float
from database_manager import Base

class Trail(Base):
    __tablename__ = "trail"

    trail_name = Column(String, primary_key=True)
    park_name = Column(String, ForeignKey("park.park_name"), primary_key=True)
    length_miles = Column(Float, nullable=False)
    difficulty = Column(String, nullable=False)