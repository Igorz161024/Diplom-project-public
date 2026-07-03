from fastapi import APIRouter, Depends, HTTPException
from backend.database import SessionLocal
from backend.models import accounts
from backend.auth import get_current_user_role

router = APIRouter()

@router.get("/")
def get_accounts(role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    db = SessionLocal()
    result = db.query(accounts.Account).all()
    return result
