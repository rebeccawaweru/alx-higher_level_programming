#!/usr/bin/python3
"""script that creates the State 'California' with
the City 'San Francisco'"""
import sys
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
    stmt = State(name="California", cities=[City(name="San Francisco")])
    session.add(stmt)
    session.commit()
    session.close()
