#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from relationship_state import State
from relationship_city import Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    fet = session.query(State).order_by(State.id)

    for state in fet:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".fromat(city.id, city.name))
    session.commit()
    session.close()
