from pydantic import BaseModel
from datetime import date

class JournalBase(BaseModel):
    date: date
    operation: str
    status: str
    amount: float

class JournalCreate(JournalBase):
    pass

class JournalUpdate(JournalBase):
    pass

class JournalSchema(JournalBase):
    id: int

    class Config:
        from_attributes = True  # для Pydantic v2
