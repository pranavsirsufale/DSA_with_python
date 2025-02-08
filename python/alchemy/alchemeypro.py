# from sqlalchemy import create_engine, ForeignKey, column, String, Integer, CHAR
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#?? Base Declaration
Base = declarative_base()

class Person(Base):
    #!! Table name will be people
    __tablename__ = 'people'

    #!!! Column names ( column name , datatype, optional null/pk/fk)
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


class Thing(Base):
    __tablename__ = 'things'

    tid = Column('tid',Integer,primary_key=True)
    description = Column('description',String)
    owner = Column(Integer, ForeignKey=('people.ssn'))


    def __init__(self,tid,description,owner):
        self.tid = tid
        self.description = description
        self.owner = owner 



##?? connect to sqlite data base
engine = create_engine('sqlite:///mydb.db',echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(100,'Pranav','Sirsufale', 'M',21)
# session.add(person)
# session.commit()

p1 = Person(101,'Pooja','Sirsufale','F',20)
p2 = Person(102,'Pallavi','Tadaskar','F',25)
p3 = Person(103,'Rohan','Magar','M',23)

# session.add_all([p1,p2,p3])
# session.commit()


results = session.query(Person).filter(Person.firstname.startswith('p') )

for row in results:
    print(f"SSN : {row.ssn} , firstname : {row.firstname} , lastname : { row.lastname} , Gender : {row.gender}")