from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from backend.database import Base

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    operation = Column(String, nullable=False)
    status = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    # ORM-зв’язок з entry_lines
    entry_lines = relationship("EntryLine", back_populates="journal")
