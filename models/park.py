from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database_manager import Base

class Park(Base):
    __tablename__ = "park"

    id = Column(Integer, nullable=False, unique=True)
    park_name = Column(String, primary_key=True)
    us_state = Column(String, primary_key=True)
    description = Column(String, nullable=False)

    trails = relationship("Trail", back_populates="park")