from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # debit / credit

    entries = relationship("Entry", back_populates="account")

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String)

    account = relationship("Account", back_populates="entries")