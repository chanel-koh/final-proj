from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from models.associations import visited_parks
from database_manager import Base
from datetime import date

class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    date_joined = Column(Date, nullable=False, default=date.today)

    visited_parks = relationship("Park", secondary=visited_parks, back_populates="visitors")