from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/purchases", tags=["Purchases"])

# 🔹 Модель для закупівель
class Purchase(BaseModel):
    date: str
    supplier: str
    amount: int
    desc: str

# 🔹 Заглушка JSON для тесту
@router.get("/")
def get_purchases():
    return [
        {
            "date": "2026-04-21",
            "supplier": "Постачальник Х",
            "amount": 12000,
            "desc": "Закупівля сировини"
        }
    ]
