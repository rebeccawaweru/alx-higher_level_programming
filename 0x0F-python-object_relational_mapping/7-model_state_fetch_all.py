#!/usr/bin/python3
"""Script that lists all State objects from
the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stat = session.query(State).order_by(asc(State.id)).all()

    for x in stat:
        print("{:d}: {:s}".format(x.id, x.name))

    session.close()
