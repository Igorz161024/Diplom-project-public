from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database import SessionLocal
from backend.models.journal import Journal
from backend.schemas.journal import JournalSchema, JournalCreate

# ❌ prefix тут не потрібен
router = APIRouter(tags=["Journal"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[JournalSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(Journal).order_by(Journal.id).all()

@router.post("/", response_model=JournalSchema)
def add_entry(entry: JournalCreate, db: Session = Depends(get_db)):
    db_entry = Journal(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.put("/{id}", response_model=JournalSchema)
def update_entry(id: int, entry: JournalCreate, db: Session = Depends(get_db)):
    db_entry = db.query(Journal).filter(Journal.id == id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete("/{id}")
def delete_entry(id: int, db: Session = Depends(get_db)):
    db_entry = db.query(Journal).filter(Journal.id == id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(db_entry)
    db.commit()
    return {"message": "Deleted successfully"}
