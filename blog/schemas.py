from typing import Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Creator(BaseModel):
    name: str
    email: str


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class Blog(BlogBase):
    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    user_id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
