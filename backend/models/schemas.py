from pydantic import BaseModel
from datetime import date
from typing import Optional

class JournalSchema(BaseModel):
    id: int
    date: date
    description: str
    status: str
    amount: float
    entry_id: Optional[int] = None

    class Config:
        orm_mode = True
