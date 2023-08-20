#!/usr/bin/python3
""" model_state module """

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """ State class """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
