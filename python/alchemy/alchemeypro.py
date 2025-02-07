# from sqlalchemy import create_engine, ForeignKey, column, String, Integer, CHAR
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssn = Column('ssn', Integer, primary_key=True)
    firstname = Column('firstname',String)
    lastname = Column('lastname',String)
    gender = Column('gender',CHAR)
    age = Column('age',Integer)


    def __init__(self,ssn, firstname , lastname , gender,age):
        self.ssn = ssn 
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age 


    def __repr__(self):
        return f'{self.ssn}, { self.firstname}, {self.gender}, {self.age}'






