#!/usr/bin/python3
"""Script that lists all State objects, and corresponding
City objects in the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).order_by(State.id)
    for x in stmt:
        print("{:d}: {:s}".format(x.id, x.name))
        for y in x.cities:
            print("\t{:d}: {:s}".format(y.id, y.name))
    session.close()
