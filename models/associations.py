from sqlalchemy import String, Date, Integer, Table, Column, ForeignKey
from database_manager import Base
from datetime import date

visited_parks = Table(
    "visited_parks",
    Base.metadata,
    Column("username", String, ForeignKey("user.username"), primary_key=True),
    Column("park_id", Integer, ForeignKey("park.id"), primary_key=True),
    Column("visit_date", Date, nullable=False, default=date.today),
)

completed_trails = Table(
    "completed_trails",
    Base.metadata,
    Column("username", String, ForeignKey("user.username"), primary_key=True),
    Column("park_id", Integer, ForeignKey("park.id"), primary_key=True),
    Column("trail_id", Integer, ForeignKey("trail.id"), primary_key=True)

)
