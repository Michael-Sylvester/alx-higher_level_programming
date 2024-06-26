#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define Base instance
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
