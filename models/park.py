from sqlalchemy import Column, String, Integer, Identity
from sqlalchemy.orm import relationship
from models.associations import visited_parks
from database_manager import Base

class Park(Base):
    __tablename__ = "park"

    id = Column(Integer, Identity(), nullable=False, unique=True)
    park_name = Column(String, primary_key=True)
    us_state = Column(String, primary_key=True)
    description = Column(String, nullable=False)

    trails = relationship("Trail", back_populates="park")
    visitors = relationship("User", secondary=visited_parks, back_populates="visited_parks")