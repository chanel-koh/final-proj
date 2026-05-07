from sqlalchemy import Column, String, ForeignKey, Integer, Identity
from sqlalchemy.orm import relationship
from models.associations import completed_trails
from database_manager import Base

class Trail(Base):
    __tablename__ = "trail"

    id = Column(Integer, Identity(start=1), nullable=False, unique=True)
    trail_name = Column(String, primary_key=True)
    park_id = Column(Integer, ForeignKey("park.id"), primary_key=True)
    difficulty = Column(String, nullable=False)

    park = relationship("Park", back_populates="trails")
    users = relationship("User", secondary=completed_trails, back_populates="trails")