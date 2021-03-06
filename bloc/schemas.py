
from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str



class Blog(BaseModel):
    title:str
    body:str


class BlogBase(Blog):
    class Config():
        orm_mode=True

class UserBase(BaseModel):
    id:int
    name:str
    email:str
    class Config():
        orm_mode=True

class showUser(BaseModel):
    id:int
    name:str
    email:str
    blogs:List[BlogBase] =[]
    class Config():
        orm_mode=True

    
class showBlog(Blog):
    id:int
    creator:UserBase
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str
    class Config():
        orm_mode=True


class TokenData(BaseModel):
    email: Optional[str] = None
