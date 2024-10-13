from pydantic import BaseModel
from typing import Optional



class AdminLogin(BaseModel):
    email: str
    password: str


class UserCreate(BaseModel):
    email: str
    password: str
    token: str