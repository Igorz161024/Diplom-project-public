from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Finance(Base):
    __tablename__ = "finance"
    id = Column(Integer, primary_key=True, index=True)
    account = Column(String, index=True)
    balance = Column(Float)
