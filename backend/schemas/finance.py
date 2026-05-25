from pydantic import BaseModel
from typing import Optional

class FinanceBase(BaseModel):
    account: str
    balance: float

class FinanceCreate(FinanceBase):
    pass

class FinanceUpdate(BaseModel):
    account: Optional[str] = None
    balance: Optional[float] = None

class FinanceSchema(FinanceBase):
    id: int

    class Config:
        from_attributes = True
