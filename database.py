from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# рядок підключення до PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:4568@localhost:5432/erp_diplom"
# створюємо engine і сесію
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)