from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from backend.database import Base

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    operation = Column(String, nullable=False)
    status = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    entry_id = Column(Integer, ForeignKey("entry_lines.id"), nullable=True)
