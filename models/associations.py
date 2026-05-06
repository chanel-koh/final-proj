from sqlalchemy import String, Date, Integer, Table, Column, ForeignKey
from database_manager import Base
from datetime import date

visited_parks = Table(
    "visited_parks",
    Base.metadata,
    Column("username", String, ForeignKey("user.username"), primary_key=True),
    Column("park_name", String, ForeignKey("park.park_name"), primary_key=True),
    Column("visit_date", Date, nullable=False, default=date.today),
    Column("rating", Integer, nullable=False)
)

completed_trails = Table(
    "completed_trails",
    Base.metadata,
    Column("username", String, ForeignKey("user.username"), primary_key=True),
    Column("park_name", String, ForeignKey("park.park_name"), primary_key=True),
    Column("trail_name", String, ForeignKey("trail.trail_name"), primary_key=True)

)
