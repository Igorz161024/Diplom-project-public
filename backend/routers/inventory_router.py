from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models
from backend.schemas import InventorySchema, InventoryCreate, InventoryUpdate

router = APIRouter(
    tags=["Inventory"]
)

# --- CRUD для Inventory ---
@router.get("/", response_model=list[InventorySchema])
def read_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@router.post("/", response_model=InventorySchema)
def create_inventory(entry: InventoryCreate, db: Session = Depends(get_db)):
    new_entry = models.Inventory(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.put("/{entry_id}", response_model=InventorySchema)
def update_inventory(entry_id: int, entry: InventoryUpdate, db: Session = Depends(get_db)):
    db_entry = db.query(models.Inventory).filter(models.Inventory.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    for key, value in entry.dict(exclude_unset=True).items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete("/{entry_id}")
def delete_inventory(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Inventory).filter(models.Inventory.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    db.delete(db_entry)
    db.commit()
    return {"detail": "Запис видалено"}
