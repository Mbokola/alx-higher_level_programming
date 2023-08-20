#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City
from model_state import State, Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
localhost/{sys.argv[3]}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_sorted_by_id = session.query(State, City).\
        join(City, State.id == City.state_id).order_by(City.id).all()
    for state, city in cities_sorted_by_id:
        print(f'{state.name}: ({city.id}) {city.name}')
