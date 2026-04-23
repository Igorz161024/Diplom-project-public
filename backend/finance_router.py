from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# 🔹 Модель для фінансових операцій
class FinanceEntry(BaseModel):
    date: str
    debit: str
    credit: str
    amount: int
    desc: str

# 🔹 Заглушка JSON для тесту
@router.get("/")
def get_finance():
    return [
        {
            "date": "2026-04-21",
            "debit": "Склад",
            "credit": "Постачальник",
            "amount": 5000,
            "desc": "Імпорт товару"
        }
    ]

