#!/usr/bin/python3
"""
Script that prints the state object with the name passed
as argument from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
