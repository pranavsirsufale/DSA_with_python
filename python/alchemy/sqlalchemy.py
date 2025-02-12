from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

#! Created local Class and inherited from Base class to perform Database operations
class Marksheet(Base):
     #!! Table name will be marksheet
    __tablename__ = 'marksheet'

    #!! Creates columns 
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

##?? connect to sqlite data base by usinsg create engine
# engine = create_engine('sqlite:///mydb.db',echo=True)
# Base.metadata.create_all(bind=engine)


mysql_db_url = 'mysql:///root:Pranav@123@localhost:3306/bamu'
engine = create_engine(mysql_db_url,echo=True)

Base.metadata.create_all(bind=engine)



Session = sessionmaker(bind=engine)
session = Session()

#??? Create an Instace (Object) of The class 
pranav_mark = Marksheet(101,'Pranav','Sirsfuale')
##?? Add to the database ( insert record to the database)
session.add(pranav_mark)
##?? save the changes 
session.commit()


##?? GETTING ALL RECORDS 
records = session.query(Marksheet).all()
for record in records:
    print(f' STUDENT iD : { record.student_id} , STUDENT FIRST NAME : {record.student_name} , STUDENT LAST NAME : {record.last_name} ')


###? getting record  
student = session.query(Marksheet).filter(Marksheet.student_id == 101 )
print(student)



##?? GET RECORDS 
results = session.query(Marksheet).filter(Marksheet.student_name.startswith('p') )
for row in results:
    print(f"STUDENT ID: {row.student_id} , STUDENT NAME : {row.student_name} , lastname : { row.last_name}")



print(pranav_mark)