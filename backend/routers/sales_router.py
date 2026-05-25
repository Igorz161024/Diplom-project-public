from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import SalesSchema, SalesCreate, SalesUpdate

router = APIRouter(
    prefix="/api/sales",
    tags=["sales"]
)

@router.get("/", response_model=list[SalesSchema])
def read_sales(db: Session = Depends(get_db)):
    return db.query(models.Sales).all()

@router.post("/", response_model=SalesSchema)
def create_sale(entry: SalesCreate, db: Session = Depends(get_db)):
    new_entry = models.Sales(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.put("/{entry_id}", response_model=SalesSchema)
def update_sale(entry_id: int, entry: SalesUpdate, db: Session = Depends(get_db)):
    db_entry = db.query(models.Sales).filter(models.Sales.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    for key, value in entry.dict(exclude_unset=True).items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete("/{entry_id}")
def delete_sale(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Sales).filter(models.Sales.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    db.delete(db_entry)
    db.commit()
    return {"detail": "Запис видалено"}
