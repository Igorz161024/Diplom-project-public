from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)   # номер рахунку (наприклад, "30", "311", "92")
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)   # актив, пасив, витрата, дохід

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