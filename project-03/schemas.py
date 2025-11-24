# schemas.py
from pydantic import BaseModel
from typing import Optional


# Base schema: common fields for both create & read
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None


# For requests (when client sends data)
class ItemCreate(ItemBase):
    pass   # no extra fields, just reuse name + description


# For responses (what API returns)
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
