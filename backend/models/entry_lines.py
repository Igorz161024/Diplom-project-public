from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database import Base

class EntryLine(Base):
    __tablename__ = "entry_lines"

    id = Column(Integer, primary_key=True, index=True)
    journal_id = Column(Integer, ForeignKey("journal.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    description = Column(String(255), nullable=False)
