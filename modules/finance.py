from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship, declarative_base
from database import SessionLocal
import datetime

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    description = Column(String)
    lines = relationship("EntryLine", back_populates="entry")

class EntryLine(Base):
    __tablename__ = "entry_lines"
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey("entries.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))
    debit = Column(Numeric(12,2), default=0)
    credit = Column(Numeric(12,2), default=0)
    entry = relationship("Entry", back_populates="lines")
    account = relationship("Account")

def add_account(code, name, type):
    s = SessionLocal(); a = Account(code=code, name=name, type=type)
    s.add(a); s.commit(); s.refresh(a); s.close(); return a

def add_entry(date, description, lines):
    s = SessionLocal(); e = Entry(date=date, description=description)
    s.add(e); s.commit()
    for l in lines: s.add(EntryLine(entry_id=e.id, account_id=l["account_id"], debit=l.get("debit",0), credit=l.get("credit",0)))
    s.commit(); s.refresh(e); s.close(); return e

def get_account_balance(account_id):
    s = SessionLocal()
    lines = s.query(EntryLine).filter_by(account_id=account_id).all()
    s.close(); return sum(l.debit for l in lines) - sum(l.credit for l in lines)