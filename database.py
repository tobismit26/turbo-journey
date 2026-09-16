import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Column, DateTime, func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    data = Column( DateTime, default=func.now())

load_dotenv() 

def create_my_engine():
    DB_URL = os.getenv("DATABASE")
    if not DB_URL:
        raise EnvironmentError("Переменная не найдена")
    
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    return session

def read_table(session):
    user = session.query(User).all()
    for i in user:
        print(i.name)

read_table(create_my_engine())

