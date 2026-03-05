from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# рядок підключення до PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:****@localhost:5432/diplom"

# створюємо engine і сесію
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)