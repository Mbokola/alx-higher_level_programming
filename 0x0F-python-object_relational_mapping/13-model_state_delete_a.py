#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
localhost/{sys.argv[3]}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_del = session.query(State).filter(State.name.like('%a%'))
    for state in states_del:
        session.delete(state)
    session.commit()  # QA review this when inside for loop
    session.close()
