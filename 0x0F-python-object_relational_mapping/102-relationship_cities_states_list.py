#!/usr/bin/python3
"""Query each State and all citites linked to it
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    CityStates = session.query(City).order_by(City.id.asc()).all()
    for city in CityStates:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
