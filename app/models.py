from app.database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Relationship


class Todo(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    is_completed=Column(Boolean,default=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=True,default=text("now()"))
    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    owner=Relationship("User")

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=True,default=text("now()"))

    
