from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





Base = declarative_base()


class Marksheet(Base):
    __tablename__ = 'marksheet'

    student_id = Column('ID', Integer,primary_key=True)
    student_name = Column('student_name',String)
    last_name = Column('last_name',String, nullable=False)
    first_year_mark = Column('first_year_mark',Float,nullable=False) 
    second_year_mark = Column('second_year_mark',Float,nullable=True)
    third_year_mark = Column('third_year_mark',Float , nullable=True) 


    def __init__(self,student_id,student_name,last_name):
        self.student_id = student_id    
        self.student_name = student_name
        self.last_name = last_name

    def __repr__(self):
        return f"ID : {self.student_id} , FIRST NAME OF STUDENT : {self.student_name} , LAST NAME OF STUDENT : {self.last_name}"



mysql_db_url = 'mysql:///root:Pranav@123@localhost:3306/bamu'
engine = create_engine(mysql_db_url,echo=True)

Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


pranav_mark = Marksheet(101,'Pranav','Sirsfuale')

print(pranav_mark)


session.add(pranav_mark)

session.commit()