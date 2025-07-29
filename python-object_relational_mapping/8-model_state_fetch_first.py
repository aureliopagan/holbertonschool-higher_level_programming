#!/usr/bin/python3
"""Prints the first State object from the `states` table."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Exit if incorrect number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py mysql_username mysql_password database_name")
        sys.exit(1)

    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Create session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
