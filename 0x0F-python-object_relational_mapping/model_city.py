#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """CLASS """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    tate_id = Column(Integer, ForeignKey('states.id'), nullable=False)
