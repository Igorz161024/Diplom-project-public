from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    entry_id = Column(Integer, ForeignKey("entry_lines.id"), nullable=True)
