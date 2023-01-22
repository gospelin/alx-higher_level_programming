#!/usr/bin/python3
"""
List the first State object from Database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(
    f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
    pool_pre_ping=True
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).first()

print(f"{states.id}: {states.name}")

session.close()
