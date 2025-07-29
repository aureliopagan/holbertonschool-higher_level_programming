#!/usr/bin/python3
"""Links the State class to the `states` table in the database."""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Base class for all models
Base = declarative_base()


class State(Base):
    """Represents the `states` table in the database."""
    __tablename__ = 'states'

    # Column definitions for the `states` table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Exit if incorrect number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py mysql_username mysql_password database_name")
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

    # Create all tables defined in Base
    Base.metadata.create_all(engine)
