from pydantic import BaseModel
from datetime import datetime
from typing import Annotated,Optional


class TodoCreate(BaseModel):
  title:str
  description:str


class TodoResponse(BaseModel):
  id:int 
  title:str
  description:str
  created_at:datetime
  is_completed:bool
  class Config:
    form_attributes=True

class TodoUpdate(BaseModel):
    title: str
    description: str
    is_completed: bool  
    class Config:
     form_attributes=True  


class UserCreate(BaseModel):
  email:str
  password:str 

  class config:
    form_attributes=True

class UserOut(BaseModel):
  id:int
  email:str
  created_at:datetime
  class config:
    form_attributes=True

class Userlogin(BaseModel):
  email:str
  password:str    
  class config:
    form_attributes=True

class Token(BaseModel):
  access_token:str
  token_type:str

class TokenData(BaseModel):
  id:Optional[int]=None
