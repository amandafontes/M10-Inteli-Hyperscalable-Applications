from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    roles: str

    class Config:
        from_attributes = True  

class UserLogin(BaseModel):
    email: EmailStr
    password: str
