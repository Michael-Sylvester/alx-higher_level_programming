#!/usr/bin/python3
"""list all State objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == "{}".format(sys.argv[4])).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
