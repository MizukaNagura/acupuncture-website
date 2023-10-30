from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AcupuncturePoint(Base):
    __tablename__ = "acupuncture_points"
    id = Column(Integer, Sequence("acupuncture_point_id_seq"), primary_key=True)
    name = Column(String)
    description = Column(String)
