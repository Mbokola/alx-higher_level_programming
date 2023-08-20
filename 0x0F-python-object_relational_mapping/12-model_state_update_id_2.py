#!/usr/bin/python3
""" 12-model_state_update_id_2 module"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
localhost/{sys.argv[3]}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    to_update = session.query(State).filter(State.id == 2).first()
    if to_update:
        to_update.name = "New Mexico"
        session.commit()

    session.close()
