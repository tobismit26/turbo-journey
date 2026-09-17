import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from pydantic import BaseModel, EmailStr

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserProfile:
    def create_or_update(self, session, name:str, email:str) -> UserCreate:
        user = session.query(User).filter(User.name.like(f'{name}%')).all()
       # if user
        print(user[0].name)
        for i in user:
            print(i.name)




load_dotenv() 
#подключение к бд
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

session = create_my_engine()
#read_table(session)

aw = UserProfile()
aw.create_or_update(session, 'one', 'saha@gmail.com')