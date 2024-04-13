#!/usr/bin/python3
"""list all State objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    places = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id.asc()).all()
    for state, city in places:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
