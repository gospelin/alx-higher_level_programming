#!/usr/bin/python3
"""
Script to Update object in database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import text

if __name__ == '__main__':

    # Connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Update the State object in the database
    states = session.query(State).get(2)
    states.name = "New Mexico"
    session.add(states)
    session.commit()

    # Output Query
    states = session.query(State)

    # Print the new state's id
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
