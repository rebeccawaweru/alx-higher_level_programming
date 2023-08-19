#!/usr/bin/python3
"""Script that list all City Objects from database"""
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
    stmt = session.query(City).order_by(City.id)
    for x in stmt:
        print("{:d}: {:s} -> {:s}".format(x.id, x.name, x.state.name))
    session.close()
