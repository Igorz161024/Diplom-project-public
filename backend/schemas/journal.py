from pydantic import BaseModel
from datetime import date
from typing import Optional

class JournalBase(BaseModel):
    date: date
    operation: str
    status: str
    amount: float
    entry_id: Optional[int] = None

class JournalCreate(JournalBase):
    """Схема для створення нового запису"""
    pass

class JournalUpdate(BaseModel):
    """Схема для оновлення існуючого запису"""
    date: Optional[date] = None
    operation: Optional[str] = None
    status: Optional[str] = None
    amount: Optional[float] = None
    entry_id: Optional[int] = None

class JournalSchema(JournalBase):
    """Схема для читання запису (GET)"""
    id: int

    class Config:
        from_attributes = True  # ✅ правильний ключ для Pydantic v2
