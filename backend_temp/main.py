from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import StreamingResponse
from database import engine
from modules.finance import Base, get_account_balance, add_account, add_entry
from auth import create_access_token, get_current_user_role

import datetime
import pandas as pd
import io
import matplotlib.pyplot as plt

app = FastAPI()

# створюємо таблиці у базі при старті
Base.metadata.create_all(bind=engine)

# Логін з різними ролями
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "1234":
        role = "admin"
    elif form_data.username == "accountant" and form_data.password == "1234":
        role = "accountant"
    elif form_data.username == "hr" and form_data.password == "1234":
        role = "hr"
    else:
        raise HTTPException(status_code=400, detail="Невірний логін або пароль")

    access_token = create_access_token({"sub": form_data.username, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
def read_root():
    return {"message": "ERP backend працює!"}

# Ендпоінт для бухгалтерів
@app.get("/finance")
def read_finance(role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Finance data visible"}

# Ендпоінт для кадровиків
@app.get("/hr")
def read_hr(role: str = Depends(get_current_user_role)):
    if role not in ["hr", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "HR data visible"}

# Ендпоінт для директора (адміна)
@app.get("/admin")
def read_admin(role: str = Depends(get_current_user_role)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return {"msg": "Admin panel visible"}

# Додавання проводки (захищено токеном)
@app.post("/add_entry")
def create_entry(
    amount: int,
    description: str = "Продаж товару за готівку",
    role: str = Depends(get_current_user_role)
):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

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
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"account_id": account_id, "balance": get_account_balance(account_id)}

@app.get("/report")
def report(role: str = Depends(get_current_user_role)):
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