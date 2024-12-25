from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Schema for updating an existing user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

# Schema for returning user data
class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models
