from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models, schemas

router = APIRouter()

# 🟢 Отримати всі записи
@router.get("/", response_model=list[schemas.JournalRead])
def read_journal(db: Session = Depends(get_db)):
    return db.query(models.Journal).all()

# 🟢 Створити новий запис
@router.post("/", response_model=schemas.JournalRead)
def create_journal(entry: schemas.JournalCreate, db: Session = Depends(get_db)):
    new_entry = models.Journal(**entry.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

# 🟢 Оновити існуючий запис
@router.put("/{entry_id}", response_model=schemas.JournalRead)
def update_journal(entry_id: int, entry: schemas.JournalUpdate, db: Session = Depends(get_db)):
    db_entry = db.query(models.Journal).filter(models.Journal.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    for key, value in entry.dict(exclude_unset=True).items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

# 🟢 Видалити запис
@router.delete("/{entry_id}")
def delete_journal(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Journal).filter(models.Journal.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Запис не знайдено")
    db.delete(db_entry)
    db.commit()
    return {"detail": "Запис видалено"}
