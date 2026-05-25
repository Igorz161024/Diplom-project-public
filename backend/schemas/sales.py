from pydantic import BaseModel
from typing import Optional

class SalesBase(BaseModel):
    client: str
    invoice: str
    amount: float

class SalesCreate(SalesBase):
    pass

class SalesUpdate(BaseModel):
    client: Optional[str] = None
    invoice: Optional[str] = None
    amount: Optional[float] = None

class SalesSchema(SalesBase):
    id: int

    class Config:
        from_attributes = True
