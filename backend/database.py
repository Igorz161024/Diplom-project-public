from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ⚙️ URL до БД з .env (docker-compose передає ці змінні)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:4568@db:5432/erp_diplom"
)

# 🔗 Engine для Postgres
engine = create_engine(DATABASE_URL)

# 🗂️ Сесії для роботи з БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 📦 Базовий клас для моделей
Base = declarative_base()
