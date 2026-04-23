from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/sales", tags=["Sales"])

# 🔹 Модель для продажів
class Sale(BaseModel):
    date: str
    customer: str
    amount: int
    desc: str

# 🔹 Заглушка JSON для тесту
@router.get("/")
def get_sales():
    return [
        {
            "date": "2026-04-21",
            "customer": "Клієнт Y",
            "amount": 8000,
            "desc": "Продаж готової продукції"
        }
    ]
