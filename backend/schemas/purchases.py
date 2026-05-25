from pydantic import BaseModel
from typing import Optional

class PurchasesBase(BaseModel):
    supplier: str
    country: str
    amount: float

class PurchasesCreate(PurchasesBase):
    pass

class PurchasesUpdate(BaseModel):
    supplier: Optional[str] = None
    country: Optional[str] = None
    amount: Optional[float] = None

class PurchasesSchema(PurchasesBase):
    id: int

    class Config:
        from_attributes = True
