from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # asset, liability, income, expense

    entries = relationship("Entry", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date = Column(Date, nullable=False)

    entries = relationship("Entry", back_populates="transaction")

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))
    debit = Column(Float, default=0)
    credit = Column(Float, default=0)
    description = Column(String)

    account = relationship("Account", back_populates="entries")
    transaction = relationship("Transaction", back_populates="entries")