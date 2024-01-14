#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa """

from sqlalchemy import Column, Integer, String
from relationship_city import Base
from sqlalchemy.orm import relationship


class State(Base):
    """CLASS """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
