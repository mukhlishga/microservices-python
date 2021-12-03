# pip install sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/perpustakaan', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

class Customers(Base):
    __tablename__ = 'customers'
    userid = Column(Integer, primary_key = True)
    username = Column(String)
    namadepan = Column(String)
    namabelakang = Column(String)
    email = Column(String)