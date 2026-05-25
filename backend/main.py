from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

import datetime
import pandas as pd
import io
import matplotlib.pyplot as plt

from backend.database import Base, engine
from backend.auth import create_access_token, get_current_user_role

# ✅ Підключаємо роутери (залишаємо їх як є)
from backend.routers import journal_router, finance_router, inventory_router, purchases_router, sales_router, legal_router

# ✅ Ініціалізація FastAPI
app = FastAPI(
    title="ERP Diplom Project",
    description="Backend API для фінансів, інвентаризації, закупівель, продажів та юридичних документів",
    version="1.0.0"
)

# ✅ Додаємо CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # дозволяємо фронтенд
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Створюємо таблиці у базі при старті
Base.metadata.create_all(bind=engine)

# ✅ Підключаємо роутери (без дублювання префіксів)
app.include_router(journal_router.router, tags=["Journal"])
app.include_router(finance_router.router, tags=["Finance"])
app.include_router(inventory_router.router, tags=["Inventory"])
app.include_router(purchases_router.router, tags=["Purchases"])
app.include_router(sales_router.router, tags=["Sales"])
app.include_router(legal_router.router, tags=["Legal"])

# 🔑 Логін з різними ролями
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    users = {
        "admin": "admin",
        "accountant": "accountant",
        "hr": "hr",
        "products": "products",
        "pkash": "pkash",
        "inventory": "inventory",
        "purchases": "purchases",
        "sales": "sales",
        "legal": "legal"
    }
    if form_data.username in users and form_data.password == "1234":
        role = users[form_data.username]
    else:
        raise HTTPException(status_code=400, detail="Невірний логін або пароль")

    access_token = create_access_token({"sub": form_data.username, "role": role})
    return {"access_token": access_token, "token_type": "bearer", "role": role}

# 📊 Ендпоінти для фінансових звітів
@app.post("/add_entry")
def create_entry(
    amount: int,
    description: str = "Продаж товару за готівку",
    role: str = Depends(get_current_user_role)
):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    from backend.modules.finance import get_account_balance, add_account, add_entry

    cash = add_account("30", "Cash", "актив")
    revenue = add_account("70", "Revenue", "дохід")

    add_entry(
        date=datetime.date.today(),
        description=description,
        lines=[
            {"account_id": cash.id, "debit": amount, "credit": 0},
            {"account_id": revenue.id, "debit": 0, "credit": amount}
        ]
    )

    return {
        "Баланс Cash": get_account_balance(cash.id),
        "Баланс Revenue": get_account_balance(revenue.id)
    }

@app.get("/balance/{account_id}")
def balance(account_id: int, role: str = Depends(get_current_user_role)):
    from backend.modules.finance import get_account_balance
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"account_id": account_id, "balance": get_account_balance(account_id)}

@app.get("/report")
def report(role: str = Depends(get_current_user_role)):
    from backend.modules.finance import get_account_balance
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    accounts = [
        {"id": 30, "name": "Cash", "balance": get_account_balance(30)},
        {"id": 70, "name": "Revenue", "balance": get_account_balance(70)},
    ]
    df = pd.DataFrame(accounts)
    summary = df.to_dict(orient="records")
    total = df["balance"].sum()
    return {"accounts": summary, "total_balance": total}

@app.get("/plot")
def plot_report(role: str = Depends(get_current_user_role)):
    from backend.modules.finance import get_account_balance
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    accounts = [
        {"id": 30, "name": "Cash", "balance": get_account_balance(30)},
        {"id": 70, "name": "Revenue", "balance": get_account_balance(70)},
    ]
    names = [acc["name"] for acc in accounts]
    balances = [acc["balance"] for acc in accounts]

    fig, ax = plt.subplots()
    ax.bar(names, balances, color=["green", "blue"])
    ax.set_title("Баланс рахунків")
    ax.set_ylabel("Сума")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
