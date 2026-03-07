from database import engine
from modules.finance import Base, add_account, add_entry, get_account_balance
import datetime

# створюємо таблиці у базі
Base.metadata.create_all(bind=engine)

# створюємо рахунки
cash = add_account("30", "Cash", "актив")
revenue = add_account("70", "Revenue", "дохід")

# додаємо проводку: надходження готівки від доходу
add_entry(
    date=datetime.date.today(),
    description="Продаж товару за готівку",
    lines=[
        {"account_id": cash.id, "debit": 1000, "credit": 0},
        {"account_id": revenue.id, "debit": 0, "credit": 1000}
    ]
)

# виводимо баланси
print("Баланс Cash:", get_account_balance(cash.id))
print("Баланс Revenue:", get_account_balance(revenue.id))