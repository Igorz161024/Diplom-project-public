from models import Base, Account, Entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Підключення до PostgreSQL (користувач postgres, пароль 4568)
engine = create_engine("postgresql+psycopg2://postgres:4568@localhost:5432/finance_db")

# Створення таблиць у базі
Base.metadata.create_all(engine)

# Сесія для роботи з даними
Session = sessionmaker(bind=engine)
session = Session()

# Тестове додавання рахунку
new_account = Account(name="Основний рахунок", type="debit")
session.add(new_account)
session.commit()

print("Таблиці створені, рахунок додано:", new_account.name)