# from sqlalchemy import create_engine, ForeignKey, column, String, Integer, CHAR
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssb = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname',String)
    lastname = Column('lastname',String)






