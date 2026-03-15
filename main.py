from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import StreamingResponse
from database import engine
from modules.finance import Base, get_account_balance, add_account, add_entry
from auth import create_access_token, oauth2_scheme

import datetime
import pandas as pd
import io
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

from fastapi import Depends, Form
from auth import create_access_token, oauth2_scheme, verify_token

app = FastAPI()

# створюємо таблиці у базі при старті
Base.metadata.create_all(bind=engine)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "1234":
        raise HTTPException(status_code=400, detail="Невірний логін або пароль")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
def read_root():
    return {"message": "ERP backend працює!"}

@app.post("/add_entry")
def create_entry(
    amount: int,
    description: str = "Продаж товару за готівку",
    token: str = Depends(oauth2_scheme)   # захист через JWT
):
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
def balance(account_id: int):
    return {"account_id": account_id, "balance": get_account_balance(account_id)}

@app.get("/report")
def report():
    # приклад звіту з pandas
    accounts = [
        {"id": 30, "name": "Cash", "balance": get_account_balance(30)},
        {"id": 70, "name": "Revenue", "balance": get_account_balance(70)},
    ]
    df = pd.DataFrame(accounts)
    summary = df.to_dict(orient="records")
    total = df["balance"].sum()
    return {"accounts": summary, "total_balance": total}

@app.get("/plot")
def plot_report():
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