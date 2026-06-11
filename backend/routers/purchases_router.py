from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import PurchasesSchema, PurchasesCreate, PurchasesUpdate

router = APIRouter(
    tags=["Purchases"]
)

# --- CRUD для Purchases ---
@router.get("/", response_model=list[PurchasesSchema])
def read_purchases(db: Session = Depends(get_db)):
    return db.query(models.Purchases).all()

@router.post("/", response_model=PurchasesSchema)
def create_purchase(entry: PurchasesCreate, db: Session = Depends(get_db)):
    new_entry = models.Purchases(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.put("/{entry_id}", response_model=PurchasesSchema)
def update_purchase(entry_id: int, entry: PurchasesUpdate, db: Session = Depends(get_db)):
    db_entry = db.query(models.Purchases).filter(models.Purchases.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    for key, value in entry.dict(exclude_unset=True).items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete("/{entry_id}")
def delete_purchase(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Purchases).filter(models.Purchases.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    db.delete(db_entry)
    db.commit()
    return {"detail": "Запис видалено"}
