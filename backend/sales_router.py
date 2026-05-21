from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Sales"])

class Sale(BaseModel):
    date: str
    customer: str
    amount: int
    desc: str

@router.get("/")
def get_sales():
    return [
        {
            "date": "2026-04-22",
            "customer": "ТОВ Рітейл",
            "amount": 15000,
            "desc": "Продаж товару"
        }
    ]

