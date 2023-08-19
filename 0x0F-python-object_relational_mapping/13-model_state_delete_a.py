#!/usr/bin/python3
""""Script that delete all State objects with
a name containing the letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).filter(State.name.like("%a%"))
    r = stmt.all()
    for x in r:
        session.delete(x)
    session.commit()
    session.close()
