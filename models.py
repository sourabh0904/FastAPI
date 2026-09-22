from sqlmodel import SQLModel, Field
from typing import Optional

#db table model
class Item(SQLModel , table=True):
    id: Optional[int] = Field(default=None , primary_key=True)
    name: str = Field(index=True)
    price: float = Field(gt=0)
    description: Optional[str] = None

#Request model
class ItemCreate(SQLModel):
    name: str
    price: float = Field(gt=0)
    description: Optional[str] = None

#update model
class ItemUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None , gt=0)
    description: Optional[str] = None
